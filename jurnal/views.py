from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from jurnal.forms import JurnalForm
from .models import Jurnal
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HarusLogin(LoginRequiredMixin):
    login_url = '/login/'

class ListJurnalView(HarusLogin, View):
    template_name = 'jurnal/list_jurnal.html'

    def get(self, request):
        data = {
            'list_jurnal': Jurnal.objects.all()
        }
        return render(request, self.template_name, data)


class TambahJurnalView(HarusLogin, View):
    template_name = 'jurnal/tambah_jurnal.html'

    def get(self, request):
        form = JurnalForm(request.POST or None)
        return render(request, self.template_name, {'form': form})


class SimpanJurnalView(HarusLogin, View):
    template_name = 'jurnal/tambah_jurnal.html'

    def post(self, request):
        form = JurnalForm(request.POST or None)
        if form.is_valid():
            jurnal = Jurnal()
            jurnal.user = request.user
            jurnal.nama = form.cleaned_data['nama']
            jurnal.keterangan = form.cleaned_data['keterangan']
            jurnal.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Simpan Jurnal Berhasil')
        return redirect('/jurnal/')


class EditJurnalView(HarusLogin, View):
    template_name = 'jurnal/edit_jurnal.html'

    def get(self, request, id):
        jurnal = Jurnal.objects.get(pk=id)
        initial = {
            'id': jurnal.pk,
            'nama': jurnal.nama,
            'keterangan': jurnal.keterangan,
        }

        form = JurnalForm(initial=initial)
        data = {
            'form': form
        }
        return render(request, self.template_name, data)


class UpdateJurnalView(HarusLogin, View):

    def post(self, request):

        form = JurnalForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            jurnal = Jurnal.objects.get(pk=id)
            jurnal.nama = form.cleaned_data['nama']
            jurnal.keterangan = form.cleaned_data['keterangan']
            jurnal.save(force_update=True)
            return redirect('/jurnal/')


class HapusJurnalView(HarusLogin, View):

    def get(self, request, id):
        jurnal = Jurnal.objects.get(pk=id)
        if jurnal:
            jurnal.delete()
            return redirect('/jurnal/')
