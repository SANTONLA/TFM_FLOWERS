from fastai.vision.all import *
from flask import Flask, request, jsonify
from pathlib import Path
import gdown

# Inicializa Flask
app = Flask(__name__)

# ------------------------------
# Descargar el modelo desde Google Drive
# ------------------------------
file_id = '1RVb_OQxe7frWNzfhEq-uZyG_YndC7ZAm'
url = f'https://drive.google.com/uc?id={file_id}'
output = 'flowers_model.pkl'

# Solo descarga si el archivo no existe
if not Path(output).exists():
    print("Descargando modelo desde Google Drive...")
    gdown.download(url, output, quiet=False)
else:
    print("El modelo ya existe localmente.")

# Cargar el modelo exportado de Fastai
model_path = Path(output)
learn = load_learner(model_path)

# ------------------------------
# Ruta de predicción
# ------------------------------
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

# ------------------------------
# Ejecutar la app
# ------------------------------
if __name__ == '__main__':
    app.run(debug=True)



