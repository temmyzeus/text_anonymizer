from typing import Optional
from fastapi import FastAPI
from app import get_entity_positions, x_anonymize

api = FastAPI()


@api.get("/")
def get_root():
    return "Text Anonymizer Roor API"


@api.get("/ent_pos/{text}")
def get_pos(text: str):
    ent_pos = get_entity_positions(text)
    return {
        'entity_positions': ent_pos
    }

@api.get('/x_anonymize/{text}')
def get_anonymized(text: str):
    anonymized_text = x_anonymize(text)
    return {
        'anonymized_text': anonymized_text
    }
