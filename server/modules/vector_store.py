from logger import logger 
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer



class VectorStore():
    def create_vector_store(self,chunks):
        try:
            logger.info("creating Embeddings...")
            
            embedding = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            
            
            logger.info("Creating ChromaDB Vector Store...")
            
            vector_db = Chroma.from_documents(
                documents=chunks,
                embedding=embedding,
                persist_directory="chroma_db"
            )
            logger.info("Vector Store Created Successfully 🥹🥹")

            return vector_db
        
        
        except Exception as e:
            logger.error(f"Error creating vector store: {e} 😖😖")
            raise

