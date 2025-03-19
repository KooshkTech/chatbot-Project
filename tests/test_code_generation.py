from src.nodes.code_generation import generate_code

def test_generate_code():
    state = {"design_docs": "sample design"}
    result = generate_code(state)
    assert "code" in result