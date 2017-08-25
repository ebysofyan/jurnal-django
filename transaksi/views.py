from django.shortcuts import render, redirect
from django.views import View
from .models import Transaksi
from jurnal.models import Jurnal
from transaksi.forms import TransaksiForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HarusLogin(LoginRequiredMixin):
    login_url = '/login/'

class ListTransaksiView(HarusLogin, View):
    template_name = 'transaksi/list_transaksi.html'

    def get(self, request, jurnal_id):
        jurnal = Jurnal.objects.get(pk=jurnal_id)
        list_transaksi = Transaksi.objects.filter(jurnal=jurnal)

        list_hasil = []
        kas = 0
        for trx in list_transaksi:
            kas = kas + (trx.debt - trx.kredit) 
            hasil = {
                'id': trx.pk,
                'tanggal': trx.tanggal,
                'uraian': trx.uraian, 
                'debt': trx.debt,
                'kredit': trx.kredit,
                'kas': kas
            }
            list_hasil.append(hasil)

        form = TransaksiForm(request.POST or None)
        data = {
            'jurnal': jurnal,
            'form': form,
            'list_hasil': list_hasil,
            'total_kas': kas,
        }
        return render(request, self.template_name, data)

class SimpanTransaksiView(HarusLogin,View):
    def post(self, request, jurnal_id):
        form = TransaksiForm(request.POST or None)
        if form.is_valid():
            jurnal = Jurnal.objects.get(pk=jurnal_id)

            transaksi = Transaksi()
            transaksi.jurnal = jurnal
            transaksi.tanggal = form.cleaned_data['tanggal']
            transaksi.uraian = form.cleaned_data['uraian']
            transaksi.debt = form.cleaned_data['debt']
            transaksi.kredit = form.cleaned_data['kredit']
            transaksi.save()

            return redirect(reverse_lazy('transaksi:view', kwargs={'jurnal_id': jurnal_id}))

class UbahTransaksiView(HarusLogin,View):
    template_name = 'transaksi/list_transaksi_ubah.html'
    def get(self, request, jurnal_id, trx_id):
        jurnal = Jurnal.objects.get(pk=jurnal_id)
        transaksi = Transaksi.objects.get(jurnal=jurnal, pk=trx_id)
        list_transaksi = Transaksi.objects.filter(jurnal=jurnal)

        list_hasil = []
        kas = 0
        for trx in list_transaksi:
            kas = kas + (trx.debt - trx.kredit) 
            hasil = {
                'id': trx.id,
                'tanggal': trx.tanggal,
                'uraian': trx.uraian, 
                'debt': trx.debt,
                'kredit': trx.kredit,
                'kas': kas
            }
            list_hasil.append(hasil)

        data_awal = {
            'id': transaksi.pk,
            'tanggal': transaksi.tanggal,
            'uraian': transaksi.uraian,
            'debt': transaksi.debt,
            'kredit': transaksi.kredit
        }
        form = TransaksiForm(request.POST or None, initial=data_awal)
        data = {
            'jurnal': jurnal,
            'form': form,
            'list_hasil': list_hasil,
            'transaksi': transaksi,
            'total_kas': kas,
        }
        return render(request, self.template_name, data)

class UpdateTransaksiView(HarusLogin, View):
    def post(self, request, jurnal_id):
        form = TransaksiForm(request.POST or None)
        if form.is_valid():
            jurnal = Jurnal.objects.get(id=jurnal_id)

            transaksi_id = form.cleaned_data['id']
            transaksi = Transaksi.objects.get(pk=transaksi_id)
            transaksi.jurnal = jurnal
            transaksi.tanggal = form.cleaned_data['tanggal']
            transaksi.uraian = form.cleaned_data['uraian']
            transaksi.debt = form.cleaned_data['debt']
            transaksi.kredit = form.cleaned_data['kredit']
            transaksi.save(force_update=True)

            return redirect(reverse_lazy('transaksi:view', kwargs={'jurnal_id': jurnal_id}))

class HapusTransaksiView(HarusLogin, View):
    def get(self, request, jurnal_id, trx_id):
        jurnal = Jurnal.objects.get(id=jurnal_id)
        transaksi = Transaksi.objects.get(jurnal=jurnal, pk=trx_id)
        if transaksi:
            transaksi.delete()

            return redirect(reverse_lazy('transaksi:view', kwargs={'jurnal_id': jurnal_id}))