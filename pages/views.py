from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name='pages/home.html'



class ProfileView(TemplateView):
    template_name = "pages/profile.html"