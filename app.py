import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.graph_objects as go
import os

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Vijayadharshan R",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------
# LOAD CSS
# ----------------------------------------------------

def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# ----------------------------------------------------
# NAVIGATION
# ----------------------------------------------------

selected = option_menu(
    None,
    ["Home", "About", "Skills", "Projects", "Education", "Certificates", "Contact"],
    icons=[
        "house",
        "person",
        "cpu",
        "rocket",
        "book",
        "award",
        "telephone",
    ],
    orientation="horizontal",
)

# ----------------------------------------------------
# HOME
# ----------------------------------------------------

if selected == "Home":

    left, right = st.columns([1, 2])

    with left:

        if os.path.exists("profile_image.png"):
            image = Image.open("profile_image.png")
            st.image(image, width=300)

    with right:

        st.markdown("<h4>HELLO 👋</h4>", unsafe_allow_html=True)

        st.markdown(
            """
            <h1 class='gradient'>
            Vijayadharshan R
            </h1>
            """,
            unsafe_allow_html=True,
        )

        st.subheader("AI Engineer")
        st.subheader("Machine Learning Developer")
        st.subheader("Data Scientist")

        st.write(
            """
Artificial Intelligence & Data Science undergraduate passionate about
building intelligent AI-powered applications using Machine Learning,
Python and Data Science.
"""
        )

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                "📄 Download Resume",
                open("resume.pdf", "rb"),
                file_name="Resume.pdf",
            )

        with col2:
            st.link_button(
                "💻 GitHub",
                "https://github.com/"
            )

st.markdown("---")

# ----------------------------------------------------
# ABOUT
# ----------------------------------------------------

if selected == "About":

    st.title("About Me")

    st.write(
        """
Artificial Intelligence & Data Science undergraduate with a strong
passion for solving real-world problems using Artificial Intelligence,
Machine Learning and Data Science.

I enjoy creating intelligent systems, beautiful dashboards and
interactive applications using Python and Streamlit.
"""
    )

st.markdown("---")

# ----------------------------------------------------
# SKILLS
# ----------------------------------------------------

if selected == "Skills":

    st.title("Technical Skills")

    skills = {
        "Java":95,
        "Python":92,
        "Machine Learning":90,
        "Data Science":90,
        "SQL":82,
        "Power BI":80,
        "HTML/CSS":85,
        "JavaScript":75
    }

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=list(skills.keys()),
            y=list(skills.values())
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        title="Skill Levels"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ----------------------------------------------------
# PROJECTS
# ----------------------------------------------------

if selected == "Projects":

    st.title("Projects")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("☕ Coffee Sales Prediction")

        st.write("""
✔ Linear Regression

✔ Streamlit

✔ Sales Forecast

✔ Temperature Analysis

✔ Customer Prediction
""")

    with col2:

        st.subheader("🛡 Insurance Prediction")

        st.write("""
✔ Logistic Regression

✔ Classification

✔ Streamlit

✔ Customer Prediction

✔ ML Deployment
""")

st.markdown("---")

# ----------------------------------------------------
# EDUCATION
# ----------------------------------------------------

if selected == "Education":

    st.title("Education")

    st.info("""
🎓 B.Tech AI & DS

Rathinam Technical Campus

2024 - Present
""")

    st.success("""
HSC

70%
""")

    st.warning("""
SSLC

58%
""")

st.markdown("---")

# ----------------------------------------------------
# CERTIFICATES
# ----------------------------------------------------

if selected == "Certificates":

    st.title("Certificates")

    certificates = [
        "IBM AI",
        "IBM Data Science",
        "Java HackerRank",
        "Power BI",
        "Git & GitHub",
        "HTML & CSS",
        "Ethical Hacking",
        "Design Thinking",
        "Excel",
        "AI Internship"
    ]

    cols = st.columns(2)

    for i, cert in enumerate(certificates):
        cols[i % 2].success(cert)

st.markdown("---")

# ----------------------------------------------------
# CONTACT
# ----------------------------------------------------

if selected == "Contact":

    st.title("Contact")

    st.write("📧 dharshanvijay7727@gmail.com")

    st.write("📱 +91 6384227515")

    st.write("📍 Coimbatore")

    st.link_button("LinkedIn", "https://linkedin.com")

    st.link_button("GitHub", "https://github.com")

st.markdown("---")

st.caption("© 2026 Vijayadharshan R | Built with Streamlit")
