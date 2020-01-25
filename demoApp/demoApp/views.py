from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import cv2
import os
from django.http import JsonResponse
from threading import Thread



def index(request):
    return render(request,'index.html')


def faceDetection():
    path = '/mnt/0812FFDF12FFD024/Kartik/Documents/VirtualEnvs/vision/lib/python3.7/site-packages/cv2/data/'
    # face_cascade = cv2.CascadeClassifier('C:\\Users\\CHETAN SHARMA\\Desktop\\dempMachineLearningWebApp\\demoApp\\demoApp\\haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(path+'haarcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    # print('here')
    
    while user_present:
        # print('hello', end=' ')
        _, img = cap.read()

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.1,4)

        for(x,y,w,h) in faces:
            cv2.rectange(img,(x,y),(x+w,y+h),(255,0,0),2)
        # directory = 'C:\\Users\\CHETAN SHARMA\\Desktop\\dempMachineLearningWebApp\\demoApp\\static'
        directory = '/home/kartik/Documents/faceDetection-Website/static'
        os.chdir(directory)
        cv2.imwrite('1.png',img)
        # cv2.imshow('Image', img)
        # if cv2.waitKey(1) & 0xff == 27:
        #     cv2.destroyAllWindows()
        #     break
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
    user_present = False
    data={}
    return JsonResponse(data)


user_present = True
# helperFunction(2)