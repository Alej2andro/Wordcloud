# 🧠 Proyecto: Extracción y Visualización de Información sobre Ciencia de Datos  

## 📋 Descripción General  
Este proyecto realiza un **proceso completo de Web Scraping, Limpieza de Texto, ETL y Visualización de Datos**, con el objetivo de **extraer información relevante sobre Ciencia de Datos desde distintas fuentes web** y **representarla visualmente mediante una nube de palabras y un gráfico de frecuencias**.  

El flujo del análisis sigue una estructura **ETL (Extract, Transform, Load)**:  
1. **Extracción** de texto desde múltiples URLs (IBM, Tableau, Wikipedia).  
2. **Transformación** mediante tokenización, limpieza lingüística y eliminación de *stopwords*.  
3. **Carga y visualización** final en un **reporte PDF automatizado** con dos gráficos generados en Python.  

---

## 🚀 Objetivo del Proyecto  
Aprender de forma práctica y **autónoma** cómo realizar un flujo de trabajo real de análisis textual en Ciencia de Datos, incluyendo:  

- Web scraping intuitivo.  
- Procesamiento y limpieza de texto.  
- Generación de una nube de palabras reproducible.  
- Visualización de las palabras más frecuentes.  
- Exportación automática a PDF para reportes profesionales.  

---

## 🧩 Adaptabilidad y Reproducibilidad  

Este script puede servir como una **matriz base** para desarrollar **otros análisis de nubes de palabras** o estudios textuales similares.  
Para adaptarlo a distintos contextos, basta con modificar:  

- 🔗 **Las URLs** en la lista `urls` (fuentes de información).  
- 🧹 **Los filtros de limpieza y exclusión de palabras** (`palabras_excluir` o *stopwords*).  
- 🖼️ **Los argumentos de las visualizaciones** (color, tamaño, número de palabras, etc.).  
- 📄 **Los parámetros del PDF** (títulos, imágenes, disposición o formato de salida).  

La **reproducibilidad del WordCloud** se garantiza gracias al argumento `random_state = 53`.  
> Si se cambia ese número, se genera una nube distinta en la disposición de las palabras, manteniendo la misma información subyacente.  
Esto permite comparar distintas configuraciones visuales sin alterar el contenido del análisis.  

---

## 🧾 Estructura de Archivos  

📂 Proyecto wordcloud:

├── 🐍 script_wordcloud.py        → Código principal del análisis  
├── ☁️ nube_palabras.png          → Nube de palabras generada  
├── 📊 grafico_frecuencia.png     → Gráfico de top 10 palabras  
├── 📄 reporte_visual.pdf         → Reporte final exportado  
└── 🧠 README.md                  → Documentación del proyecto

## 🧩 Flujo del Proceso  

### 1️⃣ Extracción  
Se recopilan textos desde URLs de referencia en ciencia de datos e inteligencia artificial:  
- [Tableau - Data Science](https://www.tableau.com/es-es/data-insights/data-science)  
- [IBM - Data Science](https://www.ibm.com/es-es/topics/data-science)  
- [Wikipedia - Inteligencia Artificial](https://es.wikipedia.org/wiki/Inteligencia_artificial)  
- Entre otras fuentes relevantes.  

El texto de cada sitio se obtiene con `BeautifulSoup` y se acumula para su posterior análisis.  

---

### 2️⃣ Transformación (Limpieza y Tokenización)  
- Tokenización del texto en palabras.  
- Eliminación de signos, números y *stopwords* (en español e inglés).  
- Filtrado adicional de palabras irrelevantes o redundantes.  

---

### 3️⃣ Carga y Visualización  
- Se genera una **nube de palabras (WordCloud)** con `random_state=53` para garantizar **reproducibilidad visual**.  
- Si se cambia el valor de `random_state`, la forma de la nube cambiará, pero las palabras seguirán siendo las mismas.  
- Se crea un **gráfico de barras** con las 10 palabras más frecuentes.  

---

### 4️⃣ Reporte Automatizado (PDF)  
Ambas visualizaciones se exportan en un **reporte visual (`reporte_visual.pdf`)** que incluye:  
- Título con la fecha del día.  
- Imagen de la nube de palabras.  
- Gráfico de frecuencia de términos.  

---

## 📊 Ejemplo de Resultados  

### - Nube de Palabras  
Representa los términos más frecuentes en los textos de Ciencia de Datos.  

### - Gráfico de Frecuencia  
Muestra las **10 palabras más mencionadas**, reflejando los conceptos dominantes en las fuentes analizadas.  

### - Reporte PDF  
El resultado final es un **reporte automático y portable** que consolida los hallazgos visuales del análisis.  

---

## 💡 Aprendizajes Clave  
- Implementar **Web Scraping** de forma intuitiva para extraer información útil de la web.  
- Aplicar **procesos ETL** al tratamiento de texto.  
- Generar **visualizaciones reproducibles** (controlando la aleatoriedad con `random_state`).  
- Crear **reportes visuales automatizados** para comunicar resultados.  
- **Reutilizar el mismo script como plantilla adaptable** para distintos proyectos de análisis textual.  

---

## ⚙️ Requisitos de Ejecución  

🧩 Entorno de Desarrollo  
💻 IDE: 🕷️ Spyder  
🐍 Lenguaje: Python 3.x

Instalar las dependencias necesarias (puedes usar un entorno virtual):  

```bash
pip install requests beautifulsoup4 matplotlib wordcloud nltk fpdf
import nltk
nltk.download("stopwords")


