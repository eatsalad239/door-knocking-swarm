"""Factory for the Web Agent and website builder.

The Web Agent generates a simple responsive website for a client using a
templating engine.  It exposes a tool function `build_website` that can be
called by other agents to assemble a ready‑to‑deploy HTML file.  The agent
definition registers this tool so CrewAI knows it can be invoked when needed.
"""

from __future__ import annotations

from typing import Dict

from crewai import Agent
from jinja2 import Template


# Basic single‑page website template using Bootstrap 5.
_BASE_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ client_name }} – Door‑Knocking Campaign</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">{{ client_name }}</a>
      </div>
    </nav>
    <header class="bg-primary text-white py-5">
      <div class="container">
        <h1 class="display-4">{{ marketing_copy.title }}</h1>
        <p class="lead">{{ marketing_copy.tagline }}</p>
      </div>
    </header>
    <main class="container my-5">
      <h2>About the Offer</h2>
      <p>{{ marketing_copy.description }}</p>
      <h2>Why Choose Us</h2>
      <ul>
        {% for benefit in marketing_copy.benefits %}
        <li>{{ benefit }}</li>
        {% endfor %}
      </ul>
    </main>
    <footer class="bg-light py-4 mt-auto border-top">
      <div class="container text-center">
        <span class="text-muted">&copy; {{ client_name }} {{ year }}. All rights reserved.</span>
      </div>
    </footer>
  </body>
</html>
"""



def build_website(client_name: str, marketing_copy: Dict[str, object], year: int | None = None) -> str:
    """Render a simple website for the client.

    Parameters
    ----------
    client_name : str
        The name of the business or client.
    marketing_copy : dict
        A dictionary containing at least `title`, `tagline`, `description` and
        `benefits` (list of strings).  The Marketing Agent is responsible for
        generating these fields.
    year : int, optional
        Year to display in the footer.  Defaults to the current year.

    Returns
    -------
    str
        A string containing the HTML for the website.
    """
    import datetime

    if year is None:
        year = datetime.datetime.now().year

    template = Template(_BASE_TEMPLATE)
    html = template.render(client_name=client_name, marketing_copy=marketing_copy, year=year)
    return html


def create_web_agent() -> Agent:
    """Create a web agent configured to build websites.

    Returns
    -------
    Agent
        A `crewai.Agent` that exposes the `build_website` tool.  The agent
        instructs the LLM to delegate website generation tasks to this tool
        rather than attempting to write HTML itself.
    """
    return Agent(
        role="Web Developer Agent",
        goal=(
            "Design and assemble simple, responsive websites for door‑knocking "
            "clients using predefined templates.  Integrate marketing copy and "
            "highlight key benefits to maximise conversions."
        ),
        backstory=(
            "You are a full‑stack web developer who specialises in small business "
            "landing pages.  You value clear information architecture, mobile "
            "responsiveness and minimal design."
        ),
        tools=[build_website],
    )
