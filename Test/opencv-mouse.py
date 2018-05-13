# -*- coding: utf-8 -*-

import cv2
#查询opencv支持的鼠标事件
events=[i for i in dir(cv2) if 'EVENT' in i]
print(events)