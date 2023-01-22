# importing the dependencies 

import numpy as np
import cv2
import face_recognition
import os
from datetime import datetime
input("enter any key to continue")
#getting the images from images path
path='images path'
images=[]
ClassName=[]
mylist=os.listdir(path)
print(mylist)
for cl in mylist:
    curimg=cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    ClassName.append(os.path.splitext(cl)[0])

print(ClassName)



#encoding the images with build in encoder of face recognition 


#checking the images from the list
def FindEncoding(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


#mark the attendance
def markAttendence(name):
    with open('attendance.csv','r+') as f:
        mydatalist= f.readlines()
        namelist=[]
        for line in mydatalist:
            entry=line.split(',')
            namelist.append(entry[0])

        if name not in namelist:
            now=datetime.now()
            datestring=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{datestring}')



encodeListKnown=FindEncoding(images)  #finding the encoding
print("Encoding complete")  #massage to the user that model has been trained 


#showing the camera and drowning the rectangle

cap=cv2.VideoCapture(1)

while True:
    SUCCESS,img=cap.read()
    imgs=cv2.resize(img,(0,0),None,0.25,0.25)
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

    faceCurFrame=face_recognition.face_locations(imgs)
    encodesCurFrame=face_recognition.face_encodings(imgs,faceCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,faceCurFrame):
        mateches=face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
        matchIndex=np.argmin(faceDis)

        if mateches[matchIndex]:
            name=ClassName[matchIndex].upper()
            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,255,255),1)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(255,255,255),cv2.FILLED)

            cv2.putText(img,name,(x1+6,y2-6,),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1)
            
            markAttendence(name)

    
    cv2.imshow('webcam',img)
    cv2.waitKey(1)

