# frontend/app.py

import streamlit as st
import requests

st.set_page_config(page_title="Qwen3 PDF Assistant")

st.title("📄 Qwen3 PDF Assistant")

# Upload PDF
uploaded_file = st.file_uploader("",type=["pdf"])

if uploaded_file:
    if st.button("Upload"):
        with st.spinner("Uploading..."):
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
            try:
                response = requests.post("http://localhost:8000/upload", files=files)
                if response.status_code == 200:
                    st.success(response.json().get("message", "Uploaded successfully!"))
                else:
                    st.error(f"Upload failed: {response.text}")
            except Exception as e:
                st.error(f"Connection error: {e}")

st.divider()

# Action selection
action = st.radio(
    "Choose an action:",
    ["Summarize PDF", "Ask a question"]
)

if action == "Summarize PDF":
    if st.button("Generate summary"):
        with st.spinner("Summarizing..."):
            try:
                response = requests.post("http://localhost:8000/summarize")
                if response.status_code == 200:
                    st.subheader("Summary")
                    st.write(response.json()["summary"])
                else:
                    st.error(f"Error: {response.json().get('error', response.text)}")
            except Exception as e:
                st.error(f"Connection error: {e}")

if action == "Ask a question":
    question = st.text_input("Enter your question")

    if st.button("Ask") and question:
        with st.spinner("Answering..."):
            try:
                response = requests.post(
                    "http://localhost:8000/ask",
                    json={"question": question}
                )
                if response.status_code == 200:
                    if "error" in response.json():
                        st.error(response.json()["error"])
                    else:
                        st.subheader("Answer")
                        st.write(response.json()["answer"])
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Connection error: {e}")
