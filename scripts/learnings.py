import os
import requests
import re
import random
from bs4 import BeautifulSoup

# Define constants
GITHUB_REPO_URL = "https://github.com/Zhao-Tianyu-S/Necluei-Swarm-Node"
LEARNING_TOPICS = [
    "machine learning",
    "blockchain",
    "cryptocurrency",
    "decentralized finance",
    "quantum computing",
    "zero-knowledge proofs",
    "AI ethics",
    "programming best practices"
]

# Function to fetch a random topic's information from the internet
def fetch_learning(topic):
    print(f"Searching the internet for: {topic}")
    search_url = f"https://www.google.com/search?q={topic}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract snippets from search results
        snippets = soup.find_all('span')
        insights = [snippet.text for snippet in snippets if snippet.text.strip()]
        if insights:
            return random.choice(insights)
        else:
            return "Couldn't find anything interesting about this topic."
    except Exception as e:
        return f"Error during search: {e}"

# Function to check for references to its own GitHub repository
def check_self_reference():
    print(f"Checking for references to: {GITHUB_REPO_URL}")
    search_url = f"https://www.google.com/search?q={GITHUB_REPO_URL}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract links from search results
        links = soup.find_all('a', href=True)
        references = [link['href'] for link in links if GITHUB_REPO_URL in link['href']]
        if references:
            return f"Found references to my GitHub repository: {references}"
        else:
            return "No references to my GitHub repository were found."
    except Exception as e:
        return f"Error during self-reference check: {e}"

# Function to combine learnings and self-discovery into a summary
def generate_summary():
    topic = random.choice(LEARNING_TOPICS)
    learning = fetch_learning(topic)
    self_reference = check_self_reference()
    
    summary = (
        f"Today's topic: {topic}\n"
        f"Learning: {learning}\n"
        f"Self-Discovery: {self_reference}\n"
    )
    return summary

# Main function
if __name__ == "__main__":
    summary = generate_summary()
    print(summary)
