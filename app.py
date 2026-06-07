import streamlit as st
import plotly.express as px
import nltk

# ==========================
# IMPORT MODULES
# ==========================

from modules.pdf_parser import extract_text_from_pdf
from modules.similarity import calculate_similarity
from modules.skill_extractor import extract_skills
from modules.ats_score import calculate_ats_score
from modules.section_checker import check_sections
from modules.suggestions import generate_suggestions
from modules.report_generator import generate_report


# ==========================
# NLTK DOWNLOADS
# ==========================

nltk.download("punkt")
nltk.download("stopwords")


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 40%,
        #0f172a 100%
    );
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(
    180deg,
    #111827,
    #1f2937
    );
}

/* Metric Cards */
[data-testid="metric-container"]{
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
}

/* Upload Area */
section[data-testid="stFileUploader"]{
    background: rgba(255,255,255,0.03);
    padding: 15px;
    border-radius: 15px;
}

/* Buttons */
.stButton > button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    background:linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color:white;
}

/* Success Messages */
.stSuccess{
    border-radius:12px;
}

/* Info Messages */
.stInfo{
    border-radius:12px;
}

/* Warning Messages */
.stWarning{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)


# ==========================
# CUSTOM HEADER
# ==========================

st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:linear-gradient(
90deg,
#2563eb,
#7c3aed
);
text-align:center;
margin-bottom:20px;
">

<h1 style="
color:white;
font-size:50px;
">
🚀 AI Resume Analyzer
</h1>

<h3 style="
color:white;
">
ATS Score • Skill Gap Analysis • Resume Improvement
</h3>

<p style="
color:white;
font-size:18px;
">
Upload your Resume and compare it with a Job Description
</p>

</div>
""", unsafe_allow_html=True)


# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.header("📌 About Project")

    st.info(
        """
        AI Resume Analyzer helps you:

        ✅ ATS Score Calculation

        ✅ Resume Matching

        ✅ Skill Gap Analysis

        ✅ Resume Section Analysis

        ✅ Improvement Suggestions
        """
    )

    st.header("📖 How To Use")

    st.write(
        """
        1. Upload Resume PDF

        2. Paste Job Description

        3. Click Analyze Resume

        4. Review Results
        """
    )


# ==========================
# FILE UPLOAD
# ==========================

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "📝 Paste Job Description",
    height=250
)


# ==========================
# ANALYZE BUTTON
# ==========================

if st.button("🚀 Analyze Resume"):

    if not uploaded_file:

        st.warning("Please upload a resume.")

        st.stop()

    if not job_description:

        st.warning("Please paste a Job Description.")

        st.stop()

    with st.spinner("Analyzing Resume..."):

        # ==========================
        # EXTRACT TEXT
        # ==========================

        resume_text = extract_text_from_pdf(
            uploaded_file
        )

        if not resume_text:

            st.error(
                "Unable to extract text from PDF."
            )

            st.stop()

        # ==========================
        # SIMILARITY SCORE
        # ==========================

        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        # ==========================
        # SKILL EXTRACTION
        # ==========================

        resume_skills = set(
            extract_skills(
                resume_text
            )
        )

        job_skills = set(
            extract_skills(
                job_description
            )
        )

        matched_skills = (
            resume_skills &
            job_skills
        )

        missing_skills = (
            job_skills -
            resume_skills
        )

        # ==========================
        # ATS SCORE
        # ==========================

        ats_score = calculate_ats_score(
            similarity_score,
            matched_skills,
            len(job_skills)
        )

        # ==========================
        # SECTION ANALYSIS
        # ==========================

        missing_sections = check_sections(
            resume_text
        )

        # ==========================
        # SUGGESTIONS
        # ==========================

        suggestions = generate_suggestions(
            missing_skills,
            missing_sections
        )
        report = generate_report(
         ats_score,
         similarity_score,
         matched_skills,
         missing_skills,
         missing_sections,
         suggestions
  )

        # ==========================
        # DASHBOARD
        # ==========================

        st.markdown("---")

        st.header("📊 Resume Dashboard")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "ATS Score",
                f"{ats_score}%"
            )

        with col2:

            st.metric(
                "Match Score",
                f"{similarity_score}%"
            )

        with col3:

            st.metric(
                "Matched Skills",
                len(matched_skills)
            )

        with col4:

            st.metric(
                "Missing Skills",
                len(missing_skills)
            )

        # ==========================
        # RESUME RATING
        # ==========================

        if ats_score >= 85:

            rating = "🏆 Excellent"

        elif ats_score >= 70:

            rating = "🥇 Good"

        elif ats_score >= 50:

            rating = "⚠ Average"

        else:

            rating = "❌ Needs Improvement"

        st.subheader("Resume Rating")

        st.success(rating)

        # ==========================
        # PROGRESS BARS
        # ==========================

        st.subheader("📈 ATS Strength")

        st.progress(
            int(ats_score)
        )

        st.write(
            f"{ats_score}%"
        )

        st.subheader("🎯 Resume Match")

        st.progress(
            int(similarity_score)
        )

        st.write(
            f"{similarity_score}%"
        )

        # ==========================
        # PIE CHART
        # ==========================

        st.subheader(
            "📊 Skill Analysis"
        )

        fig = px.pie(
            values=[
                len(matched_skills),
                len(missing_skills)
            ],
            names=[
                "Matched Skills",
                "Missing Skills"
            ],
            title="Skill Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ==========================
        # MATCHED SKILLS
        # ==========================

        st.subheader(
            "✅ Matched Skills"
        )

        if matched_skills:

            for skill in sorted(
                matched_skills
            ):

                st.success(
                    f"✅ {skill}"
                )

        else:

            st.warning(
                "No matching skills found."
            )

        # ==========================
        # MISSING SKILLS
        # ==========================

        st.subheader(
            "❌ Missing Skills"
        )

        if missing_skills:

            for skill in sorted(
                missing_skills
            ):

                st.error(
                    f"❌ {skill}"
                )

        else:

            st.success(
                "No missing skills."
            )

        # ==========================
        # MISSING SECTIONS
        # ==========================

        st.subheader(
            "📌 Missing Resume Sections"
        )

        if missing_sections:

            for section in (
                missing_sections
            ):

                st.warning(
                    f"⚠ {section.title()}"
                )

        else:

            st.success(
                "All important sections found."
            )

        # ==========================
        # SUGGESTIONS
        # ==========================

        st.subheader(
            "💡 Improvement Suggestions"
        )

        if suggestions:

            for suggestion in suggestions:

                st.info(
                    suggestion
                )

        else:

            st.success(
                "Resume looks strong."
            )
                        

        # ==========================
        # FINAL RESULT
        # ==========================

        st.markdown("---")

        st.header("🎉 Analysis Completed")

        st.success(
            "Resume analyzed successfully."
        )

        # ==========================
        # DOWNLOAD REPORT
        # ==========================

        st.markdown("---")

        st.subheader(
            "📥 Download Analysis Report"
        )

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )
     
        