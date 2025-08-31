from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
from PIL import Image
import pytesseract
import io

app = FastAPI()

# Allow CORS so frontend (Streamlit) can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- TEXT EXTRACTION ----
def extract_text_from_pdf(file_bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

def extract_text_from_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes))
    text = pytesseract.image_to_string(image)
    return text.strip()

# ---- ENGAGEMENT ANALYSIS ----
def analyze_text(text: str):
    suggestions = []

    if len(text) < 50:
        suggestions.append("Your post is too short. Try adding more details.")
    elif len(text) > 300:
        suggestions.append("Your post is long. Consider shortening for better engagement.")

    hashtag_count = text.count("#")
    if hashtag_count == 0:
        suggestions.append("Add some hashtags to improve reach.")
    elif hashtag_count > 5:
        suggestions.append("Too many hashtags. Keep it under 5 for readability.")

    mention_count = text.count("@")
    if mention_count == 0:
        suggestions.append("Mention relevant users or pages to boost engagement.")

    if not suggestions:
        suggestions.append("Your post looks well-optimized! 🚀")

    return suggestions


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_bytes = await file.read()

    if file.filename.lower().endswith(".pdf"):
        extracted_text = extract_text_from_pdf(file_bytes)
    elif file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        extracted_text = extract_text_from_image(file_bytes)
    else:
        return {"error": "Unsupported file type. Please upload PDF or Image."}

    suggestions = analyze_text(extracted_text)

    return {
        "filename": file.filename,
        "text": extracted_text,
        "suggestions": suggestions
    }
