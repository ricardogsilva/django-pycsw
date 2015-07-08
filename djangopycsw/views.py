from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib.sites.shortcuts import get_current_site
from pycsw.server import Csw

from .pycswsettings import build_pycsw_settings

#import logging
#
#logging.basicConfig(level=logging.DEBUG)


class CswEndpoint(View):

    def get(self, request):
        print("request params: {}".format(request.GET))
        pycsw_settings = build_pycsw_settings()
        server = Csw(rtconfig=pycsw_settings, env=request.META.copy(),
                     version=request.GET["version"])
        server.request = "http://{}{}".format(get_current_site(request),
                                              reverse("csw_endpoint"))
        server.requesttype = request.method
        server.kvp = self._normalize_params(request.GET)
        print("server.iface: {}".format(server.iface))
        print("server.kvp: {}".format(server.kvp))
        status_code, response = server.dispatch()
        print("server.iface: {}".format(server.iface))
        return HttpResponse(response, status=status_code,
                            content_type="application/xml")

    def post(self, request):
        pycsw_settings = build_pycsw_settings()
        server = Csw(rtconfig=pycsw_settings, env=request.META.copy(),
                     version=request.POST["version"])
        server.request = request.body
        server.requesttype = request.method
        status_code, response = server.dispatch()
        return HttpResponse(response, status=status_code,
                            content_type="application/xml")

    def _normalize_params(self, query_dict):
        """
        A hack to overcome PyCSW's early normalizing of KVP args.

        Since PyCSW normalizes KVP args in the server.dispatch_cgi() and
        server.dispatch_wsgi() methods, we need to explicitly do the same
        here, as we are bypassing these methods and calling server.dispatch()
        """

        kvp = dict()
        for k, v in query_dict.iteritems():
            kvp[k.lower()] = v
        return kvp


