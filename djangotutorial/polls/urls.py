from django.urls import path
from . import views, apps

#app_name = "polls"
#urlpatterns = [
#    # ex: /polls/
#    path("", views.index, name="index"),
#    # ex: /polls/5/
#    path("<int:question_id>/", views.detail, name="detail"),
#    # ex: /polls/5/results/
#    path("<int:question_id>/results/", views.results, name="results"),
#   # ex: /polls/5/vote/
#    path("<int:question_id>/vote/", views.vote, name="vote"),
#]

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("all/", views.AllView.as_view(), name="all"),
    path("<int:pk>/frequency/", views.FrequencyView.as_view(), name="frequency"),
    path('add/', views.add, name='add'),
#    path('confirm_add/', views.confirm_add, name='confirm_add'),
#    path("formulaire/", views.formulaire_choix, name="formulaire_choix"),
]