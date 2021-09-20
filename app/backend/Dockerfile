# get base image
FROM python:3.9.1

WORKDIR /text_anonymize

RUN apt-get update

RUN pip install flask spacy streamlit uvicorn fastapi

RUN python3 -m spacy download en_core_web_sm

COPY . /text_anonymize/

EXPOSE 8000

ENTRYPOINT [ "python3" ]

CMD [ "app/api.py" ]