import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms, models
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from tqdm import tqdm

# Config
DATA_DIR = 'datasets/weeds'
MODEL_OUT = 'models/weed_detection.pt'
BATCH = 16
EPOCHS = 5
LR = 1e-3

# Transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Custom Dataset
class WeedDataset(Dataset):
    def __init__(self, img_dir, label_dir, transform=None):
        self.img_dir = img_dir
        self.label_dir = label_dir
        self.transform = transform
        self.img_list = [f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.png'))]

    def __len__(self):
        return len(self.img_list)

    def __getitem__(self, idx):
        img_name = self.img_list[idx]
        img_path = os.path.join(self.img_dir, img_name)
        label_path = os.path.join(self.label_dir, os.path.splitext(img_name)[0] + '.txt')

        image = Image.open(img_path).convert("RGB")
        label = 0  # default: crop

        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) > 0:
                        class_id = int(parts[0])
                        if class_id == 1:  # weed detected
                            label = 1
                            break

        if self.transform:
            image = self.transform(image)

        return image, label

# Load datasets
train_ds = WeedDataset(
    img_dir=os.path.join(DATA_DIR, 'train', 'images'),
    label_dir=os.path.join(DATA_DIR, 'train', 'labels'),
    transform=transform
)

val_ds = WeedDataset(
    img_dir=os.path.join(DATA_DIR, 'valid', 'images'),
    label_dir=os.path.join(DATA_DIR, 'valid', 'labels'),
    transform=transform
)

train_loader = DataLoader(train_ds, batch_size=BATCH, shuffle=True, num_workers=0)
val_loader = DataLoader(val_ds, batch_size=BATCH, shuffle=False, num_workers=0)

# Device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Model
model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
num_ftrs = model.classifier[1].in_features
model.classifier[1] = nn.Linear(num_ftrs, 2)  # crop vs weed
model = model.to(device)

# Loss & Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

# Training loop
def train():
    for epoch in range(EPOCHS):
        model.train()
        total_loss = 0.0
        for imgs, labels in tqdm(train_loader, desc=f"Train Epoch {epoch+1}"):
            imgs, labels = imgs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1} - Train Loss: {total_loss / len(train_loader):.4f}")

        # Validation
        model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for imgs, labels in val_loader:
                imgs, labels = imgs.to(device), labels.to(device)
                outputs = model(imgs)
                _, preds = torch.max(outputs, 1)
                correct += (preds == labels).sum().item()
                total += labels.size(0)
        accuracy = correct / total
        print(f"Validation Accuracy: {accuracy * 100:.2f}%")

    # Save model
    os.makedirs(os.path.dirname(MODEL_OUT), exist_ok=True)
    torch.save(model.state_dict(), MODEL_OUT)
    print(f"✅ Model saved to {MODEL_OUT}")

if __name__ == "__main__":
    train()
