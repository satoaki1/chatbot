from dotenv import load_dotenv

from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo")

conversation = ConversationChain(llm=llm)


def chat_with_bot():
    print("Chatbot: こんにちは！何か質問がありますか？")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: さようなら！")
            break
        response = conversation.predict(input=user_input)
        print(f"Chatbot: {response}")


if __name__ == '__main__':
    chat_with_bot()
