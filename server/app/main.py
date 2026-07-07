from fastapi import FastAPI

from app.config import database
from app.modules.auth import auth_routes
from app.modules.users import user_routes
from app.modules.posts import post_routes
from app.modules.votes import vote_routes

app = FastAPI()

@app.on_event("startup")
async def init_tables():
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)
        
app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(post_routes.router)
app.include_router(vote_routes.router)