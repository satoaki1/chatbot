import os

import openai
from dotenv import load_dotenv

# OpenAI APIキーを設定
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def print_messages(messages):
    for message in messages:
        role = message["role"]
        content = message["content"]
        print(f"{role}: {content}")


def main():
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        prompt = input("You: ")
        if prompt == "exit":
            break

        messages.append({"role": "user", "content": prompt})

        # 会話履歴を表示
        print("\n--- Conversation History ---")
        print_messages(messages)
        print("----------------------------\n")

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.9,
        )

        bot_response = response.choices[0].message.content
        print(f"AI: {bot_response}")

        # 会話履歴を追加
        messages.append({"role": "assistant", "content": bot_response})


if __name__ == '__main__':
    main()
