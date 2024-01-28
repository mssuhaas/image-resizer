# Image Processing API

This project is a FastAPI application that provides an endpoint for image processing. The main functionality of this API is to resize and compress images.

## Features

- Resize images to a thumbnail of 800x800 pixels.
- Compress images to a maximum size of 100KB.
- Accepts and returns images in base64 format.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/yourrepository.git
```

2. Navigate to the project directory:
```bash
cd yourrepository
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running Locally (Development):

1. Start the server:
```bash
uvicorn app:app --reload
```

2. Send a POST request to the `/process` endpoint with the following JSON body:
```json
{
    "image": "<base64_encoded_image>",
    "initial_quality": 90
}
```

The `image` field should contain the base64 encoded string of the image you want to process. The `initial_quality` field is optional and defaults to 90 if not provided.

The response will be a JSON object with a single field `image` that contains the base64 encoded string of the processed image.

## Docker Image Run

1. Pull Docker image:
```bash
docker pull ghcr.io/mssuhaas/image-resizer
```

2. Run the docker container 
```bash
docker run mssuhaas/image-resizer -d -it
```
Note: The docker container uses port 5000, remap it as required using `-p` flag

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
