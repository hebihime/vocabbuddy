"""Export a deck of cards to markdown."""

from vocabbuddy.models import Flashcard


def to_markdown(cards: list[Flashcard]) -> str:
    lines = ["# flashcards", ""]
    for card in cards:
        lines.append(f"## {card.front}")
        lines.append("")
        lines.append(card.back)
        lines.append("")
    return "\n".join(lines)
