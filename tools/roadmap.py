"""Repository completion lists, kept separate from the CodeChef account snapshot."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def documented_codes():
    original = (ROOT/'data/all_solved.txt').read_text().split()
    additions = (ROOT/'data/completed.txt').read_text().split()
    return list(dict.fromkeys(original+additions))


def roadmap_slots():
    return json.loads((ROOT/'data/roadmap_slots.json').read_text())


def remaining_codes():
    done = set(documented_codes())
    return list(dict.fromkeys(code for course in roadmap_slots().values()
                              for code in course['slots'] if code not in done))


def all_roadmap_codes():
    return list(dict.fromkeys(code for course in roadmap_slots().values()
                              for code in course['slots']))
