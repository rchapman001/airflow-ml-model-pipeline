from playwright.async_api import async_playwright


async def get_browser():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=True)
    page = await browser.new_page()
    return playwright, browser, page


async def close_browser(playwright, browser):
    await browser.close()
    await playwright.stop()
