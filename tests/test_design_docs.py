from src.nodes.design_docs import create_design_docs

def test_create_design_docs():
    state = {"user_stories": "sample stories"}
    result = create_design_docs(state)
    assert "design_docs" in result