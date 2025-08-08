"""Entry point for running the door‑knocking agent swarm.

This script parses command line arguments, instantiates the agents and tasks and
orchestrates them with CrewAI.  To run the default workflow, set your
`OPENAI_API_KEY` environment variable and execute:

```
python main.py --client_name "Acme Solar" --product "solar panels"
```
"""

from __future__ import annotations

import argparse
import os
import json

from crewai import Crew

from agents import (
    create_marketing_agent,
    create_training_agent,
    create_web_agent,
)
from tasks import (
    create_marketing_task,
    create_training_task,
    create_web_task,
)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments for the crew run.

    Returns
    -------
    argparse.Namespace
        The parsed arguments with `client_name` and `product` attributes.
    """
    parser = argparse.ArgumentParser(description="Run the door‑knocking agent swarm")
    parser.add_argument(
        "--client_name",
        type=str,
        required=True,
        help="Name of the business or client for whom materials are generated",
    )
    parser.add_argument(
        "--product",
        type=str,
        required=True,
        help="Product or service being sold door‑to‑door",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    client_name = args.client_name
    product = args.product

    # Ensure an OpenAI API key is configured; CrewAI relies on it.
    if os.getenv("OPENAI_API_KEY") is None:
        raise RuntimeError(
            "Please set the OPENAI_API_KEY environment variable before running this script."
        )

    # Instantiate agents
    marketing_agent = create_marketing_agent()
    training_agent = create_training_agent()
    web_agent = create_web_agent()

    # Create tasks bound to the agents
    marketing_task = create_marketing_task(marketing_agent, client_name, product)
    training_task = create_training_task(training_agent, client_name, product)
    web_task = create_web_task(web_agent, client_name)

    # Assemble the crew
    crew = Crew(
        agents=[marketing_agent, training_agent, web_agent],
        tasks=[marketing_task, training_task, web_task],
    )

    # Kick off the workflow.  The first task produces marketing_copy which the
    # web task can consume.  CrewAI automatically passes outputs between tasks
    # when you name variables consistently in the descriptions.
    print(f"Starting crew for client: {client_name}\n")
    result = crew.kickoff(
        inputs={
            "client_name": client_name,
            "product": product,
        }
    )

    # The result is a list of task outputs.  We can save them to disk for later use.
    out_dir = f"output_{client_name.replace(' ', '_').lower()}"
    os.makedirs(out_dir, exist_ok=True)
    for i, task_output in enumerate(result):
        filename = os.path.join(out_dir, f"task_{i+1}.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(task_output, f, indent=2)
        print(f"Saved task {i+1} output to {filename}")


if __name__ == "__main__":
    main()
