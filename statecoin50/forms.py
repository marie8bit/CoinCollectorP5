from django import forms

from .models import Coin

class CoinCollectorForm(forms.ModelForm):

    class Meta:
        model = Coin
        fields = ('state', 'stURL', 'owned',)

class CoinDetailForm(forms.ModelForm):
    class Meta:
        model= Coin
        fields = ('owned', )
