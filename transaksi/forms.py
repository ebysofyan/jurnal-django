from django import forms
from .models import Transaksi
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class TransaksiForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    tanggal = forms.DateField(
        initial=datetime.date.today, widget=DateInput)
    uraian = forms.CharField(required=True, widget=forms.Textarea)
    debt = forms.FloatField(required=False, initial=0)
    kredit = forms.FloatField(required=False, initial=0)

    class Meta:
        model = Transaksi
