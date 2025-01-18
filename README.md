# vocabbuddy

turn your vocab lists into flashcards, powered by claude.
mostly an excuse to finally learn FastAPI properly.

## running it

    python -m venv .venv && source .venv/bin/activate
    pip install -e .
    uvicorn vocabbuddy.main:app --reload

then poke around the docs at http://127.0.0.1:8000/docs

## todo

- [ ] /flashcards endpoint
- [ ] actually call the model
- [ ] some kind of export
- [ ] spaced repetition? ambitious
