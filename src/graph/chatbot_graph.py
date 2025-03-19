from typing import TypedDict, Optional, Tuple
from langgraph.graph import StateGraph
from src.nodes import user_input, user_stories, product_review, design_docs, code_generation

# Define the state schema
class WorkflowState(TypedDict):
    user_input: Optional[str]
    requirements: Optional[str]
    validated: Optional[bool]
    user_stories: Optional[str]
    approved: Optional[bool]
    feedback: Optional[str]
    design_docs: Optional[str]
    code: Optional[str]

def create_workflow() -> Tuple[any, list, list]:
    """Create and compile the workflow, returning the compiled workflow, nodes, and edges."""
    # Initialize the workflow with the state schema
    workflow = StateGraph(WorkflowState)
    
    # Add nodes
    workflow.add_node("collect_requirements", user_input.get_user_requirements)
    workflow.add_node("validate_requirements", user_input.validate_input)
    workflow.add_node("generate_stories", user_stories.generate_user_stories)
    workflow.add_node("review_stories", product_review.product_owner_review)
    workflow.add_node("create_design_docs", design_docs.create_design_docs)
    workflow.add_node("generate_code", code_generation.generate_code)
    
    # Set edges
    workflow.add_edge("collect_requirements", "validate_requirements")
    workflow.add_edge("validate_requirements", "generate_stories")
    workflow.add_edge("generate_stories", "review_stories")
    workflow.add_edge("review_stories", "create_design_docs")
    workflow.add_edge("create_design_docs", "generate_code")
    
    # Set entry point
    workflow.set_entry_point("collect_requirements")
    
    # Extract nodes and edges before compiling
    nodes = list(workflow.nodes)
    edges = list(workflow.edges)
    
    # Compile the workflow
    compiled_workflow = workflow.compile()
    
    return compiled_workflow, nodes, edges