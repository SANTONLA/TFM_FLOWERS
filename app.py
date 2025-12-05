from flask import Flask, request, jsonify, render_template
from PIL import Image
import torch
import torchvision.transforms as transforms
import os

# Inicializa la app Flask
app = Flask(__name__)

# Definir las clases
classes = ['roses', 'tulips', 'daffodils', 'sunflowers']

# Transformación de la imagen (ajusta según tu entrenamiento)
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # tamaño que usaste al entrenar
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  # valores típicos de ImageNet
                         std=[0.229, 0.224, 0.225])
])

# Cargar el modelo entrenado
model_path = 'model_flowers.pth'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Cargar el modelo
model = torch.load(model_path, map_location=device)
model.eval()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No se subió ninguna imagen'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Archivo vacío'}), 400

    try:
        img = Image.open(file.stream).convert('RGB')
        img_tensor = transform(img).unsqueeze(0).to(device)  # Añadir dimensión batch

        # Predicción
        with torch.no_grad():
            outputs = model(img_tensor)
            _, predicted = torch.max(outputs, 1)
            prediction = classes[predicted.item()]

        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
