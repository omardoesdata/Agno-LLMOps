from agno.agent import Agent
from agno.models.ollama import Ollama

# Connect to your local Llama3 model
model = Ollama(
    id="llama3:8b",
    host="http://127.0.0.1:11434"
)

# Create agent with memory
agent = Agent(
    model=model,
    instructions="You are a helpful AI tutor who explains concepts clearly. Remember the conversation context."
)

print("Agno Chatbot (type 'exit' to quit)")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chatbot...")
        break

    # Run the agent
    response = agent.run(user_input)

    # Print only the AI text
    print(f"AI: {response.content.strip()}")