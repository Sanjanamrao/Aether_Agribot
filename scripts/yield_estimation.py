import cv2
import numpy as np
from PIL import Image
import io

def count_plants_from_image_pil(pil_img):
    # Convert to OpenCV
    cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)
    # threshold for greenish colors (tweak depending on images)
    lower = np.array([25, 40, 40])
    upper = np.array([95, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    # clean up
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # filter by area
    plant_cnt = 0
    for c in contours:
        area = cv2.contourArea(c)
        if area > 80:  # threshold depends on image size
            plant_cnt += 1
    return plant_cnt, mask

def estimate_yield(count, avg_weight_per_plant_kg=0.05):
    # Simple estimate: count * avg_weight
    return count * avg_weight_per_plant_kg

def run_demo(uploaded_file=None, avg_weight=0.05):
    if uploaded_file is None:
        return {'msg': 'Upload an image for yield estimation'}
    # load pil image
    if hasattr(uploaded_file, "read"):
        img = Image.open(io.BytesIO(uploaded_file.read())).convert("RGB")
    else:
        img = Image.open(uploaded_file).convert("RGB")
    cnt, mask = count_plants_from_image_pil(img)
    ye = estimate_yield(cnt, avg_weight_per_plant_kg=avg_weight)
    return {'count': int(cnt), 'yield_kg': float(ye), 'mask': mask}
