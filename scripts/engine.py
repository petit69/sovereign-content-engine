import os
import google.generativeai as genai
from datetime import datetime

def generate_guide():
    # Setup API Key from Environment
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        return

    genai.configure(api_key=api_key)

    # Change to a more generic and stable model name to avoid 404
    # We try gemini-1.5-flash-latest or gemini-pro
    model_name = 'gemini-1.5-flash'
    try:
        model = genai.GenerativeModel(model_name)
        # Test call to verify model exists
        model.generate_content("Test")
    except Exception:
        print(f"Trying fallback model...")
        model = genai.GenerativeModel('gemini-pro')

    # Topics for guides
    topics = [
        "Optimización de Linux Mint para CPUs antiguas",
        "Uso de SSDs en laptops obsoletas para mejorar el rendimiento",
        "Configuración de swap y zram para sistemas con poca RAM",
        "Soberanía tecnológica: Cómo evitar el bloqueo de hardware programado"
    ]

    os.makedirs("_posts", exist_ok=True)

    for topic in topics:
        date = datetime.now().strftime("%Y-%m-%d")
        clean_title = topic.lower().replace(" ", "_").replace("ó", "o").replace("í", "i").replace("á", "a").replace("é", "e").replace("ú", "u").replace("ñ", "n").replace(":", "").replace(",", "")

        print(f"Generando guía sobre: {topic}...")

        prompt = f"""
        Act as an expert systems engineer specializing in legacy hardware.
        Write a professional, high-performance technical guide in SPANISH.
        Topic: {topic}

        The guide must be:
        1. Written entirely in SPANISH.
        2. Technical, authoritative, and professional.
        3. Focused on 'Soberanía Tecnológica' and high efficiency.
        3. Structured with clear headings, a step-by-step guide, and a final conclusion.

        Format the output as a Jekyll post with frontmatter:
        ---
        layout: post
        title: '{topic}'
        date: {date}
        ---

        (The content must be in Spanish)
        """

        try:
            response = model.generate_content(prompt)
            content = response.text

            filename = f"{date}-{clean_title}.md"
            with open(f"_posts/{filename}", "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Guía guardada exitosamente en _posts: {filename}")
        except Exception as e:
            print(f"Error generating guide for {topic}: {e}")

if __name__ == "__main__":
    generate_guide()
