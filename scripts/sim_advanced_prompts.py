import os
import google.generativeai as genai
from datetime import datetime

def simulate_variants(topic):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        # Try to extract from the log file as backup
        try:
            with open("/home/petit/Escritorio/Sovereign_Content_Engine.txt", "r") as f:
                content = f.read()
                import re
                match = re.search(r'GOOGLE_API_KEY=([^"\n\s]+)', content)
                if match:
                    api_key = match.group(1)
        except Exception:
            pass

    if not api_key:
        return "Error: GOOGLE_API_KEY not found."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemma-4-31b-it')

    variants = {
        "V1_Surgical": """
            Act as a Senior Systems Architect. Write a highly professional, surgical technical guide in SPANISH.
            Topic: {topic}

            REQUIREMENTS:
            - 100% SPANISH.
            - TONE: Direct, authoritative, no fluff.
            - STRUCTURE:
                1. Technical Summary (max 3 sentences).
                2. Hardware/Kernel analysis.
                3. Execution Protocol (numbered, precise commands).
                4. Verification steps.
                5. Sovereignty verdict.
            Format as Jekyll post with frontmatter.
            """,
        "V2_Philosophical": """
            Act as the lead engineer of the Digital Resistance. Write a technical guide in SPANISH that empowers the user against planned obsolescence.
            Topic: {topic}

            REQUIREMENTS:
            - 100% SPANISH.
            - TONE: Professional but subversive, inspiring technological sovereignty.
            - STRUCTURE:
                1. The Problem (Obsolescence).
                2. Technical Solution (Hardware/Software deep-dive).
                3. Step-by-Step liberation protocol.
                4. Philosophical impact on sovereignty.
            Format as Jekyll post with frontmatter.
            """,
        "V3_Command_Centric": """
            Act as a Hardware Hacker and Linux Specialist. Write a technical guide in SPANISH focused on maximum efficiency and command-line precision.
            Topic: {topic}

            REQUIREMENTS:
            - 100% SPANISH.
            - TONE: Practical, technical, focused on performance.
            - STRUCTURE:
                1. Performance Goal.
                2. Prerequisites.
                3. Command-line sequence (heavy use of code blocks).
                4. Optimization tips.
                5. Sovereignty verdict.
            Format as Jekyll post with frontmatter.
            """
    }

    results = {}
    for name, prompt in variants.items():
        print(f"Generating {name}...")
        response = model.generate_content(prompt.format(topic=topic))
        results[name] = response.text

    return results

if __name__ == "__main__":
    test_topic = "Optimización de Memoria Swap y ZRAM en Hardware Antiguo"
    outputs = simulate_variants(test_topic)

    if isinstance(outputs, str):
        print(outputs)
    else:
        for name, content in outputs.items():
            with open(f"sim_prompt_{name}.md", "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Saved {name} to sim_prompt_{name}.md")
