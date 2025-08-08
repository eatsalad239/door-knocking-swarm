"""Expose factory functions for tasks.

Tasks encapsulate descriptions of the work to be performed by agents.  Each
factory returns a configured `crewai.Task` ready to be assembled into a crew.
"""

from .create_marketing_material import create_marketing_task  # noqa: F401
from .training_material import create_training_task          # noqa: F401
from .build_website import create_web_task                  # noqa: F401

__all__ = [
    "create_marketing_task",
    "create_training_task",
    "create_web_task",
]
