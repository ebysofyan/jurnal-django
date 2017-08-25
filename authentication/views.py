from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm
from django.contrib import messages
from django.http import HttpResponse

import requests
# Create your views here.


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/jurnal/')

        form = LoginForm(request.POST or None)
        data = {
            'form': form
        }
        return render(request, self.template_name, data)


class AksiLoginView(View):

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/jurnal/')
            else:
                messages.add_message(request, messages.WARNING,
                                     'Username dan Password salah!!!')

        return redirect('/login/')


class AksiLogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/login/')


class SendSMSView(View):
    template_name = 'test.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        msg = request.POST['msg']
        dst_number = request.POST['dst_number']

        url = 'http://api.nusasms.com/api/v3/sendsms/plain'
        data = {
            'user': 'ebysofyan_api',
            'password': 'ebyjurit73',
            'SMSText': msg,
            'GSM': dst_number,
            'output': 'json',
        }
        resp = requests.post(url, data=data)

        messages.add_message(request, messages.SUCCESS, resp.json())
        return redirect('/test/')
