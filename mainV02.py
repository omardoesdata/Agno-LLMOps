from agno.agent import Agent
from agno.models.ollama import Ollama

# -----------------------------
# Configuration
# -----------------------------
STREAM = True  # True = token by token, False = full response

# Connect to Llama3
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

    if STREAM:
        # Stream events, only print the content field
        for event in agent.run(user_input, stream=True):
            if hasattr(event, "content") and event.content:
                print(event.content, end="", flush=True)
        print()  # Newline after the AI response
    else:
        # Non-streaming: clean content
        response = agent.run(user_input)
        print(f"AI: {response.content.strip()}")