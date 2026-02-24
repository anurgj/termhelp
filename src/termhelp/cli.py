"""CLI entrypoint for termhelp."""

from __future__ import annotations

import typer

from termhelp.core.orchestrator import explain_command

app = typer.Typer(help="Beginner-friendly terminal tutor.")

@app.command()
def hello() -> None:
    """Temporary command to verify CLI wiring"""
    typer.echo("termhelp is installed and running.")

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