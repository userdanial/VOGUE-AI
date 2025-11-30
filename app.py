# app.py
import streamlit as st
from generate import generate_image_bytes, image_bytes_to_base64
from supabase_client import supabase
import io
import base64

st.set_page_config(page_title="Mood-Board Generator", layout="wide")
st.title("🎨 Mood-Board Generator")

# -----------------------------
# Input Prompt
# -----------------------------
prompt = st.text_input("Enter your fashion vibe or occasion:")

if st.button("Generate") and prompt.strip():
    with st.spinner("Generating image, please wait..."):
        try:
            img_bytes = generate_image_bytes(prompt)
            img_b64 = image_bytes_to_base64(img_bytes)
            st.image(f"data:image/png;base64,{img_b64}", use_column_width=True)
            
            # Save to session state for later
            st.session_state.generated_image = img_bytes
            st.session_state.prompt_text = prompt

        except Exception as e:
            st.error(f"Error generating image: {e}")

# -----------------------------
# Save to Supabase
# -----------------------------
if "generated_image" in st.session_state:
    if st.button("💾 Save to Board"):
        try:
            # Upload to Supabase Storage
            import uuid
            file_name = f"{uuid.uuid4()}.png"
            res = supabase.storage.from_('moodboards').upload(file_name, st.session_state.generated_image, content_type='image/png')
            
            # Get public URL
            public_url = supabase.storage.from_('moodboards').get_public_url(file_name).get('publicUrl')
            
            # Insert record into DB
            supabase.table("moodboards").insert({
                "prompt": st.session_state.prompt_text,
                "image_url": public_url
            }).execute()
            
            st.success("Saved to Mood-Board!")
        except Exception as e:
            st.error(f"Error saving to Supabase: {e}")

# -----------------------------
# Gallery
# -----------------------------
st.subheader("🌟 Community Gallery")
try:
    data = supabase.table("moodboards").select("*").order("created_at", desc=True).execute()
    records = data.data

    if records:
        cols = st.columns(3)
        for idx, record in enumerate(records):
            col = cols[idx % 3]
            with col:
                st.image(record['image_url'], use_column_width=True)
                st.caption(record['prompt'])
    else:
        st.info("No images saved yet. Generate one!")
except Exception as e:
    st.error(f"Error fetching gallery: {e}")
