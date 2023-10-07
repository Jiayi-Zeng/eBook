# chat/views.py

from django.views.generic import TemplateView
import openai

class ChatView(TemplateView):
    template_name: str = "chatbot/chatbot.html"
    

openai.api_key = "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"

openai.proxy = "http://127.0.0.1:1080"

conversation=[{"role": "system", "content": "You are a helpful assistant."}]

while(True):
    user_input = input()      
    conversation.append({"role": "user", "content": user_input})
    print(conversation)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = conversation
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    print("\n" + response['choices'][0]['message']['content'] + "\n")
    print(conversation)

