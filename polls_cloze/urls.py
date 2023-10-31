from django.urls import path
from . import views

app_name = "cloze_polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("history/", views.HistoryView.as_view(), name="history"),

    path("<int:question_id>/", views.detail, name="detail"),
    
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
 
    path("<int:question_id>/vote2/", views.vote2, name="vote2"),
]
