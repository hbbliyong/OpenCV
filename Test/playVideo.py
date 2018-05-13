# -*- coding: utf-8 -*-
"""
create 2018-05-13
"""

import cv2
import numpy as np


cap=cv2.VideoCapture(0)

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('ouput.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):#检测初始化摄像头是否成功
    ret,frame=cap.read() #如果读帧正确返回True
    if ret==True:
        frame=cv2.flip(frame,0)

        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()            