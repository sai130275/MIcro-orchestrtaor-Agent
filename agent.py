import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools.tool_context import ToolContext

# --- Setup ---
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()
model_name = os.getenv("MODEL")

# --- Tool ---
def add_tasks_to_state(tool_context: ToolContext, tasks: str) -> dict:
    tool_context.state["TASKS"] = tasks
    logging.info(f"[State] TASKS: {tasks}")
    return {"status": "stored"}

# --- Agents ---

task_structurer = Agent(
    name="task_structurer",
    model=model_name,
    description="Structures tasks into groups.",
    instruction="""
    Analyze TASKS:
    - Group related tasks
    - Identify dependencies
    - Remove redundancy

    TASKS:
    { TASKS }
    """,
    output_key="structured_tasks"
)

task_optimizer = Agent(
    name="task_optimizer",
    model=model_name,
    description="Optimizes execution order.",
    instruction="""
    Optimize STRUCTURED_TASKS:
    - Create phases
    - Prioritize tasks
    - Improve efficiency

    STRUCTURED_TASKS:
    { structured_tasks }
    """,
    output_key="execution_plan"
)

formatter = Agent(
    name="formatter",
    model=model_name,
    description="Formats execution plan.",
    instruction="""
    Present EXECUTION_PLAN as:
    - Phases
    - Ordered steps
    - Clear structure

    EXECUTION_PLAN:
    { execution_plan }
    """
)

workflow = SequentialAgent(
    name="microtask_orchestrator_workflow",
    sub_agents=[task_structurer, task_optimizer, formatter]
)

root_agent = Agent(
    name="microtask_orchestrator_entry",
    model=model_name,
    instruction="""
    - Ask user for tasks or goal
    - Store input
    - Pass to workflow
    """,
    tools=[add_tasks_to_state],
    sub_agents=[workflow]
)
