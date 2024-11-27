import os
from IPython.display import Image,display
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "sampleChatBot"


llm = ChatOpenAI(model="gpt-4o-mini")

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph,START,END

class State(TypedDict):
    messages:Annotated[list,add_messages]
    
graph_builder = StateGraph(State)

def chatbot(state:State):
    return{"messages":llm.invoke(State["messages"])}

graph_builder.add_node("chatbot",chatbot)
graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot",END)

graph = graph_builder.compile()

while True:
    user = input("User:")
    if user.lower in ["quit","q"]:
        print("Good bye")
    for event in graph.stream({"messages":("user",user)}):
        print(event.values())
    for val in event.values():
            print(val['messages'])
            print("AI :",val["messages"].content)