from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from logger import logger


class Retriever:

    def get_retriever(self):
        try:
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

            return retriever

        except Exception as e:
            logger.error(f"Retriever Error: {e}")
            raise