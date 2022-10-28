from django.urls import path, include
from . import views

urlpatterns = [
    path("meals/", views.MealsList.as_view()),
    path("meals/<int:pk>/", views.MealPK.as_view()),
    path("ratings/", views.RatingList.as_view()),
    path("ratings/<int:pk>/", views.RatingPK.as_view()),
]
