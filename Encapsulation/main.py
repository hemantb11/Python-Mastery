from google import genai

# Gemini Client
client = genai.Client(api_key="AQ.Ab8RN6LUzi5uPc6rfxf1drA4TDNFy8JKQ_-n0IsxZeF0IoNniQ")

question = input("Type your question: ")

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=f"""
You are an education trainer chatbot.
Answer only education-related questions.
If the user asks anything unrelated to education,
reply only with: I cannot.

User Question:
{question}
"""
)

print(response.text)