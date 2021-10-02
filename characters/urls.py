from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='characters-index'),
    path('about/', views.about, name='characters-about'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
]