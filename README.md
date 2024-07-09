### Prerequisite
- python 3.12.x
- poetry

### Install
- poetry プロジェクト作成（poetry init）
```
poetry install
poetry add load_dotenv
poetry add langchain langchain_community langchain_openai
poetry add gradio

```

###
```shell
poetry show | egrep '(langchain|openai)'     
langchain                0.2.6    Building applications with LLMs through c...
langchain-community      0.2.6    Community contributed LangChain integrati...
langchain-core           0.2.11   Building applications with LLMs through c...
langchain-text-splitters 0.2.2    LangChain text splitting utilities
openai                   1.35.10  The official Python library for the opena...


```

### OPENAI API Keyを設定
```
echo "OPENAI_API_KEY= sk-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" > .env
```

### 実行
```shell
poetry run python main.py

```

### chatgptサンプル実行（コマンドベースでの会話）
```shell
# Sample1
poetry run python sample/sample1_basic.py
```

### Langchainサンプル実行（Gradioを利用したGUIでの会話）
```shell
poetry run python sample/sample5_langchain_history_gradio.py
```

