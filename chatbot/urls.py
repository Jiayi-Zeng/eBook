from django.views.decorators.csrf import csrf_exempt
from django.urls import path

from .views import ChatBotView
from .views import OpenAIView

app_name = "chat"
urlpatterns = [
    path("", ChatBotView.as_view(), name="chatbot"),
    path('api/', csrf_exempt(OpenAIView.as_view())),
]