"""Definition of the website building task.

This task instructs the Web Agent to use its `build_website` tool to create
# a single‑page website for the client.  It expects to receive a dictionary
# called `marketing_copy` in the crew's inputs, produced by the marketing task.
"""

from __future__ import annotations

from crewai import Task
from crewai import Agent


def create_web_task(agent: Agent, client_name: str) -> Task:
    """Return a task that asks the Web Agent to generate a website.

    Parameters
    ----------
    agent : Agent
        The web agent created via `create_web_agent()`.
    client_name : str
        Name of the business the site is for.

    Returns
    -------
    Task
        A CrewAI task configured to call the agent's website builder tool.
    """
    description = (
        f"Use your website building skills to assemble a simple landing page for "
        f"'{client_name}'.  A dictionary named `marketing_copy` is available in the "
        "context; it contains keys 'title', 'tagline', 'description' and "
        "'benefits'.  Call your `build_website(client_name, marketing_copy)` tool "
        "with these values and return the resulting HTML.  Do not attempt to write "
        "the HTML yourself—always use the tool."
    )
    expected_output = (
        "A string containing valid HTML for the landing page, returned by the "
        "`build_website` tool."
    )
    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
    )
