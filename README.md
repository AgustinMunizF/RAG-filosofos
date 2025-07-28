# Proyecto RAG Filosófico:

Este proyecto utiliza un sistema de Retrieval-Augmented Generation (RAG) que responde preguntas con citas de filósofos clásicos, combinando ChromaDB para su busqueda y Gemini para generación de respuestas.

# Instalaciones necesarias:

Una vez clonado el repositorio se deberá configurar el entorno virtual con el comando:
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

Luego se deberan instalar las dependencias:
pip install -r requirements.txt

La API key de Gemini ya viene en el .env del proyecto

# Ejemplo de uso
ejecutar el archivo principal desde la terminal con:
python src/rag_pipeline.py

En la terminal les pedirá que ingresen su frase filisofica.
ChromaDB localiza las 3 citas más relevantes de su base de datos (vectorizada).  
Luego Gemini combina estas citas y genera una respuesta original en estilo filosófico que aparecera en la terminal como la respuesta del sabio.  

# Ejemplo practico: 
Tu frase filosófica: que es la vida?

Respuesta del Sabio:
La vida, vista a través del pragmatismo de Schopenhauer, es una experiencia con déficit existencial, un constante desequilibrio entre el anhelo y la satisfacción. 
Sin embargo, como sugiere Heidegger, este mismo déficit se manifiesta y se comprende a través del lenguaje, la casa donde construimos nuestro ser y donde resonamos con el mundo, 
dando sentido a la inefable experiencia de existir, incluso en medio de la  "esclavitud de las pasiones"  de la que habla Hume.
