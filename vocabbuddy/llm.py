"""Talk to the Claude API and turn word lists into flashcards."""

import json
import os

import httpx

from vocabbuddy.models import Flashcard

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-3-opus-20240229"

PROMPT = """You are a language tutor. Turn the word list below into vocabulary flashcards.

Rules:
- make at most {max_cards} cards
- each card covers exactly one word or short phrase
- fronts are the word in the foreign language, backs are the English translation
- reply with ONLY a JSON array of {{"front": ..., "back": ...}} objects, nothing else

Words:
{words}
"""


def _strip_fences(text: str) -> str:
    # claude sometimes wraps the JSON in ```json fences no matter what
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
    return text.removesuffix("```").strip()


def generate_cards(words: str, max_cards: int) -> list[Flashcard]:
    body = {
        "model": MODEL,
        "max_tokens": 2048,
        "messages": [
            {"role": "user", "content": PROMPT.format(max_cards=max_cards, words=words)},
        ],
    }
    headers = {
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    # 30 second timeout because long word lists blow way past the default,
    # found that out the hard way
    resp = httpx.post(API_URL, json=body, headers=headers, timeout=30.0)
    resp.raise_for_status()
    text = resp.json()["content"][0]["text"]
    cards = json.loads(_strip_fences(text))
    return [Flashcard(**card) for card in cards[:max_cards]]
