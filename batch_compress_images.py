# 批量压缩当前文件夹内的jpg图片，当文件大小大于1MB时，压缩质量为85
# 复制本脚本到目标文件夹内，运行即可，不用加任何参数

import os
from PIL import Image

def compress_image(input_image_path, output_image_path, quality=85):
    with Image.open(input_image_path) as img:
        img.save(output_image_path, 'JPEG', quality=quality, optimize=True)

def batch_compress_images(directory, quality=85):
    for filename in os.listdir(directory):
        #if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        # 如果是jpg文件，且文件大小大于1MB，则进行压缩
        if filename.lower().endswith(('.jpg')) and os.path.getsize(os.path.join(directory, filename)) > 1024 * 1024:
            input_image_path = os.path.join(directory, filename)
            output_image_path = os.path.join(directory, filename)
            compress_image(input_image_path, output_image_path, quality)
            print(f'Compressed: {filename}')

if __name__ == "__main__":
    quality = 85  # 设置压缩质量
    current_directory = '.'  # 当前文件夹
    batch_compress_images(current_directory, quality)
