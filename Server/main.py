from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware
import os
from client import getSuggest, extract_image_id, getRecord
import uvicorn

origins = [
    "http://localhost",
    "http://localhost:5050",
    "http://localhost:5173",
]

app = FastAPI()

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mock_data = [
    {
        "name": "ZX 700 HD Shoes",
        "brand": "Adidas",
        "color": "Black",
        "price": 63,
        "currency": "USD",
        "rating": 4.5,
        "images": [
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/027ab9d8671a4ccd9087ac0900cbd5e8_9366/ZX_700_HD_Shoes_Black_G55780_01_standard.jpg",
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/7a734476ac854919bedfac0900cc00d7_9366/ZX_700"
        ],
        "url": "https://www.adidas.com/us/zx-700-hd-shoes/G55780.html"
    },
    {
        "name": "Sportswear Comfy & Chill Full Zip Hoodie",
        "brand": "Grey",
        "price": 56,
        "currency": "USD",
        "rating": 4.2,
        "images": [
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/7f75112d1bcc44148b7dad23002e0272_9366/adidas_Sportswear_Comfy_and_Chill_Full_Zip_Hoodie_Grey_H45371_25_model.jpg",
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/4030e7a904a843e8b7fdad23002df9fa_9366/adidas_Sportswear_Comfy_and_Chill_Full_Zip_Hoodie_Grey_H45371_23_hover_model.jpg",
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/f1e985479c734d1fb867ad25006054ba_9366/adidas_Sportswear_Comfy_and_Chill_Full_Zip_Hoodie_Grey_H45371_01_laydown.jpg",
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/dd35cc22577641c9b5f0ad23002e1b0d_9366/adidas_Sportswear_Comfy_and_Chill_Full_Zip_Hoodie_Grey_H45371_42_detail.jpg",
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/738a0662b8b64adfaa28ad23002e0ed9_9366/adidas_Sportswear_Comfy_and_Chill_Full_Zip_Hoodie_Grey_H45371_41_detail.jpg"
        ],
        "url": "https://www.adidas.com/us/adidas-sportswear-comfy-chill-full-zip-hoodie/H45371.html"
    },
    {
        "name": "Techfit Tights",
        "brand": "Adidas",
        "price": 25,
        "currency": "USD",
        "rating": 4.2,
        "images": [
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/45d2d3247aeb4fd298cead12010cee15_9366/Techfit_Tights_Red_EY1067_01_laydown.jpg",
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/b7d4b5cbc5384b0ea463ad12010e82a4_9366/Techfit_Tights_Red_EY1067_02_laydown_hover.jpg",
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/b77f18708528428c9255ad120112f5e6_9366/Techfit_Tights_Red_EY1067_43_detail.jpg",
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/9dcf168e31744e7f9abbad1201136e93_9366/Techfit_Tights_Red_EY1067_41_detail.jpg",
            "https://assets.adidas.com/images/w_600,f_auto,q_auto/7a91db9f4962477ea457ad12011297ae_9366/Techfit_Tights_Red_EY1067_42_detail.jpg"
        ],
        "url": "https://www.adidas.com/us/techfit-tights/EY1067.html"
    }
]

@app.get("/")
async def root():
    return {"message": "Server is running!", "status": 200}

@app.post("/login")
async def root(username, password):
    if (username == "admin") and (password == "123"):
        return {"success": True}
    return {"success": False}

@app.post("/test")
async def root(input: UploadFile = File(...)):
    try:
        image = Image.open(BytesIO(await input.read()))
        return JSONResponse(content={"data": mock_data, "message": "Successful!"}, status_code=200)
    except:
        return JSONResponse(content={"data": None, "message": "Only pictures are accepted!"}, status_code=422)

@app.post("/suggest")
async def root(input: UploadFile = File(...)):
    try:
        image = Image.open(BytesIO(await input.read()))
        file_extension = os.path.splitext(input.filename)[1].lower()
        filename = f"uploaded_image{file_extension}"
        image.save(filename)
        response = getSuggest(filename)
        result = {}
        values = []
        for key, value in response.items():
            if key not in ['Upper-clothes', 'Pants']:
                continue
            result[key] = [] 
            for file_path in value:
                result[key].append(extract_image_id(file_path))
            result[key] = list(set(result[key]))
            for id in result[key]:
                value = getRecord(id)
                for hit in value['hits']['hits']:
                    source = hit['_source']
                    print(source)
                    if source not in values:
                        values.append(source)
        return JSONResponse(content={"data": values, "message": "Successful!"}, status_code=200)
    except Exception as e:
        print(e)
        return JSONResponse(content={"data": None, "message": "Only pictures are accepted!"}, status_code=422)

if __name__ == '__main__':
    uvicorn.run(app, port=5050, host='0.0.0.0')