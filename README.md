# TFM_FLOWERS

# 🌸 Flowers Dataset 🌼

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0-brightgreen.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange.svg)

## 📋 Descripción

El dataset **Flowers** contiene una colección de imágenes de diversas especies de flores, ideal para proyectos de clasificación de imágenes y reconocimiento de patrones. Este dataset está destinado tanto a investigadores como a desarrolladores que deseen explorar y crear modelos de aprendizaje automático.

## 📁 Estructura del Dataset

```plaintext
flowers-dataset/
│
├── roses/
│   ├── rose1.jpg
│   ├── rose2.jpg
│   └── ...
├── tulips/
│   ├── tulip1.jpg
│   ├── tulip2.jpg
│   └── ...
├── daffodils/
│   ├── daffodil1.jpg
│   ├── daffodil2.jpg
│   └── ...
└── sunflowers/
    ├── sunflower1.jpg
    ├── sunflower2.jpg
    └── ...
📊 Estadísticas
Total de imágenes: 3000
Clases: 5 (Rosas, Tulipanes, Narcisos, Girasoles, Dientes de León)
Formato de imagen: JPEG
Resolución: 1024x768 px
🚀 Uso
Para utilizar este dataset, clona el repositorio y accede a las imágenes:
git clone https://github.com/tuusuario/flowers-dataset.git
cd flowers-dataset

# 🌸 Flowers Dataset 🌼

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0-brightgreen.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange.svg)

## 📋 Descripción

El dataset **Flowers** contiene una colección de imágenes de diversas especies de flores, ideal para proyectos de clasificación de imágenes y reconocimiento de patrones. Este dataset está destinado tanto a investigadores como a desarrolladores que deseen explorar y crear modelos de aprendizaje automático.

## 📁 Estructura del Dataset

```plaintext
flowers-dataset/
│
├── roses/
│   ├── rose1.jpg
│   ├── rose2.jpg
│   └── ...
├── tulips/
│   ├── tulip1.jpg
│   ├── tulip2.jpg
│   └── ...
├── daffodils/
│   ├── daffodil1.jpg
│   ├── daffodil2.jpg
│   └── ...
└── sunflowers/
    ├── sunflower1.jpg
    ├── sunflower2.jpg
    └── ...
📊 Estadísticas
Total de imágenes: 3000
Clases: 4 (Rosas, Tulipanes, Narcisos, Girasoles)
Formato de imagen: JPEG
Resolución: 1024x768 px
🚀 Uso
Para utilizar este dataset, clona el repositorio y accede a las imágenes:

bash
Copiar código
git clone https://github.com/tuusuario/flowers-dataset.git
cd flowers-dataset
Ejemplo de carga del dataset en Python
python
Copiar código
import os
from PIL import Image

data_dir = 'flowers-dataset'
categories = ['roses', 'tulips', 'daffodils', 'sunflowers']

for category in categories:
    path = os.path.join(data_dir, category)
    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        image = Image.open(img_path)
        image.show()  # Abre la imagen
🤝 Contribuciones
¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:

Haz un fork del repositorio.
Crea una rama nueva (git checkout -b feature/nueva-caracteristica).
Realiza los cambios necesarios y haz commit (git commit -am 'Añadir nueva característica').
Sube los cambios a tu fork (git push origin feature/nueva-caracteristica).
Crea un nuevo Pull Request.
📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

📞 Contacto
Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactarme a través de mi correo electrónico.
