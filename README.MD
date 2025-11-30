# VOGUE-AI Moodboard Generator

Generate fashion moodboards from text prompts using AI and save them to a personal gallery.

---

## Demo

*(Add a screenshot of your app here or a link to live demo)*

---

## Features

- **Creator Studio**: Enter a text prompt describing a fashion vibe and generate a unique concept image.
- **Curator Database**: Save your favorite images to a personal gallery (Supabase).
- **Gallery**: Browse saved images in a responsive grid layout with hover effects showing the prompt.
- **AI-powered**: Uses Hugging Face Inference API (Stable Diffusion XL) for image generation.

---

## Tech Stack

- **Frontend/Backend**: Streamlit (Python)
- **AI Integration**: Hugging Face InferenceClient
- **Database/Storage**: Supabase (PostgreSQL + Storage bucket)
- **Styling**: Streamlit native + optional CSS
- **Version Control**: GitHub

## Create virtual environment (recommended)

### Windows
python -m venv appenv
.\appenv\Scripts\activate

### macOS/Linux
python3 -m venv appenv
source appenv/bin/activate


## Install dependencies

pip install -r requirements.txt


## Configure environment variables

Copy .env.example to .env:

cp .env.example .env


## Fill in your credentials:

HF_TOKEN=your_huggingface_token_here
HF_MODEL=stabilityai/stable-diffusion-xl-base-1.0
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your_supabase_service_role_key_here
SUPABASE_BUCKET=moodboards


Important: Never share your .env file publicly.

## Run the app
streamlit run app.py


## Use the app
Enter a fashion prompt (e.g., "A futuristic cyberpunk coffee date in Tokyo")
Click Generate → Wait for the image
Click Save to Board to store in your Supabase gallery
Scroll down to see your saved images in the gallery

## Technical Challenges
403 Forbidden errors from Hugging Face API solved by updating token permissions to include “Make calls to Inference Providers”.
404 Not Found errors avoided by switching from the deprecated Router HTTP POST to InferenceClient.text_to_image method.
Image size adjusted via width and height parameters in generate.py for faster generation and smaller file sizes.

## Folder Structure
VOGUE-AI/
│
├─ app.py             # Main Streamlit app
├─ generate.py        # AI image generation helper
├─ requirements.txt   # Python dependencies
├─ .env.example       # Template for environment variables
├─ .gitignore
└─ README.md

## Future Improvements (Optional)
Add Supabase Auth to show user-specific boards
Add “Surprise Me” button to generate random prompts using an LLM
Add AI-to-AI critic for auto-generated witty titles for outfits
Add higher-resolution downloads or image upscaling

## License

This project is for educational purposes / internship submission.
---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/VOGUE-AI.git
cd VOGUE-AI


