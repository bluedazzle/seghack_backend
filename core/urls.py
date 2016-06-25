from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import AgoraView, RoomView

urlpatterns = patterns('',
                       url(r'^room$', RoomView.as_view()),
                       url(r'^$', AgoraView.as_view()),
                       )
