from src.utils.deployment_utils import deploy

def deploy_application(state):
    """Deploy the application"""
    return deploy(state["code"])