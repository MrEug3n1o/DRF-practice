from django.urls import path
from .views import SuccessView, CancelView

urlpatterns = [
    path("success/", SuccessView.as_view()),
    path("cancel/", CancelView.as_view()),
]

app_name = "payment"