import json
import os
import time

from django.core import serializers
from django.forms import model_to_dict
from django.http import StreamingHttpResponse, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.timezone import now
import datetime


import numpy as np
from myapp.models import EventInfo


def events_info(request):
    name = request.session.get('name')

    list = np.arange(0,50)
    return render(request, 'events_info.html', {'name': name,'list':list})

from dwebsocket.decorators import accept_websocket,require_websocket

@accept_websocket
def test_websocket(request):

    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request,'events_info.html')
    else:
        while 1:
            events = EventInfo.objects.all().order_by("-id")

            dit = {
                'time':time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
            }
            data = serializers.serialize("json", events)
            #data = list(data)
            request.websocket.send(data)#发送消息到客户端
            time.sleep(1)
