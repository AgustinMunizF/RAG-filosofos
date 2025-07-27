import chromadb
from chromadb.utils import embedding_functions
import json
import os
from pathlib import Path

def inicializar_chroma():
    # 1. Usar rutas absolutas basadas en la ubicación del script
    base_dir = Path(__file__).parent.parent  # Carpeta raíz del proyecto
    db_path = base_dir / "db_filosofos"
    json_path = base_dir / "data" / "citas_filosofos.json"
    
    # 2. Verificar que el JSON existe
    if not json_path.exists():
        raise FileNotFoundError(
            f"❌ Archivo no encontrado en: {json_path}\n"
            f"Crea el archivo o verifica la ruta."
        )
    
    # 3. Configurar ChromaDB
    client = chromadb.PersistentClient(path=str(db_path))
    embedding_func = embedding_functions.DefaultEmbeddingFunction()
    
    collection = client.get_or_create_collection(
        name="citas_filosofos",
        embedding_function=embedding_func
    )
    
    # Cargar citas solo si la colección está vacía
    if collection.count() == 0:
        with open(json_path, 'r', encoding='utf-8') as f:
            citas = json.load(f)
        
        collection.add(
            documents=[c["cita"] for c in citas],
            metadatas=[{"autor": c["autor"]} for c in citas],
            ids=[str(i) for i in range(len(citas))]
        )
        print(f"✅ {len(citas)} citas cargadas en ChromaDB")
    
    return collection