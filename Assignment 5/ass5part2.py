
import json
from PIL import Image
from transformers import BlipForQuestionAnswering, AutoProcessor
import pandas as pd
import os


JSON_PATH = "filtered_questions.json"  
IMAGES_FOLDER = "images_updated"      


with open(JSON_PATH, "r") as f:
    data = json.load(f)


print(f"Loaded {len(data)} question-answer-image triples.")

model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")
processor = AutoProcessor.from_pretrained("Salesforce/blip-vqa-base")


import matplotlib.pyplot as plt

for i in range(2):  
    question, answer, idx = data[i]
    img_path = os.path.join(IMAGES_FOLDER, f"{idx}.png")
    img = Image.open(img_path).convert("RGB")
    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Q: {question}\nA: {answer}")
    plt.show()


def vqa(question, image):
    """Answer a question about an image using BLIP."""
    inputs = processor(image, question, return_tensors="pt")
    out = model.generate(**inputs)
    answer = processor.decode(out[0], skip_special_tokens=True)
    return answer


results = []
for q, gt_answer, idx in data:
    img_path = os.path.join(IMAGES_FOLDER, f"{idx}.png")
    img = Image.open(img_path).convert("RGB")
    pred_answer = vqa(q, img)
    results.append({
        "image_index": idx,
        "question": q,
        "ground_truth": gt_answer,
        "predicted": pred_answer
    })

pd.DataFrame(results).to_csv("vqa_results.csv", index=False)
with open("vqa_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Saved answers to vqa_results.csv and vqa_results.json.")

correct = 0
total = min(30, len(results))
print("\nFirst 30 Q&A results (compare manually for accuracy):\n")
for i in range(total):
    r = results[i]
    print(f"Q: {r['question']}")
    print(f"GT: {r['ground_truth']}")
    print(f"PRED: {r['predicted']}\n")
    
    if r['predicted'].strip().lower() == r['ground_truth'].strip().lower():
        correct += 1

accuracy = correct / total
print(f"Accuracy for first {total} questions (exact match): {accuracy:.2%}")


