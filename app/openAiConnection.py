import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="What is the current sentiment on Bitcoin?",
    max_tokens=100
)

print(response.choices[0].text.strip())
