from typer.testing import CliRunner

from termhelp.cli import app
from termhelp.core.orchestrator import debug_error

runner = CliRunner()


def test_orchestrator_debug_returns_structure() -> None:
    result = debug_error("permission denied")
    assert "summary" in result
    assert "risks" in result
    assert "next_steps" in result


def test_cli_debug_with_text_option() -> None:
    result = runner.invoke(app, ["debug", "--text", "rm -rf /tmp/data"])
    assert result.exit_code == 0
    assert "Summary" in result.output
    assert "Risks" in result.output
    assert "Level: high" in result.output


def test_cli_debug_with_stdin() -> None:
    result = runner.invoke(app, ["debug"], input="dd if=/dev/zero of=/dev/sda")
    assert result.exit_code == 0
    assert "Risks" in result.output
    assert "Level: high" in result.output
