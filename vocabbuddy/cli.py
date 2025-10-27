"""Little CLI so you don't need the server running for a one-off deck."""

import argparse
from pathlib import Path

from dotenv import load_dotenv

from vocabbuddy.export import to_markdown
from vocabbuddy.llm import generate_cards


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(prog="vocabbuddy")
    parser.add_argument("words_file", type=Path, help="text file with your vocab words")
    parser.add_argument("--max-cards", type=int, default=10)
    parser.add_argument("--out", type=Path, default=None, help="write the deck to a markdown file")
    args = parser.parse_args()

    words = args.words_file.read_text(encoding="utf-8")
    cards = generate_cards(words, args.max_cards)

    if args.out is not None:
        args.out.write_text(to_markdown(cards), encoding="utf-8")
        print(f"wrote {len(cards)} cards to {args.out}")
        return
    for i, card in enumerate(cards, 1):
        print(f"{i}. {card.front}")
        print(f"   -> {card.back}")


if __name__ == "__main__":
    main()
