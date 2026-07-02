import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Vijayadharshan | AI Portfolio",
    page_icon="🤖",
    layout="wide",
)

# ---------------- CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html,body,[class*="css"]{
    font-family:'Poppins',sans-serif;
}

.stApp{
background:linear-gradient(-45deg,#0f172a,#111827,#1e3a8a,#0f172a);
background-size:400% 400%;
animation:gradient 15s ease infinite;
color:white;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.glass{
background:rgba(255,255,255,0.08);
padding:25px;
border-radius:20px;
backdrop-filter:blur(15px);
border:1px solid rgba(255,255,255,0.15);
box-shadow:0 10px 25px rgba(0,0,0,.4);
}

.title{
font-size:50px;
font-weight:700;
color:#00E5FF;
}

.subtitle{
font-size:22px;
color:#dddddd;
}

.skill{
background:#222;
border-radius:15px;
margin-bottom:18px;
}

.bar{
background:linear-gradient(90deg,#00E5FF,#00FFB3);
padding:8px;
border-radius:15px;
color:black;
font-weight:bold;
text-align:center;
}

.project{
background:#16213e;
padding:20px;
border-radius:20px;
transition:.3s;
}

.project:hover{
transform:translateY(-8px);
box-shadow:0 0 25px cyan;
}

h2{
color:#00E5FF;
}

a{
text-decoration:none;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Sidebar ----------------
with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Home", "About", "Education", "Skills", "Projects", "Certificates", "Contact"],
        icons=["house", "person", "book", "cpu", "code-square", "award", "envelope"],
        default_index=0,
    )

# ---------------- HOME ----------------
if selected == "Home":

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "https://avatars.githubusercontent.com/u/9919?s=200&v=4",
            width=220,
        )

    with col2:
        st.markdown("<div class='title'>VIJAYADHARSHAN R</div>", unsafe_allow_html=True)

        st.markdown(
            "<div class='subtitle'>Aspiring AI Engineer • Data Scientist • Machine Learning Developer</div>",
            unsafe_allow_html=True,
        )

        st.write("")

        st.write(
            """
Artificial Intelligence & Data Science undergraduate passionate about
Machine Learning, Artificial Intelligence, Data Analytics and Full Stack Development.

I enjoy solving real-world problems with data and building intelligent applications.
"""
        )

        colA, colB = st.columns(2)

        with colA:
            st.link_button("GitHub", "https://github.com/")

        with colB:
            st.link_button("LinkedIn", "https://linkedin.com/")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ABOUT ----------------
elif selected == "About":

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.header("About Me")

    st.write("""
I'm currently pursuing **B.Tech in Artificial Intelligence & Data Science**.

My interests include:

- Artificial Intelligence
- Machine Learning
- Data Science
- Deep Learning
- Java Programming
- Python Development
- Cloud Computing

I love building intelligent applications using Streamlit and Python.
""")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------
elif selected == "Education":

    st.header("Education")

    st.markdown("""
### 🎓 B.Tech Artificial Intelligence & Data Science

**Rathinam Technical Campus**

2024 - 2028

---

### 🎓 HSC

Karthi Vidhyala Matric Hr. Sec. School

70%

---

### 🎓 SSLC

Karthi Vidhyala Matric Hr. Sec. School

58%
""")

# ---------------- SKILLS ----------------
elif selected == "Skills":

    st.header("Technical Skills")

    skills = {
        "Python":95,
        "Java":92,
        "Machine Learning":90,
        "Data Science":90,
        "Streamlit":90,
        "Git & GitHub":88,
        "Power BI":85,
        "AWS":75,
        "SQL":85,
        "HTML/CSS":80
    }

    for skill, percent in skills.items():

        st.write(skill)

        st.markdown(f"""
<div class='skill'>
<div class='bar' style='width:{percent}%'>
{percent}%
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif selected == "Projects":

    st.header("Projects")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
<div class='project'>

## ☕ Coffee Sales Prediction

✔ Linear Regression

✔ Streamlit

✔ Machine Learning

Predict coffee sales based on:

- Temperature
- Weather
- Staff
- Promotions
- Customers

</div>
""", unsafe_allow_html=True)

    with col2:

        st.markdown("""
<div class='project'>

## 🏥 Insurance Prediction

✔ Logistic Regression

✔ Classification

✔ Streamlit

Predict whether customer purchases insurance.

</div>
""", unsafe_allow_html=True)

# ---------------- CERTIFICATES ----------------
elif selected == "Certificates":

    st.header("Certificates")

    certs = [

        "IBM Data Science",

        "IBM Artificial Intelligence",

        "Java - HackerRank",

        "Git & GitHub - Google",

        "Power BI",

        "Excel",

        "Ethical Hacking",

        "Design Thinking",

        "Elevate Labs AI Internship"

    ]

    for c in certs:

        st.success("🏆 " + c)

# ---------------- CONTACT ----------------
elif selected == "Contact":

    st.header("Contact")

    st.info("📧 dharshanvijay7727@gmail.com")

    st.info("📱 +91 6384227515")

    st.info("📍 Coimbatore, Tamil Nadu")

    st.link_button("GitHub", "https://github.com/")

    st.link_button("LinkedIn", "https://linkedin.com/")

st.markdown("---")
st.caption("© 2026 Vijayadharshan R | AI Engineer Portfolio")
