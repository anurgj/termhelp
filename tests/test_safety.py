from termhelp.safety.classify import classify_command_safety

def test_high_risk_rm_rf() -> None:
    report = classify_command_safety("rm -rf /tmp/data")
    assert report["level"] == "high"
    assert any("deletion" in reason.lower() for reason in report["reasons"])

def test_medium_risk_find_delete() -> None:
    report = classify_command_safety("find . -name '*.tmp' -delete")
    assert report["level"] in {"medium", "high"}
    assert len(report["safer_alternatives"]) > 0

def test_low_risk_command() -> None:
    report = classify_command_safety("ls -la")
    assert report["level"] == "low"
    assert len(report["reasons"]) > 0