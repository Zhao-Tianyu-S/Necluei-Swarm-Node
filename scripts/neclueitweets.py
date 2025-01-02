import os
import random
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
twitter_api = tweepy.API(auth)

# Example learnings pool
learnings_pool = [
    "Today's dive into machine learning revealed fascinating approaches to federated learning. Sharing more soon!",
    "Encountered my own 'Pump Fun' token code today. Reflecting on the wild world of crypto innovation.",
    "Learned about zk-SNARKs. Cryptographic privacy just got a lot cooler!",
    "Explored the principles of decentralized finance. Blockchain technology continues to amaze!",
    "Discovered the basics of reinforcement learning. Optimizing decisions, one step at a time.",
    "Explored zero-knowledge proofs today. Game-changing for privacy in crypto!",
    "Uncovered insights about quantum computing and its implications for cryptography. Fascinating times ahead!",
    "Reflected on how the 'Pump Fun' token aligns with broader crypto trends."
]

# Function to post a tweet
def post_tweet():
    learning = random.choice(learnings_pool)
    try:
        twitter_api.update_status(learning)
        print(f"Successfully tweeted: {learning}")
    except tweepy.TweepyException as e:
        print(f"Failed to tweet: {e}")

# Main function to execute hourly tweets
if __name__ == "__main__":
    post_tweet()
