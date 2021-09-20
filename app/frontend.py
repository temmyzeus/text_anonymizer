import streamlit as st
from utils.entity_anonymizer import nlp, x_anonymize, get_entity_positions


st.title('Text Anonymizer')

# create a batch input widget
with st.form(key='form'):
    text = st.text_area(
        label = 'Enter text here',
        height = 40,
        )
    pos_or_x = st.selectbox(
        label='Get Entity Positions or Replace Entity with X\'s',
        options=('Get Entity Positions', 'X Anonymize Entities',),
        index=1,
    )
    submit_button = st.form_submit_button(
        label='Anonymize Text'
    )

# run if text is entered and submitted
if text:
    doc = nlp(text)
    st.caption('Texts and Entities')
    if (pos_or_x == 'Get Entity Positions'):
        entity_pos = get_entity_positions(text)
        st.write(entity_pos)
    elif (pos_or_x == 'X Anonymize Entities'):
        anonymized_text = x_anonymize(text)
        st.write(anonymized_text)
