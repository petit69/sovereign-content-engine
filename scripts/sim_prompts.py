import os
import google.generativeai as genai
from datetime import datetime

def simulate_prompt(prompt_version, topic):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: GOOGLE_API_KEY not found."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    print(f"\n--- Testing Prompt Version: {prompt_version} ---")
    response = model.generate_content(prompt_version.format(topic=topic, date=datetime.now().strftime("%Y-%m-%d")))
    return response.text

# Versions to test
prompts = {
    "Basic": """
        Act as an expert systems engineer specializing in legacy hardware.
        Write a professional, high-performance technical guide in SPANISH.
        Topic: {topic}
        The guide must be:
        1. Written entirely in SPANISH.
        2. Technical, authoritative, and professional.
        3. Structured with clear headings, a step-by-step guide, and a final conclusion.
        4. Focused on 'Soberanía Tecnológica' and high efficiency.
        Format as Jekyll post.
        """,
    "Advanced_Technical": """
        Act as a Senior Systems Architect and Hardware Hacker. Your goal is to empower the user to reclaim their technology from planned obsolescence.
        Write a deep-dive technical masterclass in SPANISH.
        Topic: {topic}

        REQUIREMENTS:
        1. TONE: Authoritative, cyber-technical, professional, and slightly subversive (anti-obsolescence).
        2. LANGUAGE: 100% SPANISH.
        3. STRUCTURE:
           - # [Title]
           - ## 🛠️ Análisis Técnico: Explain WHY this happens at a hardware/kernel level.
           - ## 🚀 Protocolo de Implementación: Detailed, numbered steps. Use code blocks for commands.
           - ## ⚠️ Consideraciones de Riesgo: What could go wrong and how to fix it.
           - ## ⚖️ Veredicto de Soberanía: How this action breaks the cycle of planned obsolescence.
           - ## 🏁 Conclusión.
        4. FORMATTING: Use bold text for key terms, tables for comparisons, and clear Markdown hierarchies.

        Format the output as a Jekyll post with frontmatter:
        ---
        layout: default
        title: '{topic}'
        date: {date}
        ---
        """,
    "Ultra_Premium": """
        You are the lead engineer of the 'Sovereign Content Engine'. You produce the gold standard of technical documentation for the digital resistance.
        Topic: {topic}

        Create a high-end technical guide in SPANISH that looks like a premium industrial manual.

        STRUCTURE:
        1. Executive Summary: A high-level technical overview.
        2. Hardware Deep-Dive: Detailed explanation of the components involved.
        3. Step-by-Step Execution: Precise, surgical instructions.
        4. Performance Metrics: What improvements to expect (theoretical/practical).
        5. Philosophical Angle: The impact on Technological Sovereignty.

        STYLE:
        - Use professional, precise terminology (e.g., 'latencia', 'rendimiento sostenido', 'kernel panic').
        - Avoid fluff. Be direct and surgical.
        - Use a layout that emphasizes efficiency and power.

        Language: SPANISH.
        Format: Jekyll post with frontmatter.
        ---
        layout: default
        title: '{topic}'
        date: {date}
        ---
        """
}

if __name__ == "__main__":
    test_topic = "Optimización de Linux Mint para CPUs antiguas"
    for name, prompt in prompts.items():
        result = simulate_prompt(prompt, test_topic)
        with open(f"sim_{name}.md", "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Simulation {name} saved to sim_{name}.md")
