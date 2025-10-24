import requests  
from bs4 import BeautifulSoup  
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud  
import nltk
from nltk.corpus import stopwords
from fpdf import FPDF
import os
from collections import Counter
from datetime import datetime


# Descargar stopwords en español e inglés
nltk.download("stopwords") 

# URL de la página web  
urls = [
    "https://www.tableau.com/es-es/data-insights/data-science",
    "https://www.ibm.com/es-es/topics/data-science",
    "https://www.ibm.com/es-es/topics/artificial-intelligence",
    "https://es.wikipedia.org/wiki/Inteligencia_artificial",
    "https://www.ibm.com/es-es/topics/machine-learning",
    "https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico"
]

# Acumular texto de todas las URLs
texto_total = ""

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    texto = soup.get_text()
    texto_total += texto + " "  # Agrega espacio entre textos

# 📁 Configurar carpeta de trabajo
directorio = r"C:\Users\ASUS\Desktop\carpeta"
os.chdir(directorio)

texto = texto_total

# Tokenizar el texto en palabras  
palabras = texto.split()

# Unir stopwords en español e inglés
stop_words = set(stopwords.words("spanish")) | set(stopwords.words("english"))

# Lista de palabras específicas a excluir  ,sgunda zona de cambios
palabras_excluir = {"ibm","tableau","articulo","suelen","ofrece","tener","grandes","parte","crear",
                    "usuario","trabajo", "uso","nube","puden","marco","trabajo","cómo","precios",
                    "además","alternar","alfabetización","versiones","gratis",
                    "obtener","permiten","pueden","empresa","etapa","carga","overview"
                    "incluye","nesecario","siguiente","mayor",
                    "aunque","tomo","ser","comunes","suele"}  # Puedes agregar más palabras si lo deseas

# Limpiar palabras eliminando signos y caracteres innecesarios y números  
palabras_limpias = [re.sub(r"[^\w\s]", "", palabra).lower() for palabra in palabras]  
palabras_sin_numeros = [palabra for palabra in palabras_limpias if not re.search(r"\d", palabra)]  

# Filtrar palabras eliminando stopwords y palabras específicas
palabras_filtradas = [palabra for palabra in palabras_sin_numeros if palabra not in stop_words and palabra not in palabras_excluir]

# Unir el texto final
texto_final = " ".join(palabras_filtradas)

# Generar la nube de palabras
wordcloud =WordCloud(width=1000, height=500,max_words=300,max_font_size=250,scale=2,colormap="ocean",
                 prefer_horizontal=0.90,background_color="ivory",random_state=53).generate(texto_final)

wordcloud_path = "nube_palabras.png"
wordcloud.to_file(wordcloud_path)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
  

 #📊 Gráfico de frecuencia
top = Counter(palabras_filtradas).most_common(10)
pal, frec = zip(*top)
plt.figure(figsize=(8, 4))
plt.barh(pal, frec, color="#0047AB")
plt.xlabel("Frecuencia")
plt.title("Top 10 Palabras Más Frecuentes")
plt.gca().invert_yaxis()
plt.tight_layout()
grafico_path = "grafico_frecuencia.png"
plt.savefig(grafico_path)
plt.show()
#plt.close()

# 📄 PDF con visualizaciones
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style="B", size=16)
titulo = f"Reporte Visual({datetime.now().strftime('%Y-%m-%d')})"
pdf.cell(200, 10, titulo.encode("latin-1", "ignore").decode("latin-1"), ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Visualización: Nube de Palabras", ln=True, align="C")
pdf.image(wordcloud_path, x=10, w=180)
pdf.ln(10)

pdf.cell(200, 10, "Gráfico: Top 10 Palabras Frecuentes", ln=True, align="C")
pdf.image(grafico_path, x=10, w=180)
pdf.ln(10)

pdf.output("reporte_visual.pdf")
print("✅ PDF exportado correctamente: reporte_visuale.pdf") 








