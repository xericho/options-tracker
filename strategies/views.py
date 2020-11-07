from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
import json

from .models import BasicOption, SpreadOption
from .forms import BasicOptionForm, SpreadOptionForm


def manage(request):
    basic_fields = ('ticker', 'open_date', 'close_date', 'exp_date',
              'longshort', 'callput', 'strike', 'premium',
              'quantity', 'stock_price','fees', 'broker', 'status')
    basics = list(BasicOption.objects.filter(user=request.user).values(*basic_fields))
    spread_fields = ('ticker', 'open_date', 'close_date', 'exp_date',
              'creditdebit', 'callput', 'strike1', 'strike2',
              'premium', 'quantity', 'stock_price','fees', 'broker', 'status')
    spreads = list(SpreadOption.objects.filter(user=request.user).values(*spread_fields))

    return render(request, 'strategies/manage.html', {
        'basics': basics,
        'spreads': spreads,
    })


class BasicOptionCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = BasicOption
    success_message = 'Option added!'
    template_name = 'strategies/create.html'
    fields = ('ticker', 'open_date', 'close_date', 'exp_date',
              'longshort', 'callput', 'strike', 'premium',
              'quantity', 'stock_price','fees', 'broker', 'status')

    def form_valid(self, form):

        model = form.save(commit=False)
        model.user = self.request.user
        model.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Call/Put'
        return context

    def get_success_url(self):
        return reverse('strategies:add_basic')


class BasicOptionUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = BasicOption
    success_message = 'Option updated!'
    success_url = reverse_lazy('strategies:add_basic')
    template_name = 'strategies/update.html'
    fields = ('ticker', 'open_date', 'close_date', 'exp_date',
              'longshort', 'callput', 'strike', 'premium',
              'quantity', 'stock_price','fees', 'broker', 'status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Call/Put'
        return context


class BasicOptionDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = BasicOption
    success_message = 'Option deleted!'
    template_name = 'strategies/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Call/Put'
        return context

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('strategies:add_basic')


class SpreadOptionCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = SpreadOption
    success_message = 'Option added!'
    template_name = 'strategies/create.html'
    fields = ('ticker', 'open_date', 'close_date', 'exp_date',
              'creditdebit', 'callput', 'strike1', 'strike2',
              'premium', 'quantity', 'stock_price','fees', 'broker', 'status')

    def form_valid(self, form):

        model = form.save(commit=False)
        model.user = self.request.user
        model.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Spread'
        return context

    def get_success_url(self):
        return reverse('strategies:add_spread')

class SpreadOptionUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = SpreadOption
    success_message = 'Option updated!'
    success_url = reverse_lazy('strategies:add_spread')
    template_name = 'strategies/update.html'
    fields = ('ticker', 'open_date', 'close_date', 'exp_date',
              'creditdebit', 'callput', 'strike1', 'strike2',
              'premium', 'quantity', 'stock_price','fees', 'broker', 'status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Spread'
        return context


class SpreadOptionDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = SpreadOption
    success_message = 'Option deleted!'
    template_name = 'strategies/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Spread'
        return context

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('strategies:add_spread')
