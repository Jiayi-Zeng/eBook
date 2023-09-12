# questions/views.py

from django.views.generic import TemplateView

class QuestionView(TemplateView):
    template_name: str = "question/index.html"