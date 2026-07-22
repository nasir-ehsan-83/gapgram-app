from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.common.errors.handlers import init_error_handlers
from src.db import database

from src.modules.auth import routes as auth_routes
from src.modules.users import routes as users_routes
from src.modules.posts import routes as posts_routes
from src.modules.votes import routes as votes_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)
    yield
    await database.engine.dispose()

app = FastAPI(lifespan = lifespan)


init_error_handlers(app)

app.include_router(auth_routes.router)
app.include_router(users_routes.router)
app.include_router(posts_routes.router)
app.include_router(votes_routes.router)