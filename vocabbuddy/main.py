from dotenv import load_dotenv
from fastapi import FastAPI

from vocabbuddy.llm import generate_cards
from vocabbuddy.models import FlashcardsOut, WordsIn

load_dotenv()

app = FastAPI(title="vocabbuddy")


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "ok", "app": "vocabbuddy"}


@app.post("/flashcards")
def make_flashcards(payload: WordsIn) -> FlashcardsOut:
    return FlashcardsOut(cards=generate_cards(payload.words, payload.max_cards))
