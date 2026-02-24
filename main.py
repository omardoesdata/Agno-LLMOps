from agno.agent import Agent
from agno.models.ollama import Ollama

model = Ollama(
    id="llama3:8b",
    host="http://127.0.0.1:11434"
)

agent = Agent(
    model=model,
    instructions="You are a helpful AI tutor who explains concepts very clearly and simply."
)

response = agent.run("Explain overfitting in machine learning in very simple words.")
print(response.content)