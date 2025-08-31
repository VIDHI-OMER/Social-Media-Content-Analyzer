import streamlit as st
import requests

st.title("📊 Social Media Content Analyzer")
st.write("Upload a PDF or Image file to extract text and get engagement suggestions.")

uploaded_file = st.file_uploader("Choose a PDF or Image file", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    with st.spinner("Processing... Please wait."):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        try:
            response = requests.post("http://127.0.0.1:8000/upload/", files=files)
            result = response.json()

            if "error" in result:
                st.error(result["error"])
            else:
                st.subheader("📄 Extracted Text:")
                st.text_area("Extracted Content", result["text"], height=300)

                st.subheader("💡 Suggestions for Engagement:")
                for suggestion in result["suggestions"]:
                    st.write("✅", suggestion)

        except Exception as e:
            st.error(f"Error: {e}")
