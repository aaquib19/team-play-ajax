from django.forms import ModelForm


class TeamForm(ModelForm):
    class Meta:
        exclude = ["player"]


