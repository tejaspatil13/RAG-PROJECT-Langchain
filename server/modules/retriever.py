from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from logger import logger


class Retriever:

    retriever = None

    def get_retriever(self):
        try:
            if Retriever.retriever is not None:
                logger.info("Using Existing Retriever...")
                return Retriever.retriever
            
            
            
            logger.info("Loading Embedding Model...")

            embedding = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )

            logger.info("Loading ChromaDB...")

            vector_db = Chroma(
                persist_directory="chroma_db",
                embedding_function=embedding
            )

            logger.info("Creating Retriever...")

            retriever = vector_db.as_retriever(
                search_kwargs={"k": 3}
            )

            logger.info("Retriever Created Successfully")

            return Retriever.retriever

        except Exception as e:
            logger.error(f"Retriever Error: {e}")
            raise