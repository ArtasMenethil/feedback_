from django.shortcuts import render, redirect
from .models import Ticket
from django.contrib import messages
from django.views.generic import CreateView, ListView


def home(request):
    return render(request, 'one/home.html')


class UserTickets(CreateView):
    model = Ticket
    template_name = 'one/tickets.html'

    fields = ['title', 'mess', 'load']

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class ManagerTickets(ListView):
    model = Ticket
    template_name = 'one/manager_tickets.html'
    context_object_name = 'tick'
