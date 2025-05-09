import openai

# openai 1.78.0

# Set your OpenAI API key here
import os
openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_with_openai(prompt):
    response = openai.chat.completions.create(
        model="gpt-4.1-nano-2025-04-14",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    response = chat_with_openai("最も良いインコの名前は何ですか")
    print("OpenAI: " + response)
