import json
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from limametro.utils.json import date_handler
from limametro.auth.decorators import device_token_required
from limametro.station.models import Station

#############################################################################
#
@require_http_methods(["GET"])
#@device_token_required('Lima Metro - Stations')
def all(request):
    stations = Station.objects.all()
    stations_list =  []
    for station in stations:
        services_list = []
        for service in station.services.all():
            services_list.append({'code':service.code,
                                  'name':service.name})
        # Build station list to serialize
        stations_list.append({'code':station.code, 
                              'name':station.name,
                              'map':station.map,
                              'address':station.address,
                              'lat':station.lat,
                              'long':station.long,
                              'open_hour':str(station.open_hour),
                              'close_hour':str(station.close_hour),
                              'services':services_list})
    return HttpResponse(json.dumps({'success':True, 'stations':stations_list}), content_type = 'application/json')

#############################################################################
#
@require_http_methods(["GET"])
#@device_token_required('Lima Metro - Stations')
def details(request, code):
    try:
        station = Station.objects.get(code = code)
        return HttpResponse(json.dumps({'success':True,
                                        'station':{'code':station.code,
                                                   'name':station.name,
                                                   'map':station.map,
                                                   'address':station.address,
                                                   'lat':station.lat,
                                                   'long':station.long,
                                                   'open_hour':str(station.open_hour),
                                                   'close_hour':str(station.close_hour)}}), 
                            mimetype = 'application/json')
    except:
        return HttpResponseNotFound(json.dumps({'success':False,
                                                 'message': 'Station requested doesn\'t exists in the system.', 
                                                 'errors':{'code':'Code invalid or not found'}}), 
                                    content_type = 'application/json')

#############################################################################
#
def services(request, code):
    try:
        station = Station.objects.get(code = code)
        services_list = []
        for service in station.services.all():
            services_list.append({'code':service.code, 'name': service.name})
        return HttpResponse(json.dumps({'success':True,
                                        'services':services_list}), 
                            mimetype = 'application/json')
    except:
        return HttpResponseNotFound(json.dumps({'success':False,
                                                 'message': 'Station requested doesn\'t exists in the system.', 
                                                 'errors':{'code':'Code invalid or not found'}}), 
                                    content_type = 'application/json')

