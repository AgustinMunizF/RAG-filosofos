from chroma_manager import inicializar_chroma
from gemini_integration import configurar_gemini, generar_respuesta

def main():
    # 1. Inicializar ChromaDB y Gemini
    collection = inicializar_chroma()
    model = configurar_gemini()
    
    # 2. Solicitar consulta al usuario
    consulta = input("Tu frase filosófica: ")
    
    #  3. Consultar ChromaDB
    resultados = collection.query(
        query_texts=[consulta],
        n_results=3
    )
    
    # 4. Formatear contexto
    contexto = "\n".join(
        f'"{doc}" ({meta["autor"]})' 
        for doc, meta in zip(resultados['documents'][0], resultados['metadatas'][0])
    )
    
    # 5. Generar respuesta con Gemini
    respuesta = generar_respuesta(model, consulta, contexto)
    print(f"\nRespuesta del Sabio:\n{respuesta}")

if __name__ == "__main__":
    main()