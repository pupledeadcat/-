import json
import os

from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from django.utils.timezone import now
import datetime


from sympy import false
from myapp.models import SysUser,VolunteerInfo,EventInfo,EmployeeInfo,OldpersonInfo
from myapp.camerautil import VideoCamera


# Create your views here.

video_camera = None
def open1(request):
    video_camera = VideoCamera()
    video_camera.start_record('static/video')
    return redirect('/camera')
def video_stream():

    while video_camera != None:
        frame = video_camera.get_frame()

        if frame is not None:
            if frame is not None:
                global_frame = frame
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame
                       + b'\r\n\r\n')
            else:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n'
                       + global_frame + b'\r\n\r\n')
def camera(request):
    name = request.session.get('name')

    return render(request,'camara.html', {'name': name})

                  #content_type='multipart/x-mixed-replace; boundary=frame')
def video_viewer(request):


    return StreamingHttpResponse(video_stream(),  content_type='multipart/x-mixed-replace; boundary=frame')
    # 注意旧版的资料使用mimetype,现在已经改为content_type

