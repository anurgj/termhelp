"""Classifier that applies deterministic safety rules."""

from __future__ import annotations

from typing import Literal

from termhelp.safety.rules import RULES

RiskLevel = Literal["low", "medium", "high"]

def classify_command_safety(command_text: str) -> dict[str, object]:
    """
    Classify command text into risk metadata using deterministic regex rules.
    """

    matches = [rule for rule in RULES if rule.pattern.search(command_text)]
    if not matches:
        return {
            "level": "low",
            "reasons": ["No risky shell patterns matched known deterministic rules."],
            "safer_alternatives": ["Use dry-run or preview flags when available."],
        }
    
    level = _max_level([rule.severity for rule in matches])
    reasons = [rule.reason for rule in matches]

    safer_alternatives: list[str] = []
    for rule in matches:
        for alt in rule.safer_alternatives:
            if alt not in safer_alternatives:
                safer_alternatives.append(alt)

    return {
        "level": level,
        "reasons": reasons,
        "safer_alternatives": safer_alternatives,
    }

def _max_level(levels: list[str]) -> RiskLevel:
    order = {"low": 0, "medium": 1, "high": 2}
    best = max(levels, key=lambda value: order[value])
    return best # type: ignore[return-value]