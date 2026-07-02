import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from pathlib import Path
import base64

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Vijayadharshan R | AI Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------------------------------
# LOAD CSS
# -------------------------------------------------

def load_css():
    css_file = Path("style.css")
    if css_file.exists():
        st.markdown(
            f"<style>{css_file.read_text()}</style>",
            unsafe_allow_html=True,
        )

load_css()

# -------------------------------------------------
# HELPERS
# -------------------------------------------------

def file_exists(path):
    return Path(path).exists()


def download_resume():
    resume = Path("assets/resume.pdf")

    if resume.exists():
        with open(resume, "rb") as pdf:
            st.download_button(
                "📄 Download Resume",
                pdf,
                file_name="Vijayadharshan_Resume.pdf",
                mime="application/pdf",
            )


# -------------------------------------------------
# NAVBAR
# -------------------------------------------------

selected = option_menu(
    None,
    [
        "Home",
        "About",
        "Skills",
        "Projects",
        "Education",
        "Certificates",
        "Contact",
    ],
    icons=[
        "house",
        "person",
        "cpu",
        "rocket",
        "book",
        "award",
        "envelope",
    ],
    default_index=0,
    orientation="horizontal",
)

# -------------------------------------------------
# THEME TOGGLE
# -------------------------------------------------

if "dark" not in st.session_state:
    st.session_state.dark = True

col_theme, _ = st.columns([1, 6])

with col_theme:

    if st.toggle("🌙 Dark Mode", value=True):
        st.session_state.dark = True
    else:
        st.session_state.dark = False

# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------

if selected == "Home":

    left, right = st.columns([1, 2], gap="large")

    with left:

        profile = Path("assets/profile.png")

        if profile.exists():
            st.image(Image.open(profile), use_container_width=True)
        else:
            st.info("Add assets/profile.png")

    with right:

        st.markdown(
            """
            <div class="hero-small">
            👋 Hello, I'm
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero-title">
            Vijayadharshan R
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero-sub">
            AI Engineer • Machine Learning Developer • Data Scientist
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        st.write(
            """
Artificial Intelligence & Data Science undergraduate passionate
about building intelligent AI-powered applications.

I enjoy Machine Learning, Data Analytics,
Deep Learning, Python, Java and Streamlit.
"""
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            download_resume()

        with c2:
            st.link_button(
                "GitHub",
                "https://github.com/yourusername",
                use_container_width=True,
            )

        with c3:
            st.link_button(
                "LinkedIn",
                "https://linkedin.com/in/yourusername",
                use_container_width=True,
            )

# -------------------------------------------------
# STATS
# -------------------------------------------------

st.write("")

a, b, c, d = st.columns(4)

a.metric("Projects", "2+")
b.metric("Certificates", "10+")
c.metric("Languages", "6+")
d.metric("Experience", "AI & DS")

st.divider()

# -------------------------------------------------
# PLACEHOLDERS
# -------------------------------------------------

if selected == "About":
    st.title("👨 About Me")
    st.info("About section will be added in Part 2.")

elif selected == "Skills":
    st.title("🛠 Skills")
    st.info("Interactive Plotly dashboard coming in Part 2.")

elif selected == "Projects":
    st.title("🚀 Projects")
    st.info("Premium project cards coming in Part 2.")

elif selected == "Education":
    st.title("🎓 Education")
    st.info("Timeline section coming in Part 2.")

elif selected == "Certificates":
    st.title("🏆 Certificates")
    st.info("Glassmorphism certificate cards coming in Part 2.")

elif selected == "Contact":
    st.title("📬 Contact")
    st.info("Animated contact section coming in Part 2.")

st.divider()

st.caption("© 2026 Vijayadharshan R • Built with Streamlit")
