from typer.testing import CliRunner

from termhelp.cli import app
from termhelp.core.orchestrator import explain_command

runner = CliRunner()


def test_orchestrator_explain_high_risk() -> None:
    result = explain_command("rm -rf /tmp/data")
    assert result["risks"]["level"] == "high"


def test_cli_explain_output() -> None:
    result = runner.invoke(app, ["explain", "rm -rf /tmp/data"])
    assert result.exit_code == 0
    assert "Summary" in result.output
    assert "Risks" in result.output
    assert "Level: high" in result.output
