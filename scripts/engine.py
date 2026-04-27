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
    model = genai.GenerativeModel('gemini-1.5-flash')

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
        Act as an expert systems engineer specializing in legacy hardware.
        Write a professional, high-performance technical guide in SPANISH.
        Topic: {topic}

        The guide must be:
        1. Written entirely in SPANISH.
        2. Technical, authoritative, and professional.
        3. Structured with clear headings, a step-by-step guide, and a final conclusion.
        4. Focused on 'Soberanía Tecnológica' and high efficiency.

        Format the output as a Jekyll post with frontmatter:
        ---
        layout: default
        title: '{topic}'
        date: {date}
        image: '{img_url}'
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
