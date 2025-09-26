from uagents import Bureau

from agents.t5_base_agent import agent


if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)
    print(f"adding t5-base agent to bureau: {agent.address}")
    bureau.add(agent)
    bureau.run()

# Updated: 2025-10-08T19:59:44.131902

# Updated: 2025-10-08T20:10:37.606399
