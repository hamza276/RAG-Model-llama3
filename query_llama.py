from groq import Groq
from app_constants import API_KEY

API_KEY = API_KEY  # Replace with your API key

def query_llama_api(query):
    """Directly query the LLaMA 3 model using the Groq client."""
    client = Groq(api_key=API_KEY)  # Pass the API key directly here
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. Your role is to fetch information from the PDF "
                    "and provide the specific information. If the information does not exist, "
                    "please show the message that the query is out of the data provided. Do not "
                    "create your own answers."
                )
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    return response
