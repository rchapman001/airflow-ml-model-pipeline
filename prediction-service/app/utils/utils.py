import spacy

_nlp = None


def get_nlp(model_path: str):
    global _nlp
    if _nlp is None:
        _nlp = spacy.load(model_path)
    return _nlp
