import numpy as np
import cv2
import face_recognition

imgelon = face_recognition.load_image_file('images path/elon musk.jpeg')
imgelon = cv2.cvtColor(imgelon, cv2.COLOR_BGR2RGB)
imgelon2 = face_recognition.load_image_file('images path/jeff bezoz.jpeg')
imgelon2 = cv2.cvtColor(imgelon2, cv2.COLOR_BGR2RGB)

faceloc=face_recognition.face_locations(imgelon)[0]
encodeelon=face_recognition.face_encodings(imgelon)[0]
cv2.rectangle(imgelon,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,255,255),1)


faceloc2=face_recognition.face_locations(imgelon2)[0]
encodeelon2=face_recognition.face_encodings(imgelon2)[0]
cv2.rectangle(imgelon2,(faceloc2[3],faceloc2[0]),(faceloc2[1],faceloc2[2]),(255,255,255),1)


results=face_recognition.compare_faces([encodeelon],encodeelon2)
facedistance=face_recognition.face_distance([encodeelon],encodeelon2)

print(results,facedistance)

cv2.putText(imgelon2,f'{results} {round(facedistance[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow('elon', imgelon)
cv2.imshow('elon test', imgelon2)
cv2.waitKey(0)