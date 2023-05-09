from django.contrib import messages
from django.core.mail import message
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from website import forms
from website.models import Slider, Service, Package, Video, WebsiteSettings


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        context['services'] = Service.objects.all()
        context['packages'] = Package.objects.all()
        context['videos'] = Video.objects.all()
        context['website'] = WebsiteSettings.objects.first()
        return context


class ContactView(View):

    def post(self, request):
        form = forms.ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data has been saved successfully")
        else:
            messages.error(request, "Invalid! Please try again")
        return redirect('/')


class SubscriberView(View):

    def post(self, request):
        form = forms.SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data has been saved successfully")
        else:
            messages.error(request, "Invalid! Please try again")
        return redirect('/')


# def home(self, request):
#     context={
#
#     }
#
#     return render(request, 'index.html', context=context)