from django.urls import path
from . import views

app_name = "cloze"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("history/", views.HistoryView.as_view(), name="history"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:publish_id>/vote/", views.vote, name="vote"),
]