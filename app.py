from fastai.vision.all import load_learner, PILImage
from flask import Flask, request, jsonify
from pathlib import Path

app = Flask(__name__)

# Ruta al modelo exportado
model_path = Path("flowers_model.pkl")  # Ajusta si lo tienes en otra carpeta
learn = load_learner(model_path)  # Carga el modelo Fastai

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']
        img = PILImage.create(file)  # Fastai se encarga del preprocesamiento

        # Predicción
        pred_class, pred_idx, probs = learn.predict(img)

        return jsonify({
            'prediction': str(pred_class),
            'probability': float(probs[pred_idx])
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    # Importante: host='0.0.0.0' para que se pueda acceder desde otras máquinas o contenedores
    app.run(host='0.0.0.0', port=5000, debug=True)




