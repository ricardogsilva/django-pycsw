from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.shortcuts import get_current_site

from pycsw.server import Csw


class CswEndpoint(View):

    def get(self, request):
        server = Csw(rtconfig=settings.PYCSW_CONFIG, env=request.META.copy(),
                     version=request.GET["version"])
        server.request = "http://{}{}".format(get_current_site(request),
                                              reverse("csw_endpoint"))
        server.requesttype = request.method
        server.kvp = request.GET
        status_code, response = server.dispatch()
        return HttpResponse(response, status=status_code,
                            content_type="application/xml")

    def post(self, request):
        server = Csw(rtconfig=settings.PYCSW_CONFIG, env=request.META.copy(),
                     version=request.GET["version"])
        server.request = request.body
        server.requesttype = request.method
        status_code, response = server.dispatch()
        return HttpResponse(response, status=status_code,
                            content_type="application/xml")
