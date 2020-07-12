from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render, redirect

from myapp.roomCamera import RoomCamera

video_camera = []
video_camera.append(RoomCamera())
video_camera[0].__del__()#房间
video_camera.append(RoomCamera())
video_camera[1].__del__()#走廊

video_camera.append(RoomCamera())
video_camera[2].__del__()#院子

video_camera.append(RoomCamera())
video_camera[3].__del__()#桌子
print("yy")


# Create your views here.

def openCamera(request):

    cid = int(request.GET['cid'])
    camera_id = request.session.get('state')
    if camera_id != -1:
        video_camera[camera_id].stop_record()
        video_camera[camera_id].__del__()
    request.session['state'] = cid
    video_camera[cid].__init__()
    video_camera[cid].start_record('myapp')

    return redirect('/camera')

def close(request):
    camera_id = request.session.get('state')
    video_camera[camera_id].stop_record()
    video_camera[camera_id].__del__()
    request.session['state'] = -1

    return redirect('/camera')
def video_stream(camera_id):

    while video_camera[camera_id] != None:
        frame = video_camera[camera_id].get_frame()
        if frame is not None:
            if frame is not None:
                global_frame = frame
                #print(frame)
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
    camera_id = request.session.get('state')
    if camera_id == -1:
        return HttpResponse(None)
    else:
       return StreamingHttpResponse(video_stream(camera_id),  content_type='multipart/x-mixed-replace; boundary=frame')
        # 注意旧版的资料使用mimetype,现在已经改为content_type

