import torch
from torchvision import transforms
from PIL import Image, UnidentifiedImageError
import io

# Automatically use GPU if available
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Image transformation for MobileNetV2
def get_transform():
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

# Load image from raw bytes (e.g. from Streamlit upload)
def load_image_from_bytes(byte_data):
    try:
        return Image.open(io.BytesIO(byte_data)).convert("RGB")
    except UnidentifiedImageError:
        raise ValueError("Uploaded file is not a valid image. Please upload a .jpg or .png file.")

# Apply softmax to model output
def softmax_probs(output_tensor):
    return torch.nn.functional.softmax(output_tensor, dim=1)
