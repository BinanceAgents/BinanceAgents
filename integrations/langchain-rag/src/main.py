from uagents import Bureau
from agents.langchain_rag_agent import agent
from agents.langchain_rag_user import user


if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)
    print(f"Adding RAG agent to Bureau: {agent.address}")
    bureau.add(agent)
    print(f"Adding user agent to Bureau: {user.address}")
    bureau.add(user)
    bureau.run()

# Updated: 2025-10-08T19:59:32.063457

# Updated: 2025-10-08T20:10:20.911269
