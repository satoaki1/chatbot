# chatbot

---

### Prerequisite
- python 3.12.3
- poetry

### Install
- poetry プロジェクト作成（poetry init）
```
poetry install
poetry add openai load_dotenv
poetry add googlesearch-python

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