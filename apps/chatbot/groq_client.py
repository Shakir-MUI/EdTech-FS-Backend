from groq import Groq
from django.conf import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def ask_groq(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # UPDATED SUPPORTED MODEL
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert programming tutor for Python Full Stack. "
                        "Give clear explanations, code examples, and real-world use cases."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=600,
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
