from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import cv2
import os
from django.http import JsonResponse
from threading import Thread
user_present=True


def index(request):
    return render(request,'index.html')


def faceDetection(request):
    face_cascade = cv2.CascadeClassifier('C:\\Users\\CHETAN SHARMA\\Desktop\\dempMachineLearningWebApp\\demoApp\\demoApp\\haarcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    
    while user_present:
        _, img = cap.read()

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.1,4)

        for(x,y,w,h) in faces:
            cv2.rectange(img,(x,y),(x+w,y+h),(255,0,0),2)
        directory = 'C:\\Users\\CHETAN SHARMA\\Desktop\\dempMachineLearningWebApp\\demoApp\\static'
        os.chdir(directory)
        cv2.imwrite('1.png',img)
    cap.release()
    # data={}
    # return JsonResponse(data)
        # return render(request,'face detection.html')
        # cv2.imshow('img',img)
        # k=cv2.waitKey(30) & 0xff
        # if k==27:
        #     break

    # _, img = cap.read()
    
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # directory = 'C:\\Users\\CHETAN SHARMA\\Desktop\\dempMachineLearningWebApp\\demoApp\\static'
    # os.chdir(directory)
    # cv2.imwrite('1.png',img)
    # directory = 'C:\\Users\\CHETAN SHARMA\\Desktop\\dempMachineLearningWebApp\\demoApp'
    # os.chdir(directory)

    # # cv2.imshow('img', img)
    # cv2.waitKey()
    # cap.release()
    # data={status:200,
    #     images:10}
    # return render(request,'faceDetection.html')
    # return JsonResponse(data)

def helperFunction(request):
    Thread(target=faceDetection).start()
    data={}
    return JsonResponse(data)


def userQuits(request):
    global user_present
    user_present=false
    data={}
    return JsonResponse(data)
