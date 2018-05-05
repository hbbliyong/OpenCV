import cv2
import os
#使用训练分类器查找人脸
#filepath=".\\img\\xingye-1.png"#不知道为啥相对路径找不到
BASE_DIR=os.path.dirname(__file__)#获取当前文件夹的绝对路径
#filepath="D:\\study\\opencv\\code\\Test\\img\\xingye-3.png"
filepath=os.path.join(BASE_DIR,"img/xingye-3.png")
img=cv2.imread(filepath)
#转换成灰色,图片转换成灰色（去除色彩干扰，让图片识别更准确）
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# OpenCV人脸识别分类器
classifier=cv2.CascadeClassifier("D:\\study\\opencv\\code\\Test\\img\\data\\haarcascades\\haarcascade_frontalface_default.xml")

color=(0,0,255)
#调用识别人脸
faceRects=classifier.detectMultiScale(
    gray,scaleFactor=1.2,minNeighbors=3,minSize=(32,32)
)

if(len(faceRects)):#大于0则检测到人脸
    for faceRect in faceRects:#单独框出每一张人脸
        x,y,w,h=faceRect
        #人脸
        cv2.rectangle(img,(x,y),(x+h,y+w),color,2)
        #左眼
        cv2.circle(img,(x+w//4,y+h//4+30),min(w//8,h//8),color)
        #右眼
        cv2.circle(img,(x+3*w//4,y+h//4+30),min(w//8,h//8),color)
        #嘴巴
        cv2.rectangle(img,(x+3*w//8,y+3*h//4),(x+5*w//8,y+7*h//8),color)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
