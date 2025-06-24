
import torch
from PIL import Image
import requests
from io import BytesIO
from transformers import CLIPProcessor, CLIPModel
import numpy as np
import matplotlib.pyplot as plt

IMAGE_URLS = [
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1519985176271-adb1088fa94c?auto=format&fit=crop&w=800&q=80"
]



device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")

images = []
for url in IMAGE_URLS:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")
    images.append(img)

inputs = processor(images=images, return_tensors="pt", padding=True)
image_features = model.get_image_features(**{k: v.to(device) for k, v in inputs.items()})
image_features = image_features / image_features.norm(dim=-1, keepdim=True)  

query = input("Enter which image are you looking for: ")

text_inputs = processor(text=[query], return_tensors="pt", padding=True)
text_features = model.get_text_features(**{k: v.to(device) for k, v in text_inputs.items()})
text_features = text_features / text_features.norm(dim=-1, keepdim=True)  


similarities = (image_features @ text_features.T).squeeze(1)  


best_match_idx = similarities.argmax().item()
best_image = images[best_match_idx]
plt.imshow(best_image)
plt.axis('off')
plt.title(f"Best match for: '{query}'")
plt.show()


print("Similarity scores:", similarities.cpu().numpy())
print("Best matching image URL:", IMAGE_URLS[best_match_idx])
