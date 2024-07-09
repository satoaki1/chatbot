import os

import openai
from dotenv import load_dotenv

# OpenAI APIキーを設定
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def main():
    while True:
        prompt = input("You: ")
        if prompt == "exit":
            break

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.9,
        )

        bot_response = response.choices[0].message.content
        print(f"AI: {bot_response}")


if __name__ == '__main__':
    main()
