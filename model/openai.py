# 设置API密钥
from langchain_openai.chat_models import ChatOpenAI
import os


openai_api_key = "sk-ze0I9I1tGpciyxLdfs2Ai9qtZf5b5T3smThbCOk2bPsxwnk7"

model = ChatOpenAI(
    temperature=0.7,
    api_key=openai_api_key,
    base_url="https://api.chatanywhere.tech/",
    model_name="gpt-3.5-turbo",
    streaming=True
)

def chat_with_openai_stream(prompt, memory, complete_response=None):

    # 获取历史消息
    history_messages = memory.chat_memory.messages  # 通过 chat_memory 获取历史消息
    print("history_messages:", history_messages)

    # 将历史消息中的 'ai' 角色改为 'assistant'
    formatted_messages = []
    for msg in history_messages:
        if msg['role'] == 'ai':
            formatted_messages.append({'role': 'assistant', 'content': msg['content']})
        else:
            formatted_messages.append({'role': msg['role'], 'content': msg['content']})
    print("formatted_messages:", formatted_messages)

    response_text = ""
    for chunk in model.stream(input=formatted_messages):
        content = chunk.content
        # Access the 'content' attribute safely
        content = getattr(chunk, 'content', None)
        print(content)
        if content is not None:  # 仅当 content 不是 None 或空字符串时才进行累积
            if content.strip():  # Only append non-whitespace content
                response_text += content
                yield content
                print(content)
        else:
            # Handle empty or metadata-only chunks
            print(f"Received empty or metadata-only chunk: {chunk}")
            if hasattr(chunk, 'response_metadata'):
                print(f"Response metadata: {chunk.response_metadata}")


    if complete_response is not None:
        complete_response(response_text)



