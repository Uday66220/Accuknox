from django.urls import path
from . import views

urlpatterns = [
    path("",views.test_signal_view ),
    path("transaction",views.test_signal_transaction_view),
]