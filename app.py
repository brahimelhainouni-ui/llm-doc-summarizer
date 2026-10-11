import streamlit as st

from main import clean_adoc_text, summarize


st.title(" AsciiDoc Summarizer")

st.write("Upload an AsciiDoc file and get an AI-generated summary.")


uploaded_file = st.file_uploader(
    "Choose an AsciiDoc file",
    type=["adoc"]
)


if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")

    if st.button("Summarize"):

        document_text = uploaded_file.getvalue().decode("utf-8")

        cleaned_text = clean_adoc_text(document_text)

        with st.spinner("Creating summary..."):
            summary = summarize(cleaned_text)

        st.subheader("Summary")
        st.write(summary)

        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )
