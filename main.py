import uvicorn

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from users.interface.controllers.user_controller import router as user_routers
from fastapi.responses import JSONResponse

app = FastAPI()
app.include_router(user_routers)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code = 400,
        content=exc.errors()
    )

@app.get("/")
def hello():
    return {"Hello":"FastAPI"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)
