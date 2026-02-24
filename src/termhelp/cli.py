"""CLI entrypoint for termhelp."""

from __future__ import annotations

import sys
import typer

from termhelp.core.orchestrator import debug_error, explain_command

app = typer.Typer(help="Beginner-friendly terminal tutor.")

@app.command()
def explain(command: str) -> None:
    """Explain a terminal command and highlight safety risk."""

    result = explain_command(command)
    risks = result["risks"]

    typer.echo("Summary")
    typer.echo(str(result["summary"]))
    typer.echo("")

    typer.echo("Breakdown")
    for item in result["breakdown"]:
        typer.echo(f"- {item}")
    typer.echo("")

    typer.echo("Risks")
    typer.echo(f"Level: {risks['level']}")
    typer.echo("Reasons:")
    for reason in risks["reasons"]:
        typer.echo(f"- {reason}")
    typer.echo("Safer alternatives:")
    for alt in risks["safer_alternatives"]:
        typer.echo(f"- {alt}")
    typer.echo("")

    typer.echo("Next steps")
    for step in result["next_steps"]:
        typer.echo(f"- {step}")

@app.command()
def debug(text: str | None = typer.Option(None, "--text", help="Error text to debug.")) -> None:
    """Debug terminal error output from --text or stdin."""

    payload = text
    if not payload and not sys.stdin.isatty():
        payload = sys.stdin.read().strip()

    if not payload:
        raise typer.BadParameter("Provide --text or pipe error output to stdin.")

    result = debug_error(payload)
    risks = result["risks"]

    typer.echo("Summary")
    typer.echo(str(result["summary"]))
    typer.echo("")

    typer.echo("Breakdown")
    for item in result["breakdown"]:
        typer.echo(f"- {item}")
    typer.echo("")

    typer.echo("Risks")
    typer.echo(f"Level: {risks['level']}")
    typer.echo("Reasons:")
    for reason in risks["reasons"]:
        typer.echo(f"- {reason}")
    typer.echo("Safer alternatives:")
    for alt in risks["safer_alternatives"]:
        typer.echo(f"- {alt}")
    typer.echo("")

    typer.echo("Next steps")
    for step in result["next_steps"]:
        typer.echo(f"- {step}")
