import streamlit as st
from core.text_loader import load_resume
from core.text_cleaner import preprocess
from core.vector_model import build_vectors, compute_similarity
from core.scorer import keyword_score, final_score

st.set_page_config(page_title="AI Resume Matcher")

st.title("AI Resume Matcher & Compatibility Analyzer")

resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Evaluate Resume"):

    if resume_file and job_desc:

        resume_text = load_resume(resume_file)

        clean_resume = preprocess(resume_text)
        clean_jd = preprocess(job_desc)

        matrix = build_vectors(clean_resume, clean_jd)
        similarity = compute_similarity(matrix)

        keyword_match = keyword_score(clean_resume, clean_jd)

        final = final_score(similarity, keyword_match)

        st.subheader("Evaluation Results")
        st.write(f"Semantic Similarity: {similarity}%")
        st.write(f"Keyword Match Score: {keyword_match}%")
        st.success(f"Final Compatibility Score: {final}%")

    else:
        st.warning("Please upload resume and enter job description.")