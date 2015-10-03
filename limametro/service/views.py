import json
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from limametro.utils.json import date_handler
from limametro.auth.decorators import device_token_required
from limametro.service.models import Service

#############################################################################
#
@require_http_methods(["GET"])
@device_token_required('Lima Metro - Services')
def all(request):
    services = Service.objects.all()
    services_list =  []
    for service in services:
        services_list = []
        for service in services:
            services_list.append({'code':service.code,
                                  'name':service.name})
    return HttpResponse(json.dumps({'success':True, 'services':services_list}))