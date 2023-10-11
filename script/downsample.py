import os
import cv2


def image_downsample(image):
    # 获取原始图像的宽度和高度
    height, width = image.shape[:2]

    # 计算下采样后的宽度和高度
    new_width = width // 2
    new_height = height // 2

    # 使用OpenCV的resize函数进行下采样
    downsampled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    return downsampled_image


# 定义图像目录路径
image_directory = 'images/'

# 获取目录中的所有图像文件名
image_files = os.listdir(image_directory)

# 遍历所有图像文件
for filename in image_files:
    # 拼接图像文件路径
    image_path = os.path.join(image_directory, filename)

    # 加载图像
    image = cv2.imread(image_path)

    # 进行下采样
    downsampled_image = image_downsample(image)

    # 构建保存下采样后图像的文件路径
    output_path = os.path.join(image_directory, 'downsampled', filename)

    # 确保保存下采样图像的目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 保存下采样后的图像
    cv2.imwrite(output_path, downsampled_image)
