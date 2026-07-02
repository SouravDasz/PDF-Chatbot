from fastapi import FastAPI,Request
from services.template import template
from api.uploads import router as file_router
from services.rag import clear_db
app=FastAPI()

router_list=[file_router]
for router in router_list:
    app.include_router(router)

@app.get("/")
def home(request:Request):
    # clear_db()
    return template.TemplateResponse(request=request,name="home.html")