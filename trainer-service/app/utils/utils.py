import random
import spacy
from spacy.training.example import Example


def train_ner_model(training_data: list, output_dir: str, n_iter: int = 20):
    """
    Train a spaCy NER model and persist it to disk,
    skipping invalid / overlapping training examples.
    """

    nlp = spacy.blank("en")

    # Add NER pipe
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    else:
        ner = nlp.get_pipe("ner")

    # Register labels
    for item in training_data:
        for _, _, label in item["entities"]:
            ner.add_label(label)

    optimizer = nlp.initialize()

    for i in range(n_iter):
        random.shuffle(training_data)
        losses = {}

        for idx, item in enumerate(training_data):
            text = item["text"]
            entities = item["entities"]

            doc = nlp.make_doc(text)

            try:
                # ✅ Validate example BEFORE training
                example = Example.from_dict(doc, {"entities": entities})

            except Exception as e:
                print("\n🚨 SKIPPING INVALID TRAINING EXAMPLE")
                print(f"➡️  Record {idx}")
                print(f"Text: {repr(text)}")
                print(f"Entities: {entities}")
                print(f"Error: {e}")
                continue  # 🔥 skip bad record instead of crashing

            # ✅ Only update model if example is valid
            nlp.update([example], sgd=optimizer, losses=losses)

        print(f"Iteration {i + 1}/{n_iter} - Losses: {losses}")

    # Persist model
    nlp.to_disk(output_dir)
    return nlp
