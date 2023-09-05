# chat/views.py

from django.views.generic import TemplateView

class ChatView(TemplateView):
    template_name: str = "chatbot/chatbot.html"