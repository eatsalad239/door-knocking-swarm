"""Expose factory functions for the agents.

Each specialised agent is defined in its own module.  The functions return
instances of `crewai.Agent` configured with role, goal and backstory.
"""

from .marketing_agent import create_marketing_agent  # noqa: F401
from .training_agent import create_training_agent    # noqa: F401
from .web_agent import create_web_agent              # noqa: F401

__all__ = [
    "create_marketing_agent",
    "create_training_agent",
    "create_web_agent",
]
