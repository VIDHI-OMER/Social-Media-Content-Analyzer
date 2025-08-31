# 📊 Social Media Content Analyzer

A web application that analyzes social media posts from uploaded **PDFs or Images** and suggests improvements for better engagement.  

---

## 🚀 Features
- 📂 Upload PDFs or Images (drag & drop supported)  
- 📝 Extract text using:
  - **pdfplumber** for PDFs  
  - **pytesseract OCR** for images  
- 💡 Suggests engagement improvements:
  - Post length optimization  
  - Hashtag usage  
  - Mentions usage  
- ✅ User-friendly frontend with Streamlit  
- ⚡ FastAPI backend for text extraction & analysis  

---

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)  
- **PDF Processing:** [pdfplumber](https://github.com/jsvine/pdfplumber)  
- **OCR:** [pytesseract](https://github.com/madmaze/pytesseract) + [Pillow](https://python-pillow.org/)  
- **Deployment:** Streamlit Cloud + Render  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/social-media-content-analyzer.git
cd social-media-content-analyzer
