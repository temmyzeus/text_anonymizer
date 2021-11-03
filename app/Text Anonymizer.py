import requests
import streamlit as st
from utils.entity_anonymizer import nlp


def get_x_anomymize(text: str):
    full_url = 'http://api:8000/x_anonymize/'
    json = {
        "name": "Text",
        "text": text
    }
    response = requests.post(full_url, json=json)
    return response.json()

def get_ent_pos(text: str):
    global url, port
    full_url = 'http://api:8000/entity_positions/'
    json = {
        "name": "Text",
        "text": text
    }
    response = requests.post(full_url, json=json)
    return response.json()

st.markdown('''
        ##### Built by Temiloluwa Awoyele
        ##### [Github](https://github.com/temmyzeus) | \
        [Twitter](https://twitter.com/temmyzeus100) | \
        [LinkedIn](https://www.linkedin.com/in/temiloluwa-awoyele/) | \
        [Go to API] (http://ec2-3-235-197-114.compute-1.amazonaws.com:8000)
        ''')

about = st.sidebar.markdown(
    """
    ## About the App
    This app is a Text Anonymizer that helps to obscure sensitive informations i.e Naming Entites like
    person, place, time, cardinal e.t.c in text.

    Requets to API can be sent on 2 paths:

    1. x_anonymize => Replaces naming entities with X's
    ```
    http://ec2-3-235-197-114.compute-1.amazonaws.com:8000/x_anonymize
    ```
    2. entity_positions => Gets positions of all named entities
    ```
    http://ec2-3-235-197-114.compute-1.amazonaws.com:8000/entity_positions
    ```

    Send POST Requests via Python
    ```
    # Send Post Request to API using Python
    import requests
    send_json = {
        'name': 'Input Text',
        'text': 'Your Text Here'
    }
    x_anonymize_api = 'http://ec2-3-235-197-114.compute-1.amazonaws.com:8000/x_anonymize'
    get_entity_positions_api = 'http://ec2-3-235-197-114.compute-1.amazonaws.com:8000/entity_positions'
    response = requests.post(x_anonymize_api, json=send_json)
    print(reponse.text)
    ```
    """
)

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
show_api_out = st.checkbox(label='Show raw API output', value=False)
st.caption('Code can be found here: https://github.com/temmyzeus/text_anonymizer')

# run if text is entered and submitted
if text:
    doc = nlp(text)
    st.caption('Texts and Entities')
    if (pos_or_x == 'Get Entity Positions'):
        entity_pos = get_ent_pos(text)
        # Show raw api out it true, else show just the text
        if show_api_out:
            st.write(entity_pos)
        else:
            st.write(entity_pos['entities'])
    elif (pos_or_x == 'X Anonymize Entities'):
        anonymized_text = get_x_anomymize(text)
        # Show raw api out it true, else show just the text
        if show_api_out:
            st.write(anonymized_text)
        else:
            st.write(anonymized_text['text'])

        # Download Text when X_Anonymized
        st.download_button(
                label='Download',
                data=anonymized_text['text'],
                help='Download anonymized text'
        )
