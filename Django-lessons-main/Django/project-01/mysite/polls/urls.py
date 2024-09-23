from django.urls import path #type: ignore
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #es /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/", views.results, name="results"),
    path("<int:question_id>/", views.vote, name="vote")
]
