import os
import ddddocr                       # 导入 ddddocr

# import ddddocr

# ocr = ddddocr.DdddOcr(det=False, ocr=False, 
#                       import_onnx_path="/Users/bytedance/Desktop/rubbish/common.onnx", 
#                       charsets_path="/Users/bytedance/Desktop/rubbish/common.onnx")

# with open('./img.jgp', 'rb') as f:
#     image_bytes = f.read()

# res = ocr.classification(image_bytes)
# print(res)


# current_dir = os.path.dirname(os.path.abspath(__file__))
# img_path = os.path.join(current_dir, "img.jpg")
# ocr = ddddocr.DdddOcr()              # 实例化
# with open(img_path, 'rb') as f:      # 打开图片
#     img_bytes = f.read()             # 读取图片
# res = ocr.classification(img_bytes)  # 识别
# print(res)

ocr = ddddocr.DdddOcr()              # 实例化

def ocr_img(img_bytes):
    res = ocr.classification(img_bytes)  # 识别
    print(res)
    if res == '':
        return ''
    return res
