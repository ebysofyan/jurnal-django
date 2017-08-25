from django import forms
from orm.models import Jurnal


class JurnalForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    nama = forms.CharField(max_length=30)
    keterangan = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Jurnal
