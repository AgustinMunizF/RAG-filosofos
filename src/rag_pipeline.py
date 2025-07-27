from chroma_manager import inicializar_chroma
from gemini_integration import configurar_gemini, generar_respuesta

def main():
    # 1. Inicializar componentes
    collection = inicializar_chroma()
    model = configurar_gemini()
    
    # 2. Ejemplo de consulta
    consulta = input("Tu pregunta filosófica: ")
    
    # 3. Buscar en ChromaDB
    resultados = collection.query(
        query_texts=[consulta],
        n_results=3
    )
    
    # 4. Preparar contexto
    contexto = "\n".join(
        f'"{doc}" ({meta["autor"]})' 
        for doc, meta in zip(resultados['documents'][0], resultados['metadatas'][0])
    )
    
    # 5. Generar y mostrar respuesta
    respuesta = generar_respuesta(model, consulta, contexto)
    print(f"\n🧠 Respuesta del Sabio:\n{respuesta}")

if __name__ == "__main__":
    main()