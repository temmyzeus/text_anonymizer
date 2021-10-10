import en_core_web_sm
from spacy.tokens import Doc

nlp = en_core_web_sm.load()

def x_anonymize(text: str or Doc) -> str:
    """
    Anonymize Name Entities by Replacing them with X

    Arguments:
    ----------
        text: str or spacy.tokens.Doc

    Returns:
    --------
        anonymized_text: str
    """
    # specify global variables used
    global nlp

    # get list of tokens if type is spacy doc or string
    if isinstance(text, Doc):
        doc = text
    elif isinstance(text, str):
        # make string spacy doc and tokenize to utilize spacy tokenizer
        doc = nlp(text.strip())
    else:
        raise TypeError('Text must be String or Spacy Doc')
    entities = doc.ents
    anonymized_text = doc.text

    for token in entities:
        token_len = len(token.text)
        anonymized_text = anonymized_text.replace(token.text, 'X'*token_len)

        # update doc with the new_doc
        # doc = anonymized_doc
    return anonymized_text

def get_entity_positions(text: str or Doc):
        """
        Get the starting and ending positions of named entities
        from text.

        Arguments:
        ----------
            text: str or spacy.tokens.Doc

        Returns:
        --------
            ent_n_positions: list
        """
        # specify global variables used
        global nlp

        # get list of tokens if type is spacy doc or string
        if isinstance(text, Doc):
            doc = text
        elif isinstance(text, str):
            # make string spacy doc and tokenize to utilize spacy tokenizer
            doc = nlp(text.strip())
        else:
            raise TypeError('Text must be String or Spacy Doc')

        entities = doc.ents
        # entities and their positions
        ent_n_positions:list = [{
            'word': token.text,
            'start':token.start_char,
            'stop':token.end_char
        } for token in entities]
        return ent_n_positions
