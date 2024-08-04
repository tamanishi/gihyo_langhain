from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-3.5-turbo"
)

message = [("user", "こんにちは")]
result = model.invoke(message)
print(result)
