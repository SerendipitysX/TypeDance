import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from segment_anything import sam_model_registry, SamPredictor


# =========== set up model ===========
sam_checkpoint = "models/sam_vit_h_4b8939.pth"
model_type = "vit_h"

device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

predictor = SamPredictor(sam)

# =========== some function ===========
def get_img_embedding(image, input, mode):
    """get image embedding"""
    predictor.set_image(image)
    if mode == "word":
        masks, _, _ = predictor.predict(
            point_coords=None,
            point_labels=None,
            box=input[None, :],
            multimask_output=False,
        )
    if mode == "image":
        if len(input) == 1:
            input_label = np.array([1])
            masks, scores, logits = predictor.predict(
                point_coords=input,
                point_labels=input_label,
                multimask_output=False,
            )
        else:
            # 第一个point先分割出来开（要分割好）
            input_first = np.array([input[0]])
            input_label = np.array([1])
            masks, scores, logits = predictor.predict(
                point_coords=input_first,
                point_labels=input_label,
                multimask_output=False,
            )
            # 全部points
            input_label = np.array([1]*len(input))
            mask_input = logits[np.argmax(scores), :, :]  # Choose the model's best mask
            masks, _, _ = predictor.predict(
                point_coords=input,
                point_labels=input_label,
                mask_input=mask_input[None, :, :],
                multimask_output=False,
            )
    return masks[0]


def highlight_mask(mask, image, mode):
    """highlight mask in image"""
    mask = mask.astype(np.uint8)
    # mask_image = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    # gray = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY)
    # ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    # 找contour
    contours_g, hireachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if mode == "image":
        # 画contour
        cv2.drawContours(image, contours_g, -1, (255, 255, 255), thickness=5)
        # image 高亮contour区域
    image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    image_rgba[:,:,3] = mask
    image_rgba[mask==1, 3] = 255
    image_rgba[mask==0, 3] = 75
    image_r = Image.fromarray(image_rgba)
    return image_r, contours_g

def img_word_to_canvas(mask, image, mode):
    mask = mask.astype(np.uint8)
    contours_g, hireachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    image_rgba[:,:,3] = mask
    image_rgba[mask==1, 3] = 0
    image_rgba[mask==0, 3] = 255
    image_r = Image.fromarray(image_rgba)
    return image_r, contours_g

def mask_to_image(mask, image):
    """highlight mask in image"""
    mask = mask.astype(np.uint8)
    # 找contour
    image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    image_rgba[:,:,3] = mask
    image_rgba[mask==1, 3] = 255
    image_rgba[mask==0, 3] = 0
    image_r = Image.fromarray(image_rgba)
    return image_r

# =========== try it ===========
# image_path = 'truck.jpg'
# image = cv2.imread(image_path)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# input_box = np.array([425, 600, 700, 875])
# mask = get_img_embedding(image, input_box)
# image_r = highlight_mask(mask, image)
# image_r.save("see.png")
