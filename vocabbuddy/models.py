from pydantic import BaseModel, Field


class WordsIn(BaseModel):
    words: str = Field(min_length=1, max_length=20000)
    max_cards: int = Field(default=10, ge=1, le=50)


class Flashcard(BaseModel):
    front: str
    back: str


class FlashcardsOut(BaseModel):
    cards: list[Flashcard]
