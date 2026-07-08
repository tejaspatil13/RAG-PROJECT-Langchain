from fastapi import UploadFile, File, FastAPI
import os
import shutil

from modules.document_loader import DocumentLoader
from modules.text_splitter import TextSplitter
from modules.vector_store import VectorStore

app = FastAPI()      



# document loader  

loader = DocumentLoader()

# text splitter 

splitter = TextSplitter()

# creating vector Store 

vector_store = VectorStore()


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    upload_dir = "uploaded_files"

    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # document loding 
    documents = loader.load_pdf(file_path)
    
    #creating chunks 
    chunks = splitter.split_documents(documents)
    
    # creating vector Store 
    db = vector_store.create_vector_store(chunks)



    return {
        "pages": len(documents),
        "filename": file.filename,
        "chunks": len(chunks),
        "vector store": len(db)
        }