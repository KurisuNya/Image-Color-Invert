import os
from tqdm import tqdm
from PIL import Image, ImageOps

if __name__ == "__main__":
    # 设置根目录
    root_path = "./"
    # 遍历目录下文件
    for root, dirs, files in os.walk(root_path, topdown=False):
        # 文件夹不为空
        if files != []:
            # 命令行进度条
            for name in tqdm(files):
                file_path = os.path.join(root, name)
                try:
                    # 图像处理，并保存为原文件
                    image = Image.open(file_path)
                    invert_image = ImageOps.invert(image)
                    os.remove(file_path)
                    invert_image.save(file_path)
                except:
                    # 异常处理（文件无法识别为图像）
                    pass
