from PIL import Image
from transformers import AutoTokenizer, AutoImageProcessor

# Load the image
image_path = "train_img/1_33.jpg"
image = Image.open(image_path)

# Define the model and tokenizer
model_name = "Multi Col. OCR.ipynb"
tokenizer_name = ""
model = AutoImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

# Preprocess the image
inputs = tokenizer(image, return_tensors="pt")
processed_inputs = model.preprocess(inputs)

# Print the preprocessed inputs
print(processed_inputs)
