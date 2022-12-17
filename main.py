import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI, Request, Form
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Regex_generator import Regex_generator



app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def get():
    response = RedirectResponse('/reg-extractor/')
    return response

@app.get("/reg-extractor/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})

@app.post('/reg-extractor/')
def regex_executor(request:Request,input_text: str = Form(...)):
    word = input_text.strip()
    if len(word) != 0:
        reg_gen = Regex_generator(word=word)
        res = reg_gen.regex_maker()
        return templates.TemplateResponse("item.html",{'request':request,'output':res})
    else:
        return templates.TemplateResponse("item.html",{'request':request,'output':''})


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8888,reload= True)