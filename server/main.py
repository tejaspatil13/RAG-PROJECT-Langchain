from fastapi import UploadFile, File, FastAPI
from pydantic import BaseModel
import os
import shutil

from modules.document_loader import DocumentLoader
from modules.text_splitter import TextSplitter
from modules.vector_store import VectorStore
from modules.retriever import Retriever
from modules.rag_chain import RAGChain

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()      

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# document loader  

loader = DocumentLoader()

# text splitter 

splitter = TextSplitter()

# creating vector Store 

vector_store = VectorStore()

# retriever

retriever = Retriever().get_retriever()
chain = RAGChain().get_chain()



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
    vector_store.create_vector_store(chunks)



    return {
        "message": "Vector Store Created Successfully",
        "pages": len(documents),
        "chunks": len(chunks)
    }


# # -----------------------------
# # Chat Endpoint
# # -----------------------------




class ChatRequest(BaseModel):
    question : str

@app.post("/chat")

async def chat(request: ChatRequest):
    docs = retriever.invoke(request.question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    answer = chain.invoke({
        "context" : context,
         "question" : request.question
    })

    return{
        "question":request.question,
        "answer": answer
    }















# from fastapi import FastAPI, UploadFile, File
# from pydantic import BaseModel
# import os
# import shutil

# from modules.document_loader import DocumentLoader
# from modules.text_splitter import TextSplitter
# from modules.vector_store import VectorStore
# from modules.rag_chain import RAGChain

# app = FastAPI(
#     title="Industry Level RAG API",
#     version="1.0.0"
# )

# # -----------------------------
# # Initialize Components
# # -----------------------------

# loader = DocumentLoader()
# splitter = TextSplitter()
# vector_store = VectorStore()

# # Create LCEL Chain once
# rag_chain = RAGChain()
# chain = rag_chain.get_chain()

# # -----------------------------
# # Upload Endpoint
# # -----------------------------

# @app.post("/upload")
# async def upload_pdf(file: UploadFile = File(...)):

#     upload_dir = "uploaded_files"
#     os.makedirs(upload_dir, exist_ok=True)

#     file_path = os.path.join(upload_dir, file.filename)

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     # Load PDF
#     documents = loader.load_pdf(file_path)

#     # Split into chunks
#     chunks = splitter.split_documents(documents)

#     # Store in ChromaDB
#     vector_store.create_vector_store(chunks)

#     return {
#         "message": "Vector Store Created Successfully",
#         "filename": file.filename,
#         "pages": len(documents),
#         "chunks": len(chunks)
#     }


# # -----------------------------
# # Chat Endpoint
# # -----------------------------

