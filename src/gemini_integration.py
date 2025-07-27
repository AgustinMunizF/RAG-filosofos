import google.generativeai as genai
from dotenv import load_dotenv
import os

def configurar_gemini():  # <<- ¡Nombre exacto!
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    return genai.GenerativeModel('gemini-1.5-flash')

def generar_respuesta(model, consulta, contexto):  # <<- ¡Nombre exacto!
    prompt = f"""
    Eres un sabio que fusiona todas las corrientes filosóficas.
    Consulta: '{consulta}'
    
    Contexto (autor entre paréntesis):
    {contexto}

    Responde:
    1. En 2-3 oraciones
    2. Citando al menos 2 autores
    3. Con lenguaje claro pero profundo
    """
    return model.generate_content(prompt).text