import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image
import base64
import io
from image_processing.core import resize_and_compress

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImageData(BaseModel):
    image: str


temp_dir = "temp_dir"


@app.on_event("startup")
def startup():
    os.makedirs(temp_dir, exist_ok=True)
    print("Created temp directory")
    print("Startup Completed")


@app.on_event("shutdown")
def cleanup():
    for filename in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, filename))
    os.rmdir(temp_dir)


@app.post("/process")
async def process_image(data: ImageData):
    base64_image = data.image
    image_data = base64.b64decode(base64_image)
    image = Image.open(io.BytesIO(image_data))
    output_path = f"{temp_dir}/processed_image.jpg"
    resize_and_compress(io.BytesIO(image_data), output_path)
    with open(output_path, "rb") as img_file:
        img_str = base64.b64encode(img_file.read())
    return {"image": img_str.decode("utf-8")}
