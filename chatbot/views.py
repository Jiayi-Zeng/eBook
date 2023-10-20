from django.shortcuts import render
from django.views.generic.base import TemplateView

class ChatBotView(TemplateView):
    template_name = "chatbot/chatbot.html"

    
