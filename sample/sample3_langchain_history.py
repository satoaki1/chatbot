from dotenv import load_dotenv

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 会話履歴を保持するメモリを初期化
memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, memory=memory)


def chat_with_bot():
    print("Chatbot: こんにちは！何か質問がありますか？")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: さようなら！")
            break

        response = conversation.predict(input=user_input)
        print(f"Chatbot: {response}")

        # 会話履歴を表示
        print("\n--- Conversation History ---")
        print(f"Conversation History: {memory.chat_memory}")
        print("----------------------------\n")


if __name__ == '__main__':
    chat_with_bot()
