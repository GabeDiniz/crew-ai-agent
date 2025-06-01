# CrewAiAgent Crew

CrewAI Agent

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

On Windows: install uv tool and crewai
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
```bash
uv tool install crewai
```

Install crewai dependencies
```bash
crewai install
```
## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the crew-ai-agent Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/crew_ai_agent/config/agents.yaml` to define your agents
- Modify `src/crew_ai_agent/config/tasks.yaml` to define your tasks
- Modify `src/crew_ai_agent/crew.py` to add your own logic, tools and specific args
- Modify `src/crew_ai_agent/main.py` to add custom inputs for your agents and tasks

## Understanding Your Crew

The crew-ai-agent Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the CrewAiAgent Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
