from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from utils.entity_anonymizer import entity_positions, x_anonymize


api = FastAPI()

class Text(BaseModel):
    """Data Model for Text received by the requests."""
    name: str = 'Input Text'
    text: str

class AnonymizedText(BaseModel):
    """Data Model for X Anonymized Text send by the responses."""
    name: str = 'Anonymized Text'
    len: int
    text: str

class EntityPositions(BaseModel):
    name: str = 'Entity Positions'
    len: int
    entities: list[dict]

@api.get("/", response_class=HTMLResponse)
def get_root():
    return """
        <html>
            <h1>
                Text Anonymizer Root API
            </h1>
            <h3>
                To view API documentation go to <a href="/docs">Docs Here</a> or <a href="/redoc">Redocs Here</a>
            </h3>
        </html>
        """


@api.post("/entity_positions/", response_model=EntityPositions)
def get_entity_positions(text: Text):

    ent_pos = entity_positions(text.text)
    return EntityPositions(
        len=len(ent_pos),
        entities=ent_pos
    )

@api.post('/x_anonymize/', response_model=AnonymizedText)
def get_anonymized(text: Text):

    anonymized_text = x_anonymize(text.text)
    return AnonymizedText(
        len=len(anonymized_text),
        text=anonymized_text
    )
