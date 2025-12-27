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


def schedule(card: ReviewCard, quality: int) -> ReviewCard:
    """SM-2, or at least the parts of it I understand so far.

    quality: 0-5 self rating after a review.
    """
    if quality < 3:
        card.interval_days = 1
    else:
        card.ease = max(1.3, card.ease + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        card.interval_days = round(card.interval_days * card.ease)
    # TODO: set card.due from interval_days and wire a review command into the cli
    return card
