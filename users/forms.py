from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.contrib.auth import get_user_model



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('trading_exp',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('trading_exp',)
