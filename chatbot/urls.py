from django.urls import path

from .views import ChatBotView

app_name = "chat"
urlpatterns = [
    path("", ChatBotView.as_view(), name="chatbot"),
]