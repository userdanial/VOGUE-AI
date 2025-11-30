# generate.py
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from io import BytesIO

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize Hugging Face InferenceClient
client = InferenceClient(provider="hf-inference", api_key=HF_TOKEN)

def generate_image_bytes(prompt: str, width: int = 512, height: int = 512) -> bytes:
    """
    Generate an image from a text prompt using Hugging Face InferenceClient.
    Returns image bytes (PNG).
    """
    # Generate the image
    image = client.text_to_image(
        prompt,
        model="stabilityai/stable-diffusion-xl-base-1.0",
        width=width,
        height=height
    )

    # Convert PIL Image to bytes
    buf = BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()


def image_bytes_to_base64(img_bytes: bytes) -> str:
    import base64
    return base64.b64encode(img_bytes).decode("utf-8")

