# vocabbuddy

turn your vocab lists into flashcards, powered by claude.
mostly an excuse to finally learn FastAPI properly.

## running it

    python -m venv .venv && source .venv/bin/activate
    pip install -e .
    cp .env.example .env  # put your ANTHROPIC_API_KEY in there
    uvicorn vocabbuddy.main:app --reload

then poke around the docs at http://127.0.0.1:8000/docs

## cli

    python -m vocabbuddy.cli words.txt --max-cards 15
    python -m vocabbuddy.cli words.txt --out deck.md

## roadmap

- [x] /flashcards endpoint
- [x] real model call
- [x] cli
- [x] markdown export
- [ ] spaced repetition scheduling
- [ ] dedupe similar cards
- [ ] web ui, maybe, someday
