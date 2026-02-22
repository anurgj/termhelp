"""CLI entrypoint for termhelp."""

from __future__ import annotations

import typer

app = typer.Typer(help="Beginner-friendly terminal tutor.")

@app.command()
def hello() -> None:
    """Temporary command to verify CLI wiring"""
    typer.echo("termhelp is installed and running.")