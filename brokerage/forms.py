from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Broker


class BrokerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BrokerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('amount', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('broker', css_class='form-group col-md-6 mb-0'),
                Column('open_date', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )

    class Meta:
        model = Broker
        fields = ('name', 'amount', 'broker', 'open_date')
