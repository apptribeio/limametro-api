import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from limametro.auth.decorators import application_token_required
from limametro.utils.json import date_handler
from limametro.user.models import User
from limametro.device.models import Device

#############################################################################
#
@require_http_methods(["POST"])
@application_token_required('Lima Metro - Devices')
def register(request):
    import uuid
    # Extracting parameters from request.
    name = request.GET.get('name')
    email = request.GET.get('email')
    device = request.GET.get('device')
    
    # Check if values are provided in the request.
    if all([name, email, device]):
        # Looking if user exists in the system.
        user = User.objects.filter(email = email).exists()
        if user:
            # If user exists, look if device is already registered
            current_device = Device.objects.filter(device = device).exists()
            if current_device:
                stored_user = User.objects.get(email = email)
                stored_device = Device.objects.get(device = device)
                # Send json response to client application.
                return HttpResponse(json.dumps({'success':True,
                                                'user':{'name': stored_user.name, 'email': stored_user.email, 'registered': stored_user.registered},
                                                'device':{'device': stored_device.device, 'token': stored_device.token, 'registered':stored_device.registered}}, default = date_handler),
                                    content_type='application/json')
            else:
                stored_user = User.objects.get(email = email)
                new_device = Device()
                new_device.user = stored_user
                new_device.device = device
                new_device.token = uuid.uuid4()
                new_device.registered = timezone.now()
                new_device.status = True
                new_device.save()
                # Retrieve saved device from database.
                stored_device = Device.objects.get(device = device)
                # Send json response to client application.
                return HttpResponse(json.dumps({'success':True,
                                                'user':{'name': stored_user.name, 'email': stored_user.email, 'registered': stored_user.registered},
                                                'device':{'device': stored_device.device, 'token': stored_device.token, 'registered':stored_device.registered}}, default = date_handler),
                                    content_type='application/json')
        else:
            # If user doesn't exists, register the new user in the system.
            new_user = User()
            new_user.email = email
            new_user.name = name
            new_user.registered = timezone.now()
            new_user.status = True
            new_user.save()
            # Register new device in the system.
            stored_user = User.objects.get(email = email)
            new_device = Device()
            new_device.user = stored_user
            new_device.device = device
            new_device.token = uuid.uuid4()
            new_device.registered = timezone.now()
            new_device.status = True
            new_device.save()
            # Retrieve saved user and device from database.
            stored_user = User.objects.get(email = email)
            stored_device = Device.objects.get(device = device)
            # Send json response to client application.
            return HttpResponse(json.dumps({'success':True,
                                            'user':{'name': stored_user.name, 'email': stored_user.email, 'registered': stored_user.registered},
                                            'device':{'device': stored_device.device, 'token': stored_device.token, 'registered':stored_device.registered}}, default = date_handler),
                                content_type='application/json')
    else:
        return HttpResponseBadRequest(json.dumps({'success':False,
                                                 'message': 'The request doesn\'t contains data to register the device', 
                                                 'errors':{'name':'Name data invalid or empty',
                                                           'email':'Email data invalid or empty',
                                                           'device':'Device data invalid or empty'}}), 
                                                 content_type='application/json')