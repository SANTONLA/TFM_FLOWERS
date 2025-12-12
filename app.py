from fastai.vision.all import *
from flask import Flask, request, jsonify
from pathlib import Path
import gdown

# Inicializa Flask
app = Flask(__name__)

# Descargar el modelo desde Google Drive (enlace directo)
file_id = '1JcPZfetOGB1kIffK798dFOLti_u8SKav'  # ID del archivo en Drive
url = f'https://drive.google.com/uc?id={file_id}'
output = 'flowers_model.pkl'

# Solo descargar si no existe
if not Path(output).exists():
    gdown.download(url, output, quiet=False)

# Cargar el modelo exportado
learn = load_learner(Path(output))

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


