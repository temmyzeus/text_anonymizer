from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from utils.entity_anonymizer import entity_positions, x_anonymize


api = FastAPI()

class Text(BaseModel):
    """Data Model for Text received by the requests."""
    name: str = 'Text'
    text: str

class AnonymizedText(BaseModel):
    """Data Model for X Anonymized Text send by the responses."""
    name: str = 'Anonymized Text'
    len: int
    text: str

class EntityPositions(BaseModel):
    name: str = 'Entity Positions'
    len: int
    entities: list

@api.get("/")
def get_root():
    return "Text Anonymizer Root API"


@api.post("/ent_pos/")
def get_pos(text: Text):

    ent_pos = entity_positions(text.text)
    return EntityPositions(
        len=len(ent_pos),
        entities=ent_pos
    )

@api.post('/x_anonymize/')
def get_anonymized(text: Text):

    anonymized_text = x_anonymize(text.text)
    return AnonymizedText(
        len=len(anonymized_text),
        text=anonymized_text
    )
