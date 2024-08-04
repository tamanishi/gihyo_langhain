from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "与えた単語を{language}に変換してください"),
    ("placeholder", "{messages}")
]
)
result = prompt_template.invoke({
    "language": "日本語",
    "messages": [
        ("user", "Hello"),
        ("ai", "こんにちは"),
        ("user", "Good Morning"),
    ]
})
print(result)
