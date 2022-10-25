from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class Myform(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
        ]


class MyChangeform(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
        ]
