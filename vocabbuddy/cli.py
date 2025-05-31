"""Little CLI so you don't need the server running for a one-off deck."""

import argparse
from pathlib import Path

from dotenv import load_dotenv

from vocabbuddy.llm import generate_cards


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(prog="vocabbuddy")
    parser.add_argument("words_file", type=Path, help="text file with your vocab words")
    parser.add_argument("--max-cards", type=int, default=10)
    args = parser.parse_args()

    words = args.words_file.read_text(encoding="utf-8")
    cards = generate_cards(words, args.max_cards)
    for i, card in enumerate(cards, 1):
        print(f"{i}. {card.front}")
        print(f"   -> {card.back}")


if __name__ == "__main__":
    main()
