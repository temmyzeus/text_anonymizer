import spacy
import streamlit as st


nlp = spacy.load('en_core_web_sm')

st.title('Text Anonymizer')

# create a batch input widget
with st.form(key='form'):
    text = st.text_area(
        label = 'Enter text here',
        height = 40,
        )
    submit_button = st.form_submit_button(
        label='Anonymize Text'
    )

def x_anonymize(text: str or spacy.tokens.Doc) -> str:
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
    if isinstance(text, spacy.tokens.Doc):
        doc = text
    elif isinstance(text, str):
        # make string spacy doc and tokenize to utilize spacy tokenizer
        doc = nlp(text.strip())
    else:
        raise TypeError('Text must be String or Spacy Doc')

    for token in doc.ents:
        token_len = len(token.text)

        # create new doc, where entity found is replaced by X
        anonymized_text = doc.text.replace(token.text, 'X'*token_len)
        anonymized_doc = nlp(anonymized_text)

        # update doc with the new_doc
        doc = anonymized_doc
    return anonymized_text


def get_entity_positions(text: str or spacy.tokens.Doc):
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
        if isinstance(text, spacy.tokens.Doc):
            doc = text
        elif isinstance(text, str):
            # make string spacy doc and tokenize to utilize spacy tokenizer
            doc = nlp(text.strip())
        else:
            raise TypeError('Text must be String or Spacy Doc')

        # entities and their positions
        ent_n_positions: list = list()
        entities = doc.ents

        for token in entities:
            start = token.start_char
            end = token.end_char
            ent_n_positions.append((token.text, start, end))
        return ent_n_positions


# run if text is entered and submitted
if text:
    doc = nlp(text)
    st.caption('Texts and Entities')

    anonymized_text = x_anonymize(text)

    # st.write([(token.text, token.ent_iob_) for token in doc])
    st.write(anonymized_text)
