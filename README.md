
🧠 Proyecto: Extracción y Visualización de Información sobre Ciencia de Datos
📋 Descripción General
Este proyecto realiza un proceso completo de Web Scraping, Limpieza de Texto, ETL y Visualización de Datos, con el objetivo de extraer información relevante sobre Ciencia de Datos desde distintas fuentes web y representarla visualmente mediante una nube de palabras y un gráfico de frecuencias.
El flujo del análisis sigue una estructura ETL (Extract, Transform, Load):

Extracción de texto desde múltiples URLs (IBM, Tableau, Wikipedia).
Transformación mediante tokenización, limpieza lingüística y eliminación de stopwords.
Carga y visualización final en un reporte PDF automatizado con dos gráficos generados en Python.


🚀 Objetivo del Proyecto
Aprender de forma práctica y autónoma cómo realizar un flujo de trabajo real de análisis textual en Ciencia de Datos, incluyendo:

Web scraping intuitivo.
Procesamiento y limpieza de texto.
Generación de una nube de palabras reproducible.
Visualización de las palabras más frecuentes.
Exportación automática a PDF para reportes profesionales.


🔄 Reproducibilidad y Adaptabilidad
Este script está diseñado como matriz reutilizable para otros análisis de WordCloud. Para adaptarlo a diferentes requerimientos:
Parámetros configurables:

URLs: Modificar las fuentes de extracción según el dominio de análisis.
Filtros de texto: Ajustar stopwords y condiciones de limpieza.
Argumentos de visualización: Personalizar colores, tamaños y formato de la nube de palabras.
Configuración del PDF: Adaptar título, dimensiones y estructura del reporte.

Reproducibilidad visual:
El argumento random_state=53 en WordCloud garantiza que la nube de palabras sea idéntica en cada ejecución. Si se cambia este número (ej. random_state=42), se generará una disposición visual diferente de las mismas palabras.

🧾 Estructura de Archivos
📂 proyecto_wordcloud/
├── 🐍 script_wordcloud.py      → Código principal del análisis
├── ☁️ nube_palabras.png        → Nube de palabras generada
├── 📊 grafico_frecuencia.png   → Gráfico de top 10 palabras
├── 📄 reporte_visual.pdf       → Reporte final exportado
└── 🧠 README.md                → Documentación del proyecto

🧰 Tecnologías y Librerías Utilizadas
EtapaLibrerías / HerramientasWeb Scrapingrequests, BeautifulSoupProcesamiento de Textore, nltk, collections.CounterVisualizaciónmatplotlib, wordcloudReporte AutomatizadofpdfEntorno de TrabajoSpyder (Python IDE)

🧩 Flujo del Proceso
1️⃣ Extracción
Se recopilan textos desde URLs de referencia en ciencia de datos e inteligencia artificial:

Tableau - Data Science
IBM - Data Science
Wikipedia - Inteligencia Artificial
entre otras.

El texto de cada sitio se obtiene con BeautifulSoup y se acumula para su posterior análisis.
2️⃣ Transformación (Limpieza y Tokenización)

Tokenización del texto en palabras.
Eliminación de signos, números y stopwords (en español e inglés).
Filtrado adicional de palabras irrelevantes o redundantes.

3️⃣ Carga y Visualización

Se genera una nube de palabras (WordCloud) con random_state=53 para garantizar reproducibilidad visual.
Se crea un gráfico de barras con las 10 palabras más frecuentes.

4️⃣ Reporte Automatizado (PDF)
Ambas visualizaciones se exportan en un reporte visual (reporte_visual.pdf) que incluye:

Título con fecha del día.
Imagen de la nube de palabras.
Gráfico de frecuencia de términos.


📊 Ejemplo de Resultados
☁️ Nube de Palabras
Representa los términos más frecuentes en los textos de Ciencia de Datos.
📊 Gráfico de Frecuencia
Muestra las 10 palabras más mencionadas, reflejando los conceptos dominantes en las fuentes analizadas.
📄 Reporte PDF
El resultado final es un reporte automático y portable que consolida los hallazgos visuales del análisis.

💡 Aprendizajes Clave

Implementar Web Scraping de forma intuitiva para extraer información útil de la web.
Aplicar procesos ETL al tratamiento de texto.
Generar visualizaciones reproducibles (controlando la aleatoriedad con random_state).
Crear reportes visuales automatizados para comunicar resultados.


⚙️ Requisitos de Ejecución
Instalar las dependencias necesarias:
bashpip install requests beautifulsoup4 nltk matplotlib wordcloud fpdf
Descargar recursos de NLTK (ejecutar una sola vez):
pythonimport nltk
nltk.download('stopwords')
nltk.download('punkt')

🚀 Uso
bashpython script_wordcloud.py
El script generará automáticamente:

nube_palabras.png
grafico_frecuencia.png
reporte_visual.pdf


📝 Licencia
Este proyecto es de código abierto y está disponible para fines educativos.


