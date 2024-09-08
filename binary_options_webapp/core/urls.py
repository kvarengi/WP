from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bet/", views.bet, name="bet"),
    path("transaction_history/", views.transaction_history, name="transaction_history"),
    path("sell/", views.sell, name="sell"),
    path("deposit/", views.deposit, name="deposit"),
    path("profile/", views.profile, name="profile"),
]
