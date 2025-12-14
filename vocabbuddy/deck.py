"""Deck persistence — groundwork for spaced repetition."""

import json
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path

from vocabbuddy.models import Flashcard


@dataclass
class ReviewCard:
    front: str
    back: str
    interval_days: int = 1
    ease: float = 2.5
    due: str = field(default_factory=lambda: date.today().isoformat())


def new_deck(cards: list[Flashcard]) -> list[ReviewCard]:
    return [ReviewCard(front=c.front, back=c.back) for c in cards]


def save_deck(deck: list[ReviewCard], path: Path) -> None:
    path.write_text(json.dumps([asdict(c) for c in deck], indent=2), encoding="utf-8")


def load_deck(path: Path) -> list[ReviewCard]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [ReviewCard(**item) for item in raw]
