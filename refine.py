import os
import cv2

# 设置你的文件路径
source_image_path = 'cGAN_data/test/SIRST/mask/Misc_111.png'
target_image_path = 'cGAN_data/test/SIRST/image/Misc_111.png'

# 将图片a的尺寸调整为和图片b一样的函数
def resize_image(a, b):
    return cv2.resize(a, (b.shape[1], b.shape[0]))

# 读取图片a和图片b
source_image = cv2.imread(source_image_path)
target_image = cv2.imread(target_image_path)

# 保存调整后的图片a
cv2.imwrite('source_image_resized.png', resize_image(source_image, target_image))