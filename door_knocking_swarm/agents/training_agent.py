"""Factory for the Training Agent.

This agent is responsible for creating training content for door‑knocking
salespeople, such as scripts, objection handling guides and role‑play
exercises.  It is configured with a specific role, goal and backstory so the
LLM behind it knows how to behave.
"""

from __future__ import annotations

from crewai import Agent


def create_training_agent() -> Agent:
    """Create a training agent for sales onboarding and education.

    Returns
    -------
    Agent
        A `crewai.Agent` that can generate training materials for a given
        product or service, focusing on door‑to‑door sales techniques.
    """
    return Agent(
        role="Training Agent",
        goal=(
            "Develop comprehensive training materials for door‑to‑door sales reps, "
            "including role‑play dialogues, objection‑handling scripts, FAQs and "
            "checklists tailored to the client’s product or service."
        ),
        backstory=(
            "You are an expert sales trainer who has coached hundreds of reps on "
            "how to successfully sell products face‑to‑face at the doorstep. "
            "You know how to break complex concepts into easy steps and create "
            "engaging exercises that build confidence."
        ),
    )
