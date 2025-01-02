import os
import subprocess
import requests

# GitHub repository details
REPO_URL = "https://github.com/Zhao-Tianyu-S/Necluei-Swarm-Node"
CLONE_DIR = "./necluei_swarm_node"

# Agent metadata
AGENT_NAME = "Swarm Agent"
AGENT_DESCRIPTION = "An autonomous agent powered by the Necluei Swarm Node repository."

# Function to clone the repository
def clone_repository():
    if os.path.exists(CLONE_DIR):
        print(f"Repository already exists at {CLONE_DIR}. Pulling latest changes...")
        subprocess.run(["git", "pull"], cwd=CLONE_DIR, check=True)
    else:
        print(f"Cloning repository from {REPO_URL}...")
        subprocess.run(["git", "clone", REPO_URL, CLONE_DIR], check=True)

# Function to set up the agent environment
def setup_environment():
    print("Setting up the environment...")
    requirements_path = os.path.join(CLONE_DIR, "requirements.txt")
    if os.path.exists(requirements_path):
        subprocess.run(["pip", "install", "-r", requirements_path], check=True)
    else:
        print("No requirements.txt file found in the repository.")

# Function to configure the agent
def configure_agent():
    config_file = os.path.join(CLONE_DIR, "config.json")
    config_data = {
        "name": AGENT_NAME,
        "description": AGENT_DESCRIPTION,
        "settings": {
            "autonomy_level": "high",
            "node_communication": "enabled",
            "learning_rate": 0.05
        }
    }
    with open(config_file, "w") as f:
        json.dump(config_data, f, indent=4)
    print(f"Agent configuration saved to {config_file}.")

# Function to launch the agent
def launch_agent():
    print("Launching the Swarm Agent...")
    agent_script = os.path.join(CLONE_DIR, "agent.py")
    if os.path.exists(agent_script):
        subprocess.run(["python", agent_script], check=True)
    else:
        print("Agent script not found in the repository.")

# Main function
def main():
    clone_repository()
    setup_environment()
    configure_agent()
    launch_agent()

if __name__ == "__main__":
    main()
