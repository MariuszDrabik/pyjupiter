from fastapi import FastAPI
from routers import ships, home
import uvicorn


app = FastAPI()
app.include_router(home.router)
app.include_router(ships.router)


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=3003)