from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from bootstrap_datepicker_plus import DatePickerInput

# from .models import BasicOption, SpreadOption
#
#
# class BasicOptionForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(BasicOptionForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('ticker', css_class='form-group col-md-3 mb-0'),
#                 Column('open_date', css_class='form-group col-md-3 mb-0'),
#                 Column('exp_date', css_class='form-group col-md-3 mb-0'),
#                 Column('stock_price', css_class='form-group col-md-3 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('longshort', css_class='form-group col-md-3 mb-0'),
#                 Column('callput', css_class='form-group col-md-3 mb-0'),
#                 Column('strike', css_class='form-group col-md-3 mb-0'),
#                 Column('premium', css_class='form-group col-md-3 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('quantity', css_class='form-group col-md-4 mb-0'),
#                 Column('close_price', css_class='form-group col-md-4 mb-0'),
#                 Column('close_date', css_class='form-group col-md-4 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('broker', css_class='form-group col-md-6 mb-0'),
#                 Column('status', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             Submit('submit', 'Submit')
#         )
#
#     class Meta:
#         model = BasicOption
#         fields = ('ticker', 'open_date', 'close_date', 'exp_date',
#                   'longshort', 'callput', 'strike', 'premium',
#                   'close_price', 'profitloss', 'quantity',
#                   'stock_price','fees', 'broker', 'status')
#         widgets = {
#             'open_date': DatePickerInput(options={
#                 "format": 'YYYY-MM-DD',
#             }),
#             'exp_date': DatePickerInput(options={
#                 "format": 'YYYY-MM-DD',
#             }),
#             'close_date': DatePickerInput(options={
#                 "format": 'YYYY-MM-DD',
#             }),
#         }
#
#
# class SpreadOptionForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(SpreadOptionForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('ticker', css_class='form-group col-md-3 mb-0'),
#                 Column('open_date', css_class='form-group col-md-3 mb-0'),
#                 Column('exp_date', css_class='form-group col-md-3 mb-0'),
#                 Column('stock_price', css_class='form-group col-md-3 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('creditdebit', css_class='form-group col-md-3 mb-0'),
#                 Column('callput', css_class='form-group col-md-3 mb-0'),
#                 Column('strike1', css_class='form-group col-md-3 mb-0'),
#                 Column('strike2', css_class='form-group col-md-3 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('premium', css_class='form-group col-md-3 mb-0'),
#                 Column('quantity', css_class='form-group col-md-3 mb-0'),
#                 Column('close_price', css_class='form-group col-md-3 mb-0'),
#                 Column('close_date', css_class='form-group col-md-3 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('broker', css_class='form-group col-md-6 mb-0'),
#                 Column('status', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             Submit('submit', 'Submit')
#         )
#     class Meta:
#         model = SpreadOption
#         fields = ('ticker', 'open_date', 'close_date', 'exp_date',
#                   'creditdebit', 'callput', 'strike1', 'strike2',
#                   'premium', 'quantity', 'stock_price','fees', 'profitloss',
#                   'close_date', 'close_price', 'broker', 'status')
#         widgets = {
#             'open_date': DatePickerInput(options={
#                 "format": 'YYYY-MM-DD',
#             }),
#             'exp_date': DatePickerInput(options={
#                 "format": 'YYYY-MM-DD',
#             }),
#             'close_date': DatePickerInput(options={
#                 "format": 'YYYY-MM-DD',
#             }),
#         }
#
# class CsvForm(forms.Form):
#     option_type = forms.ChoiceField(choices=(('basic', 'Basic'), ('spread', 'Spread')), widget=forms.Select(attrs={'style':'width:15rem;'}))
#     csv = forms.FileField(
#         label='Select a file',
#     )
#
