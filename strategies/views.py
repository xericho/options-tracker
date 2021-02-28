from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.http import Http404
import json


@login_required
def manage(request):
    return render(request, 'strategies/manage.html', {})


# @login_required
# @api_view(['GET'])
# def get_options(request):
#     option_type = request.query_params.get('option_type')
#     if option_type == 'basic':
#         fields = ['ticker', 'id', 'open_date', 'exp_date', 'longshort',
#                   'callput', 'strike', 'premium', 'quantity', 'stock_price',
#                   'fees', 'close_date', 'close_price', 'profitloss', 'broker__name', 'status']
#         headers = ['Ticker', 'ID', 'Open Date', 'Exp Date', 'Long/Short',
#                    'Call/Put', 'Strike', 'Premium', '#', 'Stock Price', 'Fees',
#                    'Close Date', 'Close Price', 'P/L', 'Broker', 'Status']
#         data = list(BasicOption.objects.filter(user=request.user).values(*fields))
#     elif option_type == 'spreads':
#         fields = ['ticker', 'id', 'open_date', 'exp_date',
#                   'creditdebit', 'callput', 'strike1', 'strike2',
#                   'premium', 'quantity', 'stock_price','fees',
#                   'close_date', 'close_price', 'profitloss', 'broker__name', 'status']
#         headers = ['Ticker', 'ID', 'Open Date', 'Exp Date', 'Credit/Debit',
#                    'Call/Put', 'Strike 1', 'Strike 2', 'Premium', '#', 'Stock Price', 'Fees',
#                    'Close Date', 'Close Price', 'P/L', 'Broker', 'Status']
#         data = list(SpreadOption.objects.filter(user=request.user).values(*fields))
#     else:
#         raise Http404
#
#     fields = [{'data': f, 'title': h} for f,h in zip(fields, headers)]
#     fields += [{'data': 'edit', 'title': 'Modify'}, ]
#     for d in data:
#         d['edit'] = None
#
#     return Response({
#         'data': data,
#         'fields': fields,
#         'headers': headers,
#     })
#
#
# class BasicOptionCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
#     model = BasicOption
#     success_message = 'Option added!'
#     template_name = 'strategies/create.html'
#     form_class = BasicOptionForm
#
#     def form_valid(self, form):
#         model = form.save(commit=False)
#         model.user = self.request.user
#         model.save()
#
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['type'] = 'Call/Put'
#         return context
#
#     def get_success_url(self):
#         return reverse('strategies:manage')
#
#
# class BasicOptionUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
#     model = BasicOption
#     success_message = 'Option updated!'
#     success_url = reverse_lazy('strategies:manage')
#     template_name = 'strategies/update.html'
#     form_class = BasicOptionForm
#
#     def form_valid(self, form):
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['type'] = 'Call/Put'
#         return context
#
#
# class BasicOptionDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
#     model = BasicOption
#     success_message = 'Option deleted!'
#     template_name = 'strategies/delete.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['type'] = 'Call/Put'
#         return context
#
#     def get_success_url(self):
#         messages.success(self.request, self.success_message)
#         return reverse('strategies:manage')
#
#
# class SpreadOptionCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
#     model = SpreadOption
#     success_message = 'Option added!'
#     template_name = 'strategies/create.html'
#     form_class = SpreadOptionForm
#
#     def form_valid(self, form):
#
#         model = form.save(commit=False)
#         model.user = self.request.user
#         model.save()
#
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['type'] = 'Spread'
#         return context
#
#     def get_success_url(self):
#         return reverse('strategies:manage')
#
#
# class SpreadOptionUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
#     model = SpreadOption
#     success_message = 'Option updated!'
#     success_url = reverse_lazy('strategies:manage')
#     template_name = 'strategies/update.html'
#     form_class = SpreadOptionForm
#
#     def form_valid(self, form):
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['type'] = 'Spread'
#         return context
#
#
# class SpreadOptionDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
#     model = SpreadOption
#     success_message = 'Option deleted!'
#     template_name = 'strategies/delete.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['type'] = 'Spread'
#         return context
#
#     def get_success_url(self):
#         messages.success(self.request, self.success_message)
#         return reverse('strategies:manage')
#
#
# def upload(request):
#     if request.method == 'POST':
#         form = CsvForm(request.POST, request.FILES)
#         if form.is_valid():
#             if form.cleaned_data['option_type'] == 'basic':
#                 BasicOption.objects.all().delete()
#                 load_basic_options(form.cleaned_data['csv'].file)
#             elif form.cleaned_data['option_type'] == 'spread':
#                 SpreadOption.objects.all().delete()
#                 load_spread_options(form.cleaned_data['csv'].file)
#
#             return redirect('strategies:upload')
#     else:
#         form = CsvForm()
#
#     return render(request, 'strategies/upload.html', {
#         'form': form,
#     })
