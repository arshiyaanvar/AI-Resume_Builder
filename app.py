from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_bullets(role, level):
    prompt = f"""
    Generate exactly 5 professional resume bullet points for a {level} {role}.

    Rules:
    - Output ONLY bullet points
    - No introduction or explanation
    - Each point must start with an action verb
    - Keep each point concise (one line)
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("=== AI Resume Builder ===\n")

    role = input("Enter job role: ")
    level = input("Enter experience level (Fresher/Experienced): ")

    result = generate_bullets(role, level)

    print("\n✨ Generated Resume Points:\n")

    for line in result.split("\n"):
        if line.strip():
            # Remove numbering if present and format nicely
            clean_line = line.strip().lstrip("0123456789. ")
            print(f"• {clean_line}")