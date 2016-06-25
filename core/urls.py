from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import AgoraView, RoomView, UserAView, UserBView

urlpatterns = patterns('',
                       url(r'^room$', RoomView.as_view()),
                       url(r'^usera', UserAView.as_view()),
                       url(r'^userb', UserBView.as_view()),
                       url(r'^$', AgoraView.as_view()),
                       )
