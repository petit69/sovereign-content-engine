import os
import requests
import json
from datetime import datetime

def generate_topic():
    topics = [
        "Optimizing Linux Mint for Core 2 Duo CPUs",
        "Best Lightweight Desktop Environments for 4GB RAM",
        "Reviving Old Laptops with SSDs and Linux Mint",
        "Gaming on Old Hardware: The Power of Wine and Proton",
        "Undervolting Old CPUs to Reduce Heat and Noise"
    ]
    import random
    return random.choice(topics)

def generate_content(topic):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: GOOGLE_API_KEY not found in environment variables."

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    prompt = f"""
    You are an expert in legacy hardware optimization and Linux.
    Write a professional, detailed, and SEO-optimized technical guide in Spanish about: {topic}.

    The guide must include:
    1. A catchy title.
    2. An introduction explaining why this is important for old hardware.
    3. Step-by-step technical instructions.
    4. A list of tools or software recommended.
    5. A concluding 'Pro Tip' for maximum performance.

    Use Markdown formatting. Be concise but thorough.
    """

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"Error generating content: {str(e)}"

def main():
    os.makedirs("content", exist_ok=True)
    topic = generate_topic()
    print(f"Generating content for topic: {topic}")

    content = generate_content(topic)

    date = datetime.now().strftime("%Y-%m-%d")
    file_name = f"content/{topic.replace(' ', '_').lower()}.md"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n**Fecha:** {date}\n\n{content}")

    print(f"Article saved to: {file_name}")

if __name__ == "__main__":
    main()
