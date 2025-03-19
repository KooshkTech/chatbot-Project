from src.nodes.deployment import deploy_application

def test_deploy_application():
    state = {"code": "sample code"}
    result = deploy_application(state)
    assert "status" in result