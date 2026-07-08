
from langchain_community.document_loaders import PyPDFLoader

from logger import logger


class DocumentLoader:
    def load_pdf(self, file_path : str):
        try:
            logger.info(f"loading pdf : {file_path}")
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            logger.info(f"loaded {len(documents)} pages 😎😎")

            return documents

        except Exception as e:
 
            logger.error(f"Error loading PDF : {e} 😭😭")

            raise

