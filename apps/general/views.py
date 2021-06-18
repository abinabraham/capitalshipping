from django.shortcuts import render

# Create your views here.
from django.views.generic import (View,TemplateView, ListView, DetailView, 
                                 CreateView,UpdateView,DeleteView,FormView)
from apps.home.models import *
from apps.services.models import *
from apps.aboutus.models import *
from apps.gallery.models import Gallery
from django.http import HttpResponse
from apps.contacts.models import ContactedDetails

import json

class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        all_choices = WhyChooseUs.objects.filter(is_verified=True)
        who_we_are = Whoweare.objects.filter(is_verified=True)
        context = {'all_choices': all_choices, "who_we_are":who_we_are}
        return render(request, self.template_name, context)

class ServiceView(TemplateView):
    template_name = "services.html"

    def get(self, request, *args, **kwargs):
        services = Services.objects.filter(is_verified=True)
        partners = Partners.objects.filter(is_verified=True)
        context = {'services': services, 'partners':partners}
        return render(request, self.template_name, context)


class ServiceDetailView(DetailView):
    template_name = "service_details.html"
    model = Services

class AboutUsView(TemplateView):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        about = AboutIntro.objects.filter(is_verified=True)
        dob = DirectorsBoard.objects.filter(is_verified=True)
        whyus = WhyChooseUs.objects.filter(is_verified=True)
        context = {'about': about, 'dob':dob, 'whyus':whyus}
        return render(request, self.template_name, context)

class GalleryView(TemplateView):
    template_name = "gallery.html"

    def get(self, request, *args, **kwargs):
        gallery = Gallery.objects.filter(is_verified=True)
        context = {'gallery': gallery}
        return render(request, self.template_name, context)

class ContactView(TemplateView):
    template_name = "contact.html"





class contactSubmit(View):

    def post(self,request,**kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        data = {}
        try:
            ContactedDetails.objects.create(
                name = name,
                email = email,
                mobile = mobile,
                des = message
            )
            msg = "success"
        except Exception as e:
            print("===========",e)
            msg = "failed"

        return HttpResponse(
            json.dumps(msg),
            **kwargs)