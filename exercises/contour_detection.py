# exercises/contour_detection.py
"""
练习：轮廓检测

描述：
使用 OpenCV 检测图像中的轮廓并将其绘制出来。

请补全下面的函数 `contour_detection`。
"""
import cv2
import numpy as np

def contour_detection(image_path):
    """
    使用 OpenCV 检测图像中的轮廓
    参数:
        image_path: 图像路径
    返回:
        tuple: (绘制轮廓的图像, 轮廓列表) 或 (None, None) 失败时
    """
    # 请在此处编写代码
    # 提示：
    # 1. 使用 cv2.imread() 读取图像。
    # 2. 检查图像是否成功读取。
    # 3. 使用 cv2.cvtColor() 转为灰度图。
    # 4. 使用 cv2.threshold() 进行二值化处理。
    # 5. 使用 cv2.findContours() 检测轮廓 (注意不同 OpenCV 版本的返回值)。
    # 6. 创建图像副本 img.copy() 用于绘制。
    # 7. 使用 cv2.drawContours() 在副本上绘制轮廓。
    # 8. 返回绘制后的图像和轮廓列表。
    # 9. 使用 try...except 处理异常。
    try:
        image = cv2.imread(image_path)
        if image is None:
            return None, None

        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)
        image_edges = cv2.Canny(image_blur, 100, 200)


        contours, _ = cv2.findContours(image_edges, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

        image_with_contours = image.copy()
        cv2.drawContours(
            image_with_contours, 
            contours, 
            contourIdx=-1, #绘制所有轮廓             
            color=(255, 255, 0),          
            thickness=2         #宽2像素        
        )
        #返回需要时list
        contours_list = list(contours)

        return image_with_contours, contours_list
    except Exception as e:
        return None, None