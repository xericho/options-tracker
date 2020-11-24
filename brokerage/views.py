from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Broker
from .forms import BrokerForm

BROKERS = {
    'TD': 'TD Ameritrade',
    'RH': 'Robinhood',
}


class BrokerCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Broker
    success_message = 'Broker created!'
    template_name = 'brokerage/create.html'
    form_class = BrokerForm

    def form_valid(self, form):

        model = form.save(commit=False)
        model.user = self.request.user
        model.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('broker:manage')


class BrokerUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Broker
    success_message = 'Broker updated!'
    success_url = reverse_lazy('broker:manage')
    template_name = 'brokerage/update.html'
    form_class = BrokerForm


class BrokerDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Broker
    success_message = 'Broker deleted!'
    template_name = 'brokerage/delete.html'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('broker:manage')


def manage(request):
    brokers = Broker.objects.filter(user=request.user).values()
    for b in brokers:
        b['broker'] = BROKERS[b['broker']]

    return render(request, 'brokerage/manage.html', {
        'brokers': brokers,
    })
