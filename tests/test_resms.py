import resms
import pytest
from resms import ReSMS

def test_requires_key():
    with pytest.raises(ValueError):
        ReSMS("")

def test_success(monkeypatch):
    class FakeResp:
        ok = True
        def json(self): return {"id": "1", "status": "queued"}
    monkeypatch.setattr(resms._client.requests, "post", lambda *a, **k: FakeResp())

    client = ReSMS("key")
    result = client.send(to="+336123", message="hi")
    assert result.status == "queued"