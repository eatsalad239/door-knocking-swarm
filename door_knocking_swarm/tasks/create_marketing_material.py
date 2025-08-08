"""Definition of the marketing materials task.

This task instructs the Marketing Agent to produce a package of marketing
collateral for a specific client and product.  The output is a dictionary
containing copy that can be reused in other tasks such as website building.
"""

from __future__ import annotations

from crewai import Task
from crewai import Agent


def create_marketing_task(agent: Agent, client_name: str, product: str) -> Task:
    """Return a task that asks the Marketing Agent to generate copy.

    Parameters
    ----------
    agent : Agent
        The marketing agent created via `create_marketing_agent()`.
    client_name : str
        The name of the client/business the materials are for.
    product : str
        The product or service being sold door‑to‑door.

    Returns
    -------
    Task
        A CrewAI task configured with a description and expected output.
    """
    description = (
        f"You are tasked with crafting marketing materials for a door‑to‑door "
        f"sales campaign.  The client is '{client_name}', and the product or "
        f"service being sold is '{product}'.  Produce a dictionary with the "
        "following keys:\n"
        "- title: a short, punchy headline for the campaign\n"
        "- tagline: a one‑sentence tagline that hooks customers at the door\n"
        "- description: a paragraph describing the product and its benefits\n"
        "- benefits: a list of 3–5 bullet points highlighting key advantages\n"
        "- flyer_text: a persuasive script suitable for printing on a flyer or door hanger\n"
        "- email_script: a short email template reps can send to warm leads\n"
        "Use clear, friendly language that resonates with household decision makers."
    )
    expected_output = (
        "A Python dictionary with the keys 'title', 'tagline', 'description', "
        "'benefits', 'flyer_text' and 'email_script'.  The 'benefits' value must "
        "be a list of strings."
    )
    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
    )
