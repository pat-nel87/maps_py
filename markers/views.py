import json

from django.core.serializers import serialize

from django.views.generic.base import TemplateView

from .models import Marker

class MarkersMapView(TemplateView):
    
    template_name = "map.html"
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serialize("geojson", Marker.objects.all()))
        return context
