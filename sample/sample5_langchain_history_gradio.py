import gradio as gr
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 会話履歴を保持するメモリを初期化
memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, memory=memory)


def chat_with_bot(user_input):
    if user_input.lower() in ["exit", "quit", "bye"]:
        return "Chatbot: さようなら！"

    response = conversation.predict(input=user_input)

    # 会話履歴を表示
    print("\n--- Conversation History ---")
    print(f"Conversation History: {memory.chat_memory}")
    print("----------------------------\n")

    return response


gradio_main = gr.Interface(fn=chat_with_bot,
                           inputs="text",
                           outputs="text",
                           title="My First AI Chatbot",
                           description="何か質問ありますか？")

if __name__ == '__main__':
    gradio_main.launch(share=True)
