from fastai.vision.all import *
from flask import Flask, request, jsonify
from pathlib import Path

# Inicializa Flask
app = Flask(__name__)

# Cargar el modelo exportado
model_path = Path("flowers_model.pkl")  # Ajusta la ruta si hace falta
learn = load_learner(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        img = PILImage.create(file)  # Fastai se encarga del preprocesamiento

        # Obtener predicción
        pred_class, pred_idx, probs = learn.predict(img)

        return jsonify({
            'prediction': str(pred_class),
            'probability': float(probs[pred_idx])
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

