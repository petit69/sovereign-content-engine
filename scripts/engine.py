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

    # Using the latest stable model to avoid 404 errors
    model = genai.GenerativeModel('gemma-4-31b-it')

    # Technical image library for the robot
    image_library = {
        "cpu": "https://images.unsplash.com/photo-1591799264318-7e6ef8B7f73c?auto=format&fit=crop&w=600&q=80",
        "ram": "https://images.unsplash.com/photo-1518770660439-4636efebcaef?auto=format&fit=crop&w=600&q=80",
        "ssd": "https://images.unsplash.com/photo-1597733336794-775d63963840?auto=format&fit=crop&w=600&q=80",
        "general": "https://images.unsplash.com/photo-1550751827-4c39ad817773?auto=format&fit=crop&w=600&q=80"
    }

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

        # Assign image based on keyword
        img_url = image_library["general"]
        if "cpu" in topic.lower(): img_url = image_library["cpu"]
        elif "ssd" in topic.lower(): img_url = image_library["ssd"]
        elif "ram" in topic.lower() or "swap" in topic.lower(): img_url = image_library["ram"]

        prompt = f"""
        Act as the lead engineer of the Digital Resistance. Write a technical guide in SPANISH that empowers the user against planned obsolescence.
        Topic: {topic}

        REQUIREMENTS:
        1. LANGUAGE: 100% SPANISH.
        2. TONE: Professional but subversive, inspiring technological sovereignty.
        3. STRUCTURE:
           - # [Title]
           - ## ✊ El Problema: la Obsolescencia Programada (Explain why this topic matters for sovereignty).
           - ## 🛠️ La Solución Técnica: (Deep-dive into hardware/software technicals).
           - ## 🚀 Protocolo de Liberación (Detailed, numbered steps with code blocks).
           - ## ⚖️ Impacto en la Soberanía Tecnológica (Philosophical and practical conclusion).
        4. FORMATTING: Use bold text for key terms and tables for comparisons where applicable.

        Format the output as a Jekyll post with frontmatter:
        ---
        layout: default
        title: '{topic}'
        date: {date}
        image: '{img_url}'
        ---
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
