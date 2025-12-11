from flask import Flask, request, jsonify
from PIL import Image
import io
import torch
from torchvision import transforms

# Inicializa Flask
app = Flask(__name__)

# Carga tu modelo
model = torch.load('model.pth', map_location='cpu')
model.eval()

# Clases
classes = ['Rosa', 'Tulipán', 'Narciso', 'Girasol']

# Transformación de imagen (ajusta según tu modelo)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    img = Image.open(file).convert('RGB')
    img = transform(img).unsqueeze(0)  # añade batch dimension
    
    with torch.no_grad():
        output = model(img)
        _, pred = torch.max(output, 1)
        class_name = classes[pred.item()]

    return jsonify({'prediction': class_name})

if __name__ == '__main__':
    app.run(debug=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
