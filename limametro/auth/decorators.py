import base64
import json
from django.http import HttpResponse, HttpResponseForbidden
from limametro.auth.models import Token
from limametro.device.models import Device

#############################################################################
#
def application_token_required(realm=''):
    def view_decorator(view):
        def wrapper(request, *args, **kwargs):
            if 'HTTP_AUTHORIZATION' in request.META:
                auth = request.META['HTTP_AUTHORIZATION'].split()
                if len(auth) == 2:
                    # NOTE: We are only support basic authentication for now.
                    #
                    if auth[0].lower() == "basic":
                        username, password = base64.b64decode(auth[1]).split(':')
                        token = Token.objects.filter(username = username, token = password).exists()
                        if token:
                            return view(request, *args, **kwargs)
                        else:
                            return HttpResponseForbidden(json.dumps({'success':False,
                                                                     'message': 'The provided token is invalid or can\'t be found in the server', 
                                                                     'errors':{'username':'Username invalid or not found',
                                                                               'token':'Token invalid or not found'}}), 
                                                         mimetype='application/json')
            # Either they did not provide an authorization header or
            # something in the authorization attempt failed. Send a 401
            # back to them to ask them to authenticate.
            #
            response = HttpResponse()
            response.status_code = 401
            response['WWW-Authenticate'] = 'Basic realm="%s"' % realm
            return response
        return wrapper
    return view_decorator

#############################################################################
#
def device_token_required(realm=''):
    def view_decorator(view):
        def wrapper(request, *args, **kwargs):
            if 'HTTP_AUTHORIZATION' in request.META:
                auth = request.META['HTTP_AUTHORIZATION'].split()
                if len(auth) == 2:
                    # NOTE: We are only support basic authentication for now.
                    #
                    if auth[0].lower() == "basic":
                        username, password = base64.b64decode(auth[1]).split(':')
                        device = Device.objects.filter(device = username, token = password).exists()
                        if device:
                            return view(request, *args, **kwargs)
                        else:
                            return HttpResponseForbidden(json.dumps({'success':False,
                                                                     'message': 'The provided token is invalid or can\'t be found in the server', 
                                                                     'errors':{'device':'Device invalid or not found',
                                                                               'token':'Token invalid or not found'}}), 
                                                         mimetype='application/json')
            # Either they did not provide an authorization header or
            # something in the authorization attempt failed. Send a 401
            # back to them to ask them to authenticate.
            #
            response = HttpResponse()
            response.status_code = 401
            response['WWW-Authenticate'] = 'Basic realm="%s"' % realm
            return response
        return wrapper
    return view_decorator