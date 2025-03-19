from src.nodes.user_stories import generate_user_stories

def test_generate_user_stories():
    state = {"requirements": "sample requirements"}
    result = generate_user_stories(state)
    assert "user_stories" in result