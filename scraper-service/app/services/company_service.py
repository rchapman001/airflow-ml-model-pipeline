import json
import os
from app.utils.browser import get_browser, close_browser
from app.models.scrape_models import ScrapeResponse


async def get_company_addresses(input_path: str, output_path: str) -> ScrapeResponse:
    with open(input_path, "r") as f:
        rows = [line.strip().split(",") for line in f.readlines()[1:]]

    # 🔄 Load existing records if file exists
    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            try:
                spacy_records = json.load(f)
            except json.JSONDecodeError:
                spacy_records = []
    else:
        spacy_records = []

    playwright, browser, page = await get_browser()

    for row in rows:
        state = row[0]
        zip_code = row[1]
        city = row[2]

        search_string = f"Top Companies in {city} {state} {zip_code}"
        print(f"Searching: {search_string}")

        try:
            await page.goto(f"https://www.google.com/maps?q={search_string}", timeout=60000)

            await page.wait_for_selector("a.hfpxzc", timeout=8000)

        except Exception:
            print(f"No results found for: {search_string}")
            continue

        results_locator = page.locator("a.hfpxzc")
        count = await results_locator.count()

        print(f"Found {count} results for {search_string}")

        for i in range(count):
            try:
                results_locator = page.locator("a.hfpxzc")
                result = results_locator.nth(i)

                await result.scroll_into_view_if_needed()
                await result.click()

                await page.wait_for_selector("h1.DUwDvf", timeout=10000)

                try:
                    raw_address = await page.locator("button[data-item-id='address']").inner_text()
                    address = raw_address.replace("Address:", "").strip()
                except:
                    address = None

                if address:
                    cleaned = clean_address(address)
                    spacy_records_batch = to_spacy_format(cleaned)

                    if spacy_records_batch:
                        for record in spacy_records_batch:
                            spacy_records.append(record)

                        # 💾 Write immediately after each batch
                        with open(output_path, "w") as f:
                            json.dump(spacy_records, f, indent=2)

                        print(f"Saved {len(spacy_records_batch)} records for: {cleaned}")

                    else:
                        print(f"Failed to format address: {address}")

                await page.keyboard.press("Escape")
                await page.wait_for_timeout(600)

            except Exception as e:
                print(f"Error scraping result {i}: {e}")

    await close_browser(playwright, browser)

    return ScrapeResponse(status="success", records_written=len(spacy_records))


def to_spacy_format(address: str) -> list[dict]:
    """
    Generate multiple spaCy training records with different comma placements:
    - street, city, state, zip
    - street, city state zip
    - street city, state zip
    - street city state, zip
    - street, city, state zip
    - street city, state, zip
    - street city state zip
    """
    records = []

    try:
        parts = [p.strip() for p in address.split(",")]
        if len(parts) != 3:
            return []

        street = parts[0]
        city = parts[1]

        state_zip = parts[2].split()
        if len(state_zip) != 2:
            return []

        state, zip_code = state_zip

        # (comma_after_street, comma_after_city, comma_after_state)
        variants = [
            (True, True, True),  # street, city, state, zip
            (True, False, False),  # street, city state zip
            (False, True, False),  # street city, state zip
            (False, False, True),  # street city state, zip
            (True, True, False),  # street, city, state zip
            (False, True, True),  # street city, state, zip
            (False, False, False),  # street city state zip
        ]

        for comma_after_street, comma_after_city, comma_after_state in variants:
            text_parts = []
            offsets = {}
            cursor = 0

            # STREET
            offsets["STREET"] = (cursor, cursor + len(street))
            text_parts.append(street)
            cursor += len(street)

            if comma_after_street:
                text_parts.append(",")
                cursor += 1

            text_parts.append(" ")
            cursor += 1

            # CITY
            offsets["CITY"] = (cursor, cursor + len(city))
            text_parts.append(city)
            cursor += len(city)

            if comma_after_city:
                text_parts.append(",")
                cursor += 1

            text_parts.append(" ")
            cursor += 1

            # STATE
            offsets["STATE"] = (cursor, cursor + len(state))
            text_parts.append(state)
            cursor += len(state)

            if comma_after_state:
                text_parts.append(",")
                cursor += 1

            text_parts.append(" ")
            cursor += 1

            # ZIP
            offsets["ZIP"] = (cursor, cursor + len(zip_code))
            text_parts.append(zip_code)
            cursor += len(zip_code)

            text = "".join(text_parts)

            entities = [
                (*offsets["STREET"], "STREET"),
                (*offsets["CITY"], "CITY"),
                (*offsets["STATE"], "STATE"),
                (*offsets["ZIP"], "ZIP"),
            ]

            records.append({"text": text, "entities": entities})

        return records

    except Exception:
        return []


def clean_address(address: str) -> str:
    return address.replace("\ue0c8", "").replace("\n", "").strip()
