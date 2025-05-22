#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from crew_ai_agent.crew import CrewAiAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # Job Post Summarizer Agent
    run_job_post_summarizer()

    # inputs = {
    #     'topic': 'AI LLMs',
    #     'current_year': str(datetime.now().year)
    # }
    # try:
    #     CrewAiAgent().crew().kickoff(inputs=inputs)
    # except Exception as e:
    #     raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        CrewAiAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewAiAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        CrewAiAgent().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_job_post_summarizer():
    """
    Run the JobPostSummarizerAgent to extract skills from a job post.
    """
    job_posting = """
    Nexxa.AI specializes in automating industrial operations through advanced Agentic AI solutions. Our mission is to revolutionize heavy industries by providing cognitive, resilient, and end-to-end automation that seamlessly integrates with existing technologies. By addressing challenges such as legacy system dependencies, workforce transitions, and rising operational costs, we empower businesses to achieve immediate efficiency and profitability.

    Do you enjoy building with novel technologies and are curious about AI agents? As a Forward Deployed Engineer, you will help build and drive the development of Nexxa.AI’s automation platform. You’ll work closely with the founding team to design, prototype, and deploy AI-driven solutions that integrate seamlessly with enterprise operations. This role is for a hands-on engineer who thrives in early-stage, fast-paced environments, enjoys tackling complex challenges, and has a passion for AI-powered automation.  Your expertise will be crucial in building systems that automate complex industrial processes, ensuring seamless integration with clients' existing infrastructures.
    """

    inputs = {
        "input": job_posting
    }

    try:
        CrewAiAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"Error during JobPostSummarizerAgent run: {e}")
