"""Orchestrator for CLI flows."""

from __future__ import annotations

from termhelp.safety.classify import classify_command_safety

def explain_command(command_text: str) -> dict[str,object]:
    """Build explain response using deterministic safety analysis."""

    safety = classify_command_safety(command_text)

    return {
        "summary": f"This command was analyzed before execution: `{command_text}`",
        "breakdown": [
            "The command was checked against deterministic risk patterns.",
            "Use risk reasons and alternatives to whether to proceed.",
        ],
        "risks": safety,
        "next_steps": list(safety["safer_alternatives"])[:3],
    }