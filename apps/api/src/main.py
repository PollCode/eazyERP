import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # ---- Startup ----
#     logger.info("Starting up...")
#     init_db()
#     try:
#         with Session(engine) as db:
#             create_default_admin(db)
#     except Exception:
#         logger.exception("Failed to seed default admin")

#     yield

#     # ---- Shutdown ----
#     logger.info("Shutting down...")
    
app = FastAPI(
    title="EazyERP API",
    # lifespan=lifespan,
    version="0.1.0",
    openapi_url="/api/openapi.json",   
    docs_url="/api/docs",
    redoc_url="/api/redoc",  
)

@app.get('/api/health')
def health_check():
    return {"status": "ok"}