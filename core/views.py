from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class AgoraView(TemplateView):
    template_name = 'index.html'


class RoomView(TemplateView):
    template_name = 'room.html'


class UserAView(TemplateView):
    template_name = 'UserA.html'


class UserBView(TemplateView):
    template_name = 'UserB.html'