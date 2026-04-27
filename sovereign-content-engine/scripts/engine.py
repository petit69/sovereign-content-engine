import os
import requests
from datetime import datetime

def generate_topic():
    # Simulation of AI topic selection based on the "Ancient Hardware" niche
    topics = [
        "Optimizing Linux Mint for Core 2 Duo CPUs",
        "Best Lightweight Desktop Environments for 4GB RAM",
        "Reviving Old Laptops with SSDs and Linux Mint",
        "Gaming on Old Hardware: The Power of Wine and Proton",
        "Undervolting Old CPUs to Reduce Heat and Noise"
    ]
    import random
    return random.choice(topics)

def create_article():
    topic = generate_topic()
    date = datetime.now().strftime("%Y-%m-%d")
    content = f"# {topic}\n\nGenerated on {date}\n\nThis is a placeholder for the AI-generated technical guide on {topic}. The actual LLM integration will happen via the GitHub Action secret."

    file_name = f"content/{topic.replace(' ', '_').lower()}.md"
    with open(file_name, "w") as f:
        f.write(content)

    return topic, file_name

if __name__ == "__main__":
    os.makedirs("content", exist_ok=True)
    topic, path = create_article()
    print(f"Topic created: {topic}")
    print(f"File saved to: {path}")
