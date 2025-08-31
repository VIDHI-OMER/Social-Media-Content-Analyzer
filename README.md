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



---

## 📝 Approach

The Social Media Content Analyzer application is designed to extract and analyze text from PDF and image documents to provide insights for improving engagement. The application supports drag-and-drop and file picker interfaces for easy document upload, ensuring a user-friendly experience. For PDFs, text extraction is performed using pdfplumber to preserve formatting. For image-based documents, OCR technology (pytesseract) is employed to accurately extract textual content.

The backend is implemented using FastAPI, which handles file uploads, text extraction, and serves results efficiently. The frontend is built with Streamlit for rapid development and interactive visualization of extracted content. Loading states and basic error handling are incorporated to enhance user experience and ensure robustness.

The project leverages open-source tools and libraries, avoiding paid services while maintaining production-quality standards. Test data was sourced from publicly available social media posts and documents to validate functionality.

Overall, the approach emphasizes simplicity, reliability, and usability, with clear separation between frontend and backend logic. The application demonstrates practical problem-solving and clean code structure, providing a foundation for future enhancements such as sentiment analysis or engagement prediction.

