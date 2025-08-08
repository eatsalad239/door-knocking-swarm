"""Definition of the training materials task.

This task asks the Training Agent to prepare onboarding and practice content
for door‑knocking sales representatives.  The resulting materials can be
assembled into slides, handbooks or workshops.
"""

from __future__ import annotations

from crewai import Task
from crewai import Agent


def create_training_task(agent: Agent, client_name: str, product: str) -> Task:
    """Return a task that instructs the Training Agent to generate content.

    Parameters
    ----------
    agent : Agent
        The training agent created via `create_training_agent()`.
    client_name : str
        Name of the company receiving the training materials.
    product : str
        The product or service to be sold door‑to‑door.

    Returns
    -------
    Task
        A CrewAI task for generating training materials.
    """
    description = (
        f"Develop a comprehensive training module for new door‑knocking sales reps of "
        f"'{client_name}'.  The reps will be selling '{product}'.  The module "
        "should include:\n"
        "- an overview of the product and why it solves the customer's problem\n"
        "- a step‑by‑step script for approaching a house, introducing yourself and "
        "  presenting the offer\n"
        "- a list of common objections and effective rebuttals\n"
        "- a role‑play exercise that mentors can use to practice with trainees\n"
        "Write in an encouraging tone and emphasise listening to customer needs."
    )
    expected_output = (
        "A structured training guide covering product overview, approach script, "
        "objections and rebuttals, and a role‑play dialogue.  Format the output as "
        "Markdown with clear headings."
    )
    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
    )
