from fastapi import FastAPI

from vocabbuddy.models import Flashcard, FlashcardsOut, WordsIn

app = FastAPI(title="vocabbuddy")


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "ok", "app": "vocabbuddy"}


@app.post("/flashcards")
def make_flashcards(payload: WordsIn) -> FlashcardsOut:
    # canned response until the real model call goes in
    return FlashcardsOut(
        cards=[
            Flashcard(front="el gato", back="the cat (Spanish)"),
            Flashcard(front="ねこ", back="cat (Japanese)"),
        ]
    )
