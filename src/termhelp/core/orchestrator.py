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

def debug_error(error_text: str) -> dict[str, object]:
    """Build debug response using deterministic safety analysis."""

    safety = classify_command_safety(error_text)

    return {
        "summary": "This error output was analyzed with deterministic heuristics.",
        "breakdown": [
            "Check the first concrete error line for missing path, permission, or command usage issues.",
            "Use the risk section to avoid unsafe retry attempts.",
        ],
        "risks": safety,
        "next_steps": [
            "Re-run with a narrower/safer command variant.",
            "Validate target path/device/flags before retrying.",
            "If available, run a non-destructive preview first.",
        ],
    }
