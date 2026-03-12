from gmail_no_send.utils import audit_log


def test_audit_log(tmp_path, monkeypatch):
    monkeypatch.setenv("GMAIL_NO_SEND_CONFIG", str(tmp_path))
    audit_log("test", {"x": 1})
    log = (tmp_path / "audit.log").read_text().strip()
    assert "\"action\": \"test\"" in log
