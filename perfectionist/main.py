import gradio as gr
from langchain.messages import AIMessage, HumanMessage  
from langfuse import Langfuse

from perfectionist.graph import graph

 
if Langfuse().auth_check():
    print("Langfuse client is authenticated and ready!")
else:
    print("Authentication failed. Please check your credentials and host.")


def invoke_graph(message, history):
    history_langchain_format = []
    for msg in history:
        if msg["role"] == "user":
            history_langchain_format.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            history_langchain_format.append(AIMessage(content=msg["content"]))
    history_langchain_format.append(HumanMessage(content=message))

    response = graph.invoke({'messages': history_langchain_format})
        
    return response["messages"][-1].content


with gr.Blocks(fill_height=True) as app:
    chatbot = gr.Chatbot()
    gr.ChatInterface(
        invoke_graph,
        api_name = "chat", 
        title = "Perfectionist.",
        fill_height=True,
        chatbot=chatbot
    )

app.launch()

print("App up and running!")