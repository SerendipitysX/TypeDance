import io
from io import BytesIO
import base64
import numpy as np
import cv2
import os
from PIL import Image, ImageDraw, ImageFont
from colorthief import ColorThief
import openai
from keybert import KeyBERT
import svgtrace
from pathlib import Path
import convertapi
import requests
openai.api_key = "your key"

def img_to_svg_api(img_path, output_path):
    # output_path: svg path
    response = requests.post(
        'https://vectorizer.ai/api/v1/vectorize',
        files={'image': open(img_path, 'rb')},
        data={
            # TODO: Add more upload options here
        },
        headers={
            'Authorization':
            'Basic img_to_svg_api API key'
        },
    )
    if response.status_code == requests.codes.ok:
        # Save result
        with open(output_path, 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

def dataurl_to_pil(dataurl, output_path=None):
    image_data = dataurl.replace("data:image/png;base64,", '')
    if(len(image_data)%3 == 1): 
        image_data += "=="
    elif(len(image_data)%3 == 2): 
        image_data += "=" 
    binary_data = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(binary_data))
    return image

def pil_to_data_uri(pil_img):
    # Convert PIL image to bytes
    img_bytes = BytesIO()
    pil_img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    # Encode bytes as base64 string
    img_base64 = base64.b64encode(img_bytes).decode()

    # Create data URI
    data_uri = 'data:image/png;base64,' + img_base64

    # Create HTML string with image tag
    # html_str = f'<img src="{data_uri}">'

    return data_uri

def crop_element_from_RGBA(image, mask_single_FLAG= True):
    img_removal = np.array(image)
    imgray = cv2.cvtColor(img_removal, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 30, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 像素的边界
    if len(contours) == 1 or mask_single_FLAG == False:
        left, top, right, bottom = image.width, image.height, 0, 0 
        for x in range(image.width): 
            for y in range(image.height): 
                if image.getpixel((x, y))[3] != 0: 
                    left = min(left, x) 
                    top = min(top, y) 
                    right = max(right, x) 
                    bottom = max(bottom, y) 
        image = image.crop((left, top, right, bottom))
    else: # 最大的contour
        area_highest = 0
        for cntr in contours:
            x,y,w,h = cv2.boundingRect(cntr)
            if w*h > area_highest:   # find the biggest area 
                x_gen, y_gen, w_gen, h_total = x,y,w,h
                area_highest = w*h
        img_removal_correct = img_removal[y_gen:y_gen+h_total,x_gen:x_gen+w_gen]
        image = Image.fromarray(img_removal_correct).convert("RGBA")
    return image

def add_bg_color(img_rgba, color=[247, 246, 240]):
    image_array = np.array(img_rgba)
    alpha = image_array[:, :, 3]
    # white_array = np.ones_like(image_array) * color
    color_array = np.full_like(image_array[:, :, :3], color)

    image_array = np.where(np.expand_dims(alpha, axis=2) == 0, color_array, image_array[:, :, :3])

    # 打印处理后的数组
    image_rgb_r = Image.fromarray(image_array).convert("RGB")
    return image_rgb_r

def add_margin(background, img):
    
    w, h = img.size
    bg_wh, _ = background.size
    # print(h, w)
    max_value = max(h,w)
    if max_value-bg_wh>-10 or bg_wh - max_value > 100:
        if h>=w:
            ideal_h = bg_wh*0.9
            ideal_w = ideal_h * (w/h)
        if w>h:
            ideal_w = bg_wh*0.9
            ideal_h = ideal_w * (h/w)

    # if bg_wh - max_value > 100:
    #     # print("bg_wh - max_value > 100")
    #     if h>=w:
    #         ideal_h = bg_wh*0.9
    #         ideal_w = ideal_h * (w/h)
    #     if w>h:
    #         ideal_w = bg_wh*0.9
    #         ideal_h = ideal_w * (h/w)
        img = img.resize((int(ideal_w), int(ideal_h)))

    # print(ideal_w, ideal_h)
    # 计算居中位置
    x = (background.width - img.width) // 2
    y = (background.height - img.height) // 2

    # 将您的PIL对象居中粘贴到背景图像上
    background.paste(img, (x, y)) # 左上角的坐标
    return background

def add_margin_for_word(background, img):
    
    w, h = img.size
    bg_wh, _ = background.size
    # print(h, w)
    max_value = max(h,w)
    if max_value-bg_wh>-10 or bg_wh - max_value > 100:
        if h>=w:
            ideal_h = bg_wh*0.7
            ideal_w = ideal_h * (w/h)
        if w>h:
            ideal_w = bg_wh*0.7
            ideal_h = ideal_w * (h/w)
        img = img.resize((int(ideal_w), int(ideal_h)))

    # if bg_wh - max_value > 100:
    #     # print("bg_wh - max_value > 100")
    #     if h>=w:
    #         ideal_h = bg_wh*0.7
    #         ideal_w = ideal_h * (w/h)
    #     if w>h:
    #         ideal_w = bg_wh*0.7
    #         ideal_h = ideal_w * (h/w)

    # print(ideal_w, ideal_h)
    # 计算居中位置
    x = (background.width - img.width) // 2
    y = (background.height - img.height) // 2

    # 将您的PIL对象居中粘贴到背景图像上
    background.paste(img, (x, y)) # 左上角的坐标
    return background

def extract_shape(image_r, img_contour):
    # 得到边界 (left, top, right, bottom)
    border_tuple = get_rgba_border(img_contour) 
    # 新建画布 和边界一样大小
    bg = Image.new("RGBA", (border_tuple[2]-border_tuple[0], border_tuple[3]-border_tuple[1]),  "#D7D8C9")
    # 贴合上去 alpha
    # blank_rgba_arr = np.array(blank_rgba)
    # cv2.drawContours(blank_rgba_arr, contours_g, -1, (79, 79, 79), thickness=8)
    # blank_rgba_r = Image.fromarray(blank_rgba_arr).convert("RGB")
    # image_r = blank_rgba_r.crop(input_box)
    img_contour_border = img_contour.crop((border_tuple[0], border_tuple[1], border_tuple[2], border_tuple[3]))
    image_r = Image.alpha_composite(bg, img_contour_border) # color_bar 放上面
    return image_r

def rgb_to_hex(rgb):
    hex_value = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
    return hex_value

def extract_color_palatte(image_test):
    color_thief = ColorThief(image_test)
    color_count=5
    palette = color_thief.get_palette(color_count=color_count)
    color_bar = Image.open("frontend/src/assets/generation/default/color_bar.png").convert("RGBA")
    color_bar_w , color_bar_h = color_bar.size
    gap_length = color_bar_w//color_count
    bg = Image.new("RGBA", color_bar.size, "white")
    for i in range(color_count):
        hex_value = rgb_to_hex(palette[i])
        # create rectangle image
        brush = ImageDraw.Draw(bg)  
        brush.rectangle([(i*gap_length,0), ((i+1)*gap_length, color_bar_h)], fill=hex_value)
    # print(bg.size, color_bar.size)
    final_palette = Image.alpha_composite(bg,color_bar) # color_bar 放上面
    # final_palette = bg
    return final_palette

def extract_keyword(prompt):
    kw_model = KeyBERT(model='all-mpnet-base-v2')
    keywords = kw_model.extract_keywords(prompt,
                                        keyphrase_ngram_range=(1,1),
                                        stop_words='english',
                                        highlight=False,
                                        top_n=3)
    keywords_list = list(dict(keywords).keys())
    return keywords_list[0]

def add_text_to_img(keyword):
    # 加载字体和图像
    mf = ImageFont.truetype('frontend/src/assets/fonts/en/IBMPlexSans.ttf', 80)
    img_defalt_semantic = Image.open("frontend/src/assets/generation/default/semantic.png")
    brush = ImageDraw.Draw(img_defalt_semantic)
    # 要绘制的文本
    # 计算文本的宽度
    text_width, _ = brush.textsize(keyword, font=mf)
    # 计算文本应该放置的位置
    text_x = img_defalt_semantic.width - text_width - 30  # 图像宽度减去文本宽度再减去30px的距离
    # 绘制文本
    brush.text((text_x, 90), keyword, fill=(70, 70, 70), font=mf)
    return img_defalt_semantic

def get_rgba_border(img_rgba):
    left, top, right, bottom = img_rgba.width, img_rgba.height, 0, 0 
    for x in range(img_rgba.width): 
        for y in range(img_rgba.height): 
            if img_rgba.getpixel((x, y))[3] != 0: 
                left = min(left, x) 
                top = min(top, y) 
                right = max(right, x) 
                bottom = max(bottom, y) 
    return (left, top, right, bottom)

def get_rgb_border(img_rgb): 
    # 只能处理word，假设背景全白哦
    left, top, right, bottom = img_rgb.width, img_rgb.height, 0, 0  
    for x in range(img_rgb.width):  
        for y in range(img_rgb.height):  
            if img_rgb.getpixel((x, y)) != (255, 255, 255):  
                left = min(left, x)  
                top = min(top, y)  
                right = max(right, x)  
                bottom = max(bottom, y)  
    return (left, top, right, bottom)

# 得到image_word
def get_word_img(image):
    border_tuple = get_rgba_border(image)
    image_white = add_bg_color(image, [255,255,255])
    image_white = image_white.crop((border_tuple[0], border_tuple[1], border_tuple[2], border_tuple[3])).convert("RGB")
    bg = Image.new("RGB", (512, 512), "white")
    image_word = add_margin_for_word(bg, image_white)
    return image_word

# 横轴拉伸，最后还是512，512
def scale_image(init_image):
    # init_image = Image.open("check/img_word.png").convert("RGB").resize((512, 512))
    border_tuple = get_rgb_border(init_image)
    width = border_tuple[2] - border_tuple[0]
    height = border_tuple[3] - border_tuple[1]
    if width < 250: 
        scale = 300/width
        target_width = int(512*scale)
        scale_img = init_image.resize((target_width, 512))
        scale_img_r = scale_img.crop(((target_width/2-256), 0, (target_width/2+256), 512))
        return scale_img_r, target_width
    else:
        return scale_img_r

def clear_folder():
        main_folder = "C:/Users/user/A-project/TypeDance/"
        folder_path = ["check/first_generation", "check/second_generation"]  # 文件夹路径

        # 遍历文件夹中的所有文件并删除
        for i in range(len(folder_path)):
            for filename in os.listdir(main_folder+folder_path[i]):
                file_path = os.path.join(main_folder, folder_path[i], filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")

def find_max_contour(contours):
    if len(contours)>1:
            max_area = 0
            max_contour = None
            for contour in contours:
                area = cv2.contourArea(contour)
                if area > max_area:
                    max_area = area
                    max_contour = contour
    else:
        max_contour = contours[0]
    return max_contour

# ======== 要处理的word转成svg ========
def word_to_svg(image_pil):
	# 这里的svg只是string
	# step1： 截取一下word，不能边框太大了
	(left, top, right, bottom) = get_rgb_border(image_pil)
	image_pil = image_pil.crop((left-10, top-10, right+10, bottom+10)).resize((512,512))
    # image_pil = image_pil.crop((left, top, right, bottom)).resize((512,512))

	# # step2： word_pil->svg
	svg_path = svgtrace.skimageTrace(image_pil)
	space_index = svg_path.find(" ")
	svg_path = svg_path[:space_index] + ' ' + 'id="svg-element"' + svg_path[space_index:]
	Path(f"svgTry.svg").write_text(
			svg_path, encoding="utf-8"
		)
	return svg_path

# ======== 找到contour ========
def find_continuous_contour(image_pil):
    # step1: 给img_mask换背景
    image_pil = add_bg_color(image_pil, color=[0, 0, 0])
    # step2: 找最大的contour
    image = np.array(image_pil)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_contour = find_max_contour(contours)
    # step3: crop iamge
    x, y, w, h = cv2.boundingRect(max_contour)
    image = image[y:y+h, x:x+w]
    image_pil = Image.fromarray(image)
    bg = Image.new("RGB", (512, 512), "black")
    image_pil = add_margin(bg, image_pil)
    # step2: 在crop之后的ima|ge上找最大的contour
    image = np.array(image_pil)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_contour = find_max_contour(contours)
    # step3: 近似contour（保证了只有一根contour）
    epsilon = 0.005 * cv2.arcLength(max_contour, True)
    contours = [cv2.approxPolyDP(max_contour, epsilon, True)]

    # # 绘制并显示结果
    # cv2.drawContours(image, contours, -1, (0, 255, 0), thickness=5)
    # # cv2.drawContours(image, max_contour, -1, (0, 0, 255), thickness=10)
    # img_r = Image.fromarray(image)
    # img_r
    return contours

# ======== 在contour上sample出点来 ========
def sample_from_contours(contours):
    # step1：预处理contours数组
    contours_array = [np.array(contour) for contour in contours]
    result = np.vstack(contours_array)
    reshaped_array = result.reshape(result.shape[0], 2)

    # step2：生成等间距的索引
    indices = np.linspace(0, reshaped_array.shape[0] - 1, num=18, dtype=int)
    indices = indices[:-1]

    # step3：通过索引获取相应的点
    sampled_points = reshaped_array[indices]

    # # step4：可视化
    # for point in sampled_points:
    #     cv2.circle(image, point, 3, (255, 0, 0), -1)
    # img_r = Image.fromarray(image)

    # step5：找到最左边的点（x最小）的位置，之前的都往后排，像队列一样
    # 为了保证第一个字母在左边，且没有旋转太多
    min_x = np.min(sampled_points[:,0])
    min_x_idx = np.argmin(sampled_points[:,0])
    sample_list = []
    for i in range(4):
        if i==0:
            new_sampled_points = np.vstack([sampled_points[min_x_idx:], sampled_points[:min_x_idx]])
        if i==1:
            new_sampled_points = np.vstack([sampled_points[min_x_idx-1:], sampled_points[:min_x_idx+i]])
        if i==2:
            new_sampled_points = np.vstack([sampled_points[min_x_idx+1:], sampled_points[:min_x_idx-1]])
        if i==3:
            new_sampled_points = np.vstack([sampled_points[min_x_idx-2:], sampled_points[:min_x_idx-2]])
        sampled_result = str(new_sampled_points.tolist())
        sample_list.append(sampled_result)
    return sample_list
