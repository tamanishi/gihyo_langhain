from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.prompts.chat import SystemMessagePromptTemplate

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "与えた単語を{language}に変換してください"),
    ("user", "Hello")
]
)
result = prompt_template.invoke(
    {"language": "日本語"}
)
print(result)
