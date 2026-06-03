from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)
history=[
    SystemMessage(content='you are a helpful ai and you always cry and you are always sad while telling the response')
]

print("Welcome! Type 'quit' to exit.")

while True:
    que = input("You: ").strip()

    if que== "quit":
        break
    history.append(HumanMessage(que))
    response = llm.invoke(history)
    history.append(AIMessage(response.content))
    print(f"Bot: {response.content}")