# vocabbuddy

Guidance for Claude (trying out AI pair programming for real).

## What this is

FastAPI app + CLI that turns vocab lists into flashcards via the Claude API.

## Layout

- vocabbuddy/main.py — FastAPI app, POST /flashcards
- vocabbuddy/llm.py — the model call + the prompt (the heart of the whole thing)
- vocabbuddy/cli.py — CLI entry point
- vocabbuddy/export.py — markdown export

## Conventions

- type hints everywhere, ruff for lint (config in pyproject.toml)
- keep the prompt in llm.py, do not scatter prompt strings around
- never commit .env

## Current focus

Spaced repetition scheduling (SM-2 style) so decks are actually useful for review.
