from typing import Optional

import uvicorn
from fastapi import FastAPI

from entity_anonymizer import get_entity_positions, x_anonymize


api = FastAPI()


@api.get("/")
def get_root():
    return "Text Anonymizer Root API"


@api.post("/ent_pos/{text}")
def get_pos(text: str):
    ent_pos = get_entity_positions(text)
    return {
        'entity_positions': ent_pos
    }

@api.post('/x_anonymize/{text}')
def get_anonymized(text: str):
    anonymized_text = x_anonymize(text)
    return {
        'anonymized_text': anonymized_text
    }

if __name__ == '__main__':
    uvicorn.run('api:api', host='0.0.0.0', port=8000)
