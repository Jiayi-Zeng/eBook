# chat/views.py

from django.views.generic import TemplateView
import openai
import json
from django.shortcuts import render

openai.api_key = "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"

openai.proxy = "http://127.0.0.1:7890"

conversation=[
                { "role": "system", "content": "You are a helpful assistant." },
                { "role": "user", "content": "Who won the world series in 2020?" },
                { "role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020." },
                { "role": "user", "content": "Where was it played?" }
            ]

# while(True):
#     user_input = input()      
#     conversation.append({"role": "user", "content": user_input})
#     print(conversation)

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo", 
#         messages = conversation
#     )

#     conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
#     print("\n" + response['choices'][0]['message']['content'] + "\n")
#     print(conversation)

# class ChatView(TemplateView):
#     template_name: str = "chatbot/chatbot.html"

#     conversation=[
#                 { "role": "system", "content": "You are a helpful assistant." },
#                 { "role": "user", "content": "Who won the world series in 2020?" },
#                 { "role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020." },
#                 { "role": "user", "content": "Where was it played?" }
#             ]

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context.update({
#             'conversation': conversation,
#         })

#         return context

import json
from django.shortcuts import render

def chat_view(request):
    conversation = [
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "user", "content": "Who won the world series in 2020?" },
        { "role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020." },
        { "role": "user", "content": "Where was it played?" }
    ]

    conversation_json = json.dumps(conversation)

    context = {
        'conversation_json': conversation_json
    }

    return render(request, 'chatbot/chatbot.html', context)