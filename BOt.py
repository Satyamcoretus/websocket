from agent import Agent

# Agent instances
agent1 = Agent('ajay',True)
agent2 = Agent('mukesh',False)
agent3  = Agent('Harra',True)



class Chatbot:
    def __init__(self):
        self.all_agents = [agent1,agent2,agent3]  # Example agents

    def contact_agent(self):
        available_agent = None
        for agent in self.all_agents:
            if agent.available:
                available_agent = agent
                break

        if available_agent:
            available_agent.available = False
            return f"Connected with {available_agent.name}."
        else:
            return "All agents are currently busy. Please wait."

    def agent_becomes_available(self, agent_name):
        for agent in self.agents:
            if agent.name == agent_name:
                agent.available = True
                break