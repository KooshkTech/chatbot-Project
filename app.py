import streamlit as st
from pyvis.network import Network
import json
import base64

# Function to visualize the workflow graph using pyvis
def visualize_workflow_with_pyvis(workflow):
    """Generate an interactive workflow graph using pyvis."""
    net = Network(height="500px", width="100%", notebook=False, directed=True)
    
    # Add nodes
    for step in workflow:
        net.add_node(step["step"], label=step["step"])
    
    # Add edges
    for step in workflow:
        for next_step in step["next_steps"]:
            net.add_edge(step["step"], next_step)
    
    # Generate HTML file
    net.save_graph("workflow.html")
    return "workflow.html"

# Function to create a download link for files
def get_download_link(file_data, file_name, file_format):
    """Generate a download link for a file."""
    b64 = base64.b64encode(file_data.encode()).decode()
    href = f'<a href="data:file/{file_format};base64,{b64}" download="{file_name}.{file_format}">Download {file_format.upper()}</a>'
    return href

# Streamlit App
st.title("Custom Workflow Generator")

# User input
user_input = st.text_area("Enter your requirements:")

# Toggle options
display_steps = st.checkbox("Display Workflow Steps", value=True)
display_graph = st.checkbox("Display Workflow Graph", value=True)

# Button to generate workflow
if st.button("Generate Workflow"):
    if user_input:
        # Example workflow (replace this with your Groq API call)
        workflow = [
            {"step": "Clinic Registration", "description": "Register the clinic with local health authorities.", "next_steps": ["Clinic Setup"]},
            {"step": "Clinic Setup", "description": "Design and set up the clinic layout.", "next_steps": ["Staff Hiring"]},
            {"step": "Staff Hiring", "description": "Recruit and train staff.", "next_steps": ["Patient Registration"]},
            {"step": "Patient Registration", "description": "Create a system for patient onboarding.", "next_steps": ["Appointment Scheduling"]},
            {"step": "Appointment Scheduling", "description": "Set up a booking system.", "next_steps": ["Initial Consultation"]},
            {"step": "Initial Consultation", "description": "Conduct patient consultations.", "next_steps": ["Treatment Planning"]},
            {"step": "Treatment Planning", "description": "Develop personalized treatment plans.", "next_steps": ["Dental Procedures"]},
            {"step": "Dental Procedures", "description": "Perform treatments.", "next_steps": ["Billing and Insurance"]},
            {"step": "Billing and Insurance", "description": "Generate invoices and process claims.", "next_steps": ["Inventory Management"]},
            {"step": "Inventory Management", "description": "Track and reorder supplies.", "next_steps": ["Clinic Operations"]},
            {"step": "Clinic Operations", "description": "Oversee daily activities.", "next_steps": ["Patient Follow-Up", "Clinic Marketing"]},
            {"step": "Patient Follow-Up", "description": "Schedule post-treatment checkups.", "next_steps": ["Feedback Collection"]},
            {"step": "Clinic Marketing", "description": "Promote the clinic to attract patients.", "next_steps": ["Patient Registration"]},
            {"step": "Feedback Collection", "description": "Collect and analyze patient feedback.", "next_steps": ["Clinic Operations"]},
            {"step": "Staff Performance Reviews", "description": "Evaluate and train staff.", "next_steps": ["Clinic Operations"]}
        ]
        
        # Display workflow steps if toggled
        if display_steps:
            st.write("### Generated Workflow Steps")
            for step in workflow:
                st.write(f"**Step:** {step['step']}")
                st.write(f"**Description:** {step['description']}")
                st.write(f"**Next Steps:** {', '.join(step['next_steps']) if step['next_steps'] else 'End'}")
                st.write("---")
        
        # Visualize the workflow graph if toggled
        if display_graph:
            st.write("### Workflow Graph")
            html_file = visualize_workflow_with_pyvis(workflow)
            with open(html_file, "r", encoding="utf-8") as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=500)
        
        # Download options
        st.write("### Download Workflow")
        
        # Download as JSON
        workflow_json = json.dumps(workflow, indent=4)
        st.markdown(get_download_link(workflow_json, "workflow", "json"), unsafe_allow_html=True)
        
        # Download as Text
        workflow_text = "\n".join([f"Step: {step['step']}\nDescription: {step['description']}\nNext Steps: {', '.join(step['next_steps']) if step['next_steps'] else 'End'}\n" for step in workflow])
        st.markdown(get_download_link(workflow_text, "workflow", "txt"), unsafe_allow_html=True)
    else:
        st.error("Please enter some requirements to generate a workflow.")