from src.nodes.security_review import review_security

def test_review_security():
    state = {"code": "sample code"}
    result = review_security(state)
    assert "approved" in result