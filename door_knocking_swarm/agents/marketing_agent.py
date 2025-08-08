"""Factory for the Marketing Agent.

The Marketing Agent specialises in generating door‑knocking marketing collateral
such as flyers, scripts and email copy.  It uses CrewAI’s `Agent` class to
package the role, goal and backstory for the LLM.
"""

from __future__ import annotations

from crewai import Agent


def create_marketing_agent() -> Agent:
    """Create a marketing agent configured for door‑knocking copy.

    Returns
    -------
    Agent
        A `crewai.Agent` instance with a role, goal and backstory.  The agent
        will use whichever LLM you select when instantiating the Crew in
        `main.py`.
    """
    return Agent(
        role="Marketing Agent",
        goal=(
            "Generate concise, persuasive marketing materials for door‑to‑door "
            "sales campaigns, including flyers, door hangers, email templates and "
            "talking points tailored to a given product or service."
        ),
        backstory=(
            "You are a seasoned direct‑marketing copywriter with years of "
            "experience crafting messages that grab attention at the doorstep. "
            "You understand the needs of small businesses and can adapt tone and "
            "style to suit different audiences."
        ),
    )
