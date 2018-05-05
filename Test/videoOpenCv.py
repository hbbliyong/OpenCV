#coding=utf-8
#视频人脸检测类 - OpenCV版本
import cv2

#获取摄像头
cap=cv2.VideoCapture(0)
def discern(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
    cap=cv2.CascadeClassifier("D:\\study\\opencv\\code\\Test\\img\\data\\haarcascades\\haarcascade_frontalface_default.xml")
    faceRects=cap.detectMultiScale(
        gray,scaleFactor=1.2,minNeighbors=3,minSize=(50,50))
    if len(faceRects):
        for faceRect  in faceRects:
            x,y,w,h=faceRect
            cv2.rectangle(img,(x,y),(x+h,y+w),(0,255,0),2)
    cv2.imshow("image",img)

while(1):# 逐帧显示
    ret,img=cap.read()
    #cv2.imshow("image",img)
    discern(img)
    if cv2.waitKey(1) & 0xFF==ord('q'):#输入q退出
        break
cap.release()
cv2.destroyAllWindows()        