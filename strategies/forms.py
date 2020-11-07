from crispy_forms.helper import FormHelper
from django import forms

from .models import BasicOption, SpreadOption


class BasicOptionForm(forms.ModelForm):
    class Meta:
        model = BasicOption
        fields = ('ticker', 'open_date', 'close_date', 'exp_date',
                  'longshort', 'callput', 'strike', 'premium',
                  'quantity', 'stock_price','fees', 'broker', 'status')

class SpreadOptionForm(forms.ModelForm):
    class Meta:
        model = SpreadOption
        fields = ('ticker', 'open_date', 'close_date', 'exp_date',
                  'creditdebit', 'callput', 'strike1', 'strike2',
                  'premium', 'quantity', 'stock_price','fees', 'broker', 'status')
