# supabase_client.py
import os
from supabase import create_client
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET", "moodboards")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Set SUPABASE_URL and SUPABASE_KEY in .env")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_image_to_storage(img_bytes: bytes, filename: str) -> str:
    """
    Upload image bytes to Supabase Storage and return public URL.
    If bucket is public, we can call get_public_url. For private buckets,
    you'd generate a signed URL.
    """
    path = f"{datetime.utcnow().strftime('%Y/%m/%d')}/{filename}"
    # supabase.storage.from_(bucket).upload expects a file-like object or bytes? 
    # The python client accepts bytes via .upload() where arg is path and file is bytes.
    res = supabase.storage.from_(SUPABASE_BUCKET).upload(path, img_bytes, content_type="image/png")
    if 'error' in res and res['error']:
        raise Exception(f"Upload error: {res['error']}")

    # Get public URL
    public_url = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(path)
    # public_url is dict with 'publicUrl' in some versions
    if isinstance(public_url, dict):
        return public_url.get('publicUrl') or public_url.get('public_url') or public_url.get('publicURL')
    # else if returned string:
    return public_url

def insert_moodboard_record(prompt: str, image_url: str):
    data = {"prompt": prompt, "image_url": image_url}
    res = supabase.table("moodboards").insert(data).execute()
    if res.error:
        raise Exception(f"Insertion error: {res.error}")
    return res.data
