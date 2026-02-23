"""Safety rules for risky shell patterns."""

from __future__ import annotations

from dataclasses import dataclass
from re import Pattern, compile

@dataclass(frozen=True)
class SafetyRule:
    """A regex-based rule describing a risky shell pattern."""

    id: str
    pattern: Pattern[str]
    severity: str # "low" | "medium" | "high"
    reason: str
    safer_alternatives: tuple[str, ...]

RULES: tuple[SafetyRule, ...] = (
    SafetyRule(
        id="rm-rf",
        pattern=compile(r"\brm\s+-[^\n]*r[^\n]*f\b|\brm\s+-[^\n]*f[^\n]*r\b"),
        severity="high",
        reason="Recursive forced deletion can permanently remove large directory trees.",
        safer_alternatives=(
            "Preview targets with `ls` or `find` first.",
            "Use `rm -i` for confirmation where possible.",
        ),
    ),
    SafetyRule(
        id="dd",
        pattern=compile(r"\bdd\b"),
        severity="high",
        reason="`dd` can overwrite disks without interactive confirmation.",
        safer_alternatives=(
            "Double check source/destination with `lsblk` before running.",
        ),
    ),
    SafetyRule(
        id="mkfs",
        pattern=compile(r"\bmkfs(\.[a-z0-9]+)?\b", flags=0),
        severity="high",
        reason="`mkfs` formats filesystems and destroys existing data on target devices.",
        safer_alternatives=(
            "Verify the exact device path with `lsblk -f` first",
        ),
    ),
    SafetyRule(
        id="chmod-777-recursive",
        pattern=compile(r"\bchmod\s+-R\s+777\b|\bchmod\s+777\s+-R\b"),
        severity="high",
        reason="Recurive `chmod 777` creates broad write access and security risk.",
        safer_alternatives=(
            "Use least-privilege modes like `755` for directories and `644` for files.",
        ),
    ),
    SafetyRule(
        id="chown-recursive",
        pattern=compile(r"\bchown\s+-R\b|\bchown\b[^\n]*\s-R\b"),
        severity="medium",
        reason="Recursive ownership changes can break application and system permissions.",
        safer_alternatives=(
            "Limit ownership changes to specific paths and verify with `ls -l`.",
        ),
    ),
    SafetyRule(
        id="redirect-dev",
        pattern=compile(r">\s*/dev/[^\s]+"),
        severity="high",
        reason="Redirecting output to `/dev/*` can target devices and cause data loss.",
        safer_alternatives=(
            "Write output to a regular file unless device output is intentional.",
        ),
    ),
    SafetyRule(
        id="pipe-to-sudo",
        pattern=compile(r"\|\s*sudo\b"),
        severity="high",
        reason="Piping data directly into privileged commands can execute unsafe input.",
        safer_alternatives=(
            "Inspect command output first before running with `sudo`.",
        ),
    ),
    SafetyRule(
        id="find-delete",
        pattern=compile(r"\bfind\b[^\n]*\s-delete\b"),
        severity="medium",
        reason="`find ... -delete` can remove more files than intended.",
        safer_alternatives=(
            "Run the same `find` command without `-delete` to preview matches.",
        ),
    ),
)