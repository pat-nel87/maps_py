# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 19:25:06 2020

@author: Patrick
"""

"""Markers urls."""

from django.urls import path

from .views import MarkersMapView

app_name = "markers"

urlpatterns = [
    path("map/", MarkersMapView.as_view()),
]