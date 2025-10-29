from fastapi import FastAPI
from routers import authors_router, auth_router, books_router, loans_router
import dotenv

dotenv.load_dotenv(".env")

app = FastAPI()
app.include_router(auth_router)
app.include_router(authors_router)
app.include_router(books_router)
app.include_router(loans_router)
