from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import get_settings
from app.database import create_tables
from app.routers import members_router, contact_router, newsletter_router, feedback_router

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run startup tasks before the app begins serving requests."""
    create_tables()  # Creates DB tables if they don't exist — safe to run on every startup
    yield
    # (Shutdown tasks would go here if needed)


app = FastAPI(
    title="Stanchics API",
    description="Backend API for the Stanchics Women in Tech community — Nairobi, Kenya.",
    version="1.0.0",
    docs_url="/docs" if not settings.is_production else None,   # Hide Swagger in production
    redoc_url="/redoc" if not settings.is_production else None,
    lifespan=lifespan,
)

# ─── CORS ────────────────────────────────────────────────────────────────────
# Allows the separately-hosted HTML frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins_list,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# ─── Routers ─────────────────────────────────────────────────────────────────
app.include_router(members_router)
app.include_router(contact_router)
app.include_router(newsletter_router)
app.include_router(feedback_router)


# ─── Health check ────────────────────────────────────────────────────────────
@app.get("/health", tags=["Health"])
def health():
    """Azure App Service uses this to confirm the app is running."""
    return {"status": "ok", "service": "Stanchics API"}


# ─── Root ────────────────────────────────────────────────────────────────────
@app.get("/", tags=["Health"])
def root():
    return {
        "message": "Stanchics API is running.",
        "docs": "/docs",
        "version": "1.0.0",
    }
