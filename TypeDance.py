from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import torch
from pathlib import Path
from PIL import Image
import cv2
from diffusers import DiffusionPipeline,StableDiffusionDepth2ImgPipeline,StableDiffusionImg2ImgPipeline,StableDiffusionPipeline
from brainstorm import get_answer, get_dict_from_answer
from image_segment import get_img_embedding, highlight_mask, mask_to_image, img_word_to_canvas
from segment_anything import sam_model_registry, SamPredictor
from clip_interrogator import Config, Interrogator
from utils import *
from generate import Generation
from generate import Generation, Feedback, Refine
from transformers import CLIPProcessor, CLIPModel


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/brainstorm',methods=['GET', 'POST'])
def brainstorm():
    data = request.get_json()
    user_prompt = data["user_prompt"]
    answer = get_answer(user_prompt)
    print(answer)
    string = answer["content"]
    concept_dict = get_dict_from_answer(string)
    # concept_dict = {"1. Giant Panda": "The giant panda is not only a beloved symbol of Chengdu, but it is also native to the region. Using the image of a playful and adorable giant panda in the logo can represent Chengdu's connection to nature and its commitment to wildlife conservation.",
# "2. Sichuan Cuisine": "Chengdu is renowned for its delicious and spicy Sichuan cuisine. Using elements like chili peppers, hot pot, or a pair of chopsticks can symbolize the city's vibrant food culture and its reputation as a food lover's paradise.",
# "3. Bamboo Forest": "Chengdu is surrounded by beautiful bamboo forests, known for their tranquility and elegance. Incorporating the image of bamboo stalks or leaves in the logo can represent Chengdu's connection to nature, its traditional arts, and its commitment to preserving green spaces.",
# "4. Mask Changing": "Sichuan Opera is famous for its unique art of 'mask changing,' where performers change masks in the blink of an eye using various techniques. Including a mask or a theatrical mask-inspired design element in the logo can symbolize Chengdu's rich cultural heritage, its vibrant performing arts scene, and its tradition of innovation.",
# "5. Jinsha Site Museum": "The Jinsha Site Museum is an archaeological site in Chengdu that preserves the remains of the ancient Shu civilization. Incorporating elements such as ancient artifacts, a stylized symbol of archaeological discoveries, or the museum's iconic architecture can represent Chengdu's historical significance, its rich heritage, and its commitment to preserving and promoting its cultural roots."}
    return jsonify(concept_dict)

# box
# @app.route('/image_segment',methods=['GET', 'POST'])
# def image_view():
#     data = request.get_json()
#     input_box = data["box"]
#     image_url = data["image_url"]
#     mode = data["mode"]
#     image = dataurl_to_pil(image_url, output_path=None).convert("RGB")
#     print(image.size)
#     image.save("from_interface.png")
#     if mode == "image":
#         input_box = np.array([input_box[0]*(image.size[1]/180), input_box[1]*(image.size[1]/180), input_box[2]*(image.size[1]/180), input_box[3]*(image.size[1]/180)])
#         print(input_box)
#     if mode == "word":
#         input_box = np.array([input_box[0], input_box[1], input_box[2], input_box[3]])
#     image = np.array(image)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     mask = get_img_embedding(image, input_box)
#     image_r, contours_g = highlight_mask(mask, image, mode)
#     image_r.save("check/img_segment.png")

#     if mode == "image":
#         # ===== get design prior ====
#         # shape
#         img_defalt_bg = Image.open('frontend/src/assets/generation/default/extract-feature-bg.png')	
#         shape_rectagle = extract_shape(image_r, contours_g, input_box)
#         shape_image = add_margin(img_defalt_bg, shape_rectagle)
#         # 圆角rgba贴上去是黑色
#         shape_image_rgb = add_bg_color(shape_image, color=[247, 246, 240])
#         # paste to img_defalt_shape
#         img_defalt_shape = Image.open('frontend/src/assets/generation/default/shape.png')
#         shape_image_resize = shape_image_rgb.resize((175,175))
#         img_defalt_shape.paste(shape_image_resize, (535, 18))
#         img_defalt_shape.save("check/img_shape.png")

#         # shape
#         color_palette = extract_color_palatte(image_r)
#         img_defalt_color = Image.open("frontend/src/assets/generation/default/color.png")
#         img_defalt_color.paste(color_palette, (215, 150))
#         img_defalt_color.save("check/img_color.png")

#         return {"img": pil_to_data_uri(image_r), "shape":pil_to_data_uri(img_defalt_shape),
#                 "color":pil_to_data_uri(img_defalt_color)}

#     if mode == "word":
#         return pil_to_data_uri(image_r)

# click
@app.route('/image_segment',methods=['GET', 'POST'])
def image_view():
    data = request.get_json()
    image_url = data["image_url"]
    mode = data["mode"]
    image = dataurl_to_pil(image_url, output_path=None).convert("RGB")
    image.save("check/from_interface.png")
    if mode == "image":
        # input_box = np.array([input_box[0]*(image.size[1]/180), input_box[1]*(image.size[1]/180), input_box[2]*(image.size[1]/180), input_box[3]*(image.size[1]/180)])
        input_points = np.array(data["points"])*(image.size[1]/180)
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mask = get_img_embedding(image, input_points, mode)
        img_mask = mask_to_image(mask, image)
        img_mask.save("check/img_mask.png")

        # highlight
        image_r, contours_g = highlight_mask(mask, image, mode)
        image_r.save("check/img_segment.png")

        ## 找contour为了shape
        blank_rgba = Image.new("RGBA", image_r.size, (0,0,0,0))
        blank_rgba_arr = np.array(blank_rgba)
        ## 找contour里面最大的那个
        max_contour = find_max_contour(contours_g) # 有不连续线段
        # img_mask = add_bg_color(img_mask, color=[0, 0, 0])
        # image = np.array(img_mask)
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
        # contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # max_contour = find_max_contour(contours)
        cv2.drawContours(blank_rgba_arr, max_contour, -1, (79, 79, 79, 255), thickness=8)
        img_contour = Image.fromarray(blank_rgba_arr).convert("RGBA")
        img_contour = crop_element_from_RGBA(img_contour, mask_single_FLAG= False)
        # 存一下图片好debug
        img_contour.save("check/img_segment_contour.png")

    if mode == "word":
        input_boxes = data["box"]
        print(input_boxes)
        if isinstance(input_boxes[0], list):
            print("--ADD SELECTION--")
            mask_merge = np.zeros((300,464), dtype=bool)
            image = np.array(image)
            for input_box in input_boxes:
                input_box = np.array([input_box[0], input_box[1], input_box[2], input_box[3]])
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                mask = get_img_embedding(image, input_box, mode)
                mask_merge = np.bitwise_or(mask_merge, mask)
                img_mask = mask_to_image(mask_merge, image)
                img_mask.save("check/img_mask_word.png")
                img_word = get_word_img(img_mask)
                img_word.save("check/img_word.png")
                # highlight
                image_r, contours_g = highlight_mask(mask_merge, image, mode)
                image_r.save("check/img_segment.png")
            # SVG 
            # reverted_word, _ = img_word_to_canvas(mask_merge, image, mode)
            # reverted_word.save("check/reverted_word.png")
            # img_to_svg_api("check/reverted_word.png", "frontend/src/assets/canvas/word.svg")

        else: 
            input_box = input_boxes
            input_box = np.array([input_box[0], input_box[1], input_box[2], input_box[3]])
            image = np.array(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            mask = get_img_embedding(image, input_box, mode)
            img_mask = mask_to_image(mask, image)
            img_mask.save("check/img_mask_word.png")
            img_word = get_word_img(img_mask)
            img_word.save("check/img_word.png")
            # highlight
            image_r, contours_g = highlight_mask(mask, image, mode)
            image_r.save("check/img_segment.png")
            # SVG 
            # reverted_word, _ = img_word_to_canvas(mask, image, mode)
            # reverted_word.save("check/reverted_word.png")
            # img_to_svg_api("check/reverted_word.png", "frontend/src/assets/canvas/word.svg")

    return pil_to_data_uri(image_r)


@app.route('/image_extract',methods=['GET', 'POST'])
def image_extract():
    image_r = Image.open("check/img_segment.png")
    img_contour = Image.open("check/img_segment_contour.png").convert("RGBA")
    img_mask = Image.open("check/img_mask.png").convert("RGBA")
    # =================== shape =========================
    img_defalt_bg = Image.open('frontend/src/assets/generation/default/extract-feature-bg.png')	
    shape_rectagle = extract_shape(image_r, img_contour)
    shape_image = add_margin(img_defalt_bg, shape_rectagle)
    # 圆角rgba贴上去是黑色
    shape_image_rgb = add_bg_color(shape_image, color=[247, 246, 240])
    # paste to img_defalt_shape
    img_defalt_shape = Image.open('frontend/src/assets/generation/default/shape.png')
    shape_image_resize = shape_image_rgb.resize((175,175))
    img_defalt_shape.paste(shape_image_resize, (535, 18))
    img_defalt_shape.save("check/img_shape.png")

    # =================== color =========================
    color_palette = extract_color_palatte(img_mask)
    img_defalt_color = Image.open("frontend/src/assets/generation/default/color.png")
    img_defalt_color.paste(color_palette, (215, 150))
    img_defalt_color.save("check/img_color.png")

    # ================= semantics =======================
    image_add_bg = add_bg_color(img_mask, color=[255, 255, 255])
    # image 2 prompt
    # clip-interrogator
    config = Config(clip_model_name="ViT-L-14/openai")
    ci = Interrogator(config)
    prompt = ci.interrogate_fast(image_add_bg)
    print(prompt)
    # obtain the keyword
    sentance = prompt.split(",")[0]
    keyword = extract_keyword(sentance)
    img_defalt_semantic = add_text_to_img(keyword)
    img_defalt_semantic.save("check/img_semantic.png")

    # ================= prepare material for wrap ================= 
    img_word = Image.open("check/img_word.png").convert("RGB")
    svg_string = word_to_svg(img_word)
    Path(f"frontend/src/assets/generation/shape_wrap/svgTry.svg").write_text(
			svg_string, encoding="utf-8"
		)
    contours = find_continuous_contour(img_mask)
    sampled_points = sample_from_contours(contours)

    return {"shape":pil_to_data_uri(img_defalt_shape),
            "color":pil_to_data_uri(img_defalt_color),
            "semantic":pil_to_data_uri(img_defalt_semantic),
            "semantic_prompt": prompt,
            "sampled_points": sampled_points}


@app.route('/show_info',methods=['GET', 'POST'])
def show_info():
    img_word = Image.open("check/img_word.png").convert("RGB")
    img_mask = Image.open("check/img_mask.png").convert("RGBA")
    image_add_bg = add_bg_color(img_mask, color=[255, 255, 255])
    return {"word": pil_to_data_uri(img_word), "img": pil_to_data_uri(image_add_bg)}


@app.route('/generate',methods=['GET', 'POST'])
def image_generate():
    data = request.get_json()
    prompt = data["prompt"]
    num_to_generate = data["num_to_generate"]
    strength = float(data["strength"])
    semantic_prompt = data["semantic_prompt"]
    bool_list = data["generate-option"]
    # previous_mode = data["previous_mode"]
    # previous_img = data["previous_img"]
    FEEDBACK_FLAG = False
    # if len(previous_mode) !=0:
    #     FEEDBACK_FLAG = True
    #     print(previous_mode)
    #     previous_img_list = []
    #     for img in previous_img:
    #         img = dataurl_to_pil(img, output_path=None)
    #         previous_img_list.append(img)
    option_list = [option for index, option in enumerate(["semantic", "color", "shape"]) if bool_list[index]]
    if "shape" in option_list:
        wrap_svg_string = data["wrap_svg"]
        for i in range(4):
            Path('check/wrap/wrap_'+str(i)+'.svg').write_text(
                wrap_svg_string[i], encoding="utf-8"
            )

    print("prompt", prompt)
    print("semantic_prompt", semantic_prompt)
    print(option_list)

    img_word = Image.open("check/img_word.png").convert("RGB") # 已经512，512
    img_image = Image.open("check/img_segment.png").convert("RGB")
    img_mask = Image.open("check/img_mask.png").convert("RGBA")
    image_add_bg = add_bg_color(img_mask, color=[255, 255, 255])

    # if not FEEDBACK_FLAG or : # from scratch
    generationOperator = Generation()
    img_list, mode_list, alt = generationOperator(img_word, img_mask, prompt, semantic_prompt, num_to_generate, strength, option_list)
    # else:
    #     feedbackOperator = Feedback(img_word, img_mask, prompt, semantic_prompt, num_to_generate, strength, option_list, previous_mode, previous_img_list)




    return {"gallery": [pil_to_data_uri(img) for img in img_list], 
            "word": pil_to_data_uri(img_word), 
            "img": pil_to_data_uri(image_add_bg),
            "mode": mode_list,
            "alt": alt}

@app.route('/convert_to_svg',methods=['GET', 'POST'])
def convert_to_SVG():
    data = request.get_json()
    dataurl = data["data"]["src"]
    image = dataurl_to_pil(dataurl, output_path=None).convert("RGB")
    image.save("check/from_canvas.png")
    img_to_svg_api("check/from_canvas.png", "frontend/src/assets/canvas/image.svg")
    return jsonify("send svg")

@app.route('/evaluate_element',methods=['GET', 'POST'])
def evaluate_img():
    data = request.get_json()
    dataurl = data["data"]
    prompt = data["alt"]
    prompt = prompt.replace("_", " ")
    image = dataurl_to_pil(dataurl, output_path=None).convert("RGB")
    image.save("check/evaluate_img.png")

    model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")#.cuda()
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")
    inputs = processor(text=["A word or text", "An illustration or photo"], images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities
    max_value, max_index = torch.max(probs, dim=1)
    if max_index == 0:
        print("more like typeface")
        origin_score = max_value.item()
        final_score = -(origin_score-0.5)*2
    if max_index == 1:
        print("more like imagery")
        origin_score = max_value.item()
        final_score = (origin_score-0.5)*2
    print(final_score)
    result_score = round(final_score * 20) / 20
    result_score = 0.90 if result_score>0.90 else result_score
    result_score = -0.90 if result_score<-0.90 else result_score
    return jsonify({"result_score": result_score})

@app.route('/refine_element',methods=['GET', 'POST'])
def refine_img():
    data = request.get_json()
    print(data)
    strength = float(data["value"])
    anchor = data["anchor"]
    alt = data["alt"]

    RefineOperator = Refine()
    img = RefineOperator(strength, anchor, alt)

    return {"dataURL": pil_to_data_uri(img)} 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=88, debug=True)