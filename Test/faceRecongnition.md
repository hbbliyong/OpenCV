# 人脸识别--使用训练分类器查找人脸

## 1.坑

## 2.知识点

### 2.1 判断文件是否存在

>这里有个问题，不知道咋回事相对路径怎么都找不到文件

```python
import os
 
filepath="img/xingye-1.png"
print(filepath)
if os.path.exists("D:\\study\\opencv\\code\\Test\\img\\xingye-1.png"):
    print('ssss')
else:
    print("xxxx")
```

代码文件所在路径

```python
print(__file__)
#文件所在目录
os.path.dirname(os.path.realpath(__file__))
```
