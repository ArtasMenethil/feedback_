from django.urls import path
from . import views as vi

urlpatterns = [
    path('', vi.home, name='home'),
    path('ticket', vi.UserTickets.as_view(), name='ticket'),
    path('tickets_all', vi.ManagerTickets.as_view(), name='tickets_all'),
]