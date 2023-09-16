from django.urls import path
from .views import QuestionView

app_name = "question"

urlpatterns = [path("", QuestionView.as_view(), name="question")]