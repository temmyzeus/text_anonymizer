# get base image
FROM python:3.9.1

WORKDIR /text_anonymize

RUN apt-get update

RUN pip install streamlit

COPY . /text_anonymize/

EXPOSE 8000

ENTRYPOINT [ "streamlit" ]

CMD [ "run" , "frontend.py"]