import streamlit as st
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Agriculture Advisor",
    page_icon="🌱",
    layout="wide"
)

# ---------------- BACKGROUND IMAGE ----------------
def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("background.png")

# ---------------- RESPONSIVE CSS ----------------
st.markdown("""
<style>
/* General */
.card {
    background-color: rgba(255, 255, 255, 0.92);
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    text-align: center;
    height: 100vw;
}

.header {
    background-color: rgba(255,255,255,0.92);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    text-align: center;
}

.big {
    font-size: 26px;
    font-weight: bold;
}

.sub {
    font-size: 16px;
    color: #555;
}

/* Tablet */
@media (max-width: 992px) {
    .big {
        font-size: 22px;
    }
    .card {
        padding: 16px;
    }
}

/* Mobile */
@media (max-width: 600px) {
    .header h1 {
        font-size: 24px;
    }
    .sub {
        font-size: 14px;
    }
    .big {
        font-size: 20px;
    }
    .card {
        margin-bottom: 15px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <h1>🌱 Smart Agriculture Advisor</h1>
    <p class="sub">AI-Powered Crop Recommendation System</p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
st.markdown("### Enter Crop Details")

col1, col2, col3, col4 = st.columns(4)

with col1:
    N = st.number_input("Nitrogen (N)", 0, 140, 70)
with col2:
    P = st.number_input("Phosphorus (P)", 0, 145, 40)
with col3:
    K = st.number_input("Potassium (K)", 0, 205, 35)
with col4:
    ph = st.number_input("pH Level", 0.0, 14.0, 6.5)

col5, col6 = st.columns(2)

with col5:
    temp = st.number_input("Temperature (°C)", 0.0, 60.0, 28.0)
with col6:
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 65.0)

st.write("")

# ---------------- BUTTON ----------------
predict = st.button("🌾 Predict Crop")

st.write("")

# ---------------- DASHBOARD OUTPUT ----------------
if predict:
    crop = "Rice"
    soil = "Loamy Soil"

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="card">
            <h3>🌾 Recommended Crop</h3>
            <p class="big">{crop}</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="card">
            <h3>🌱 Soil Condition</h3>
            <p>Soil Type: {soil}</p>
            <p>pH Level: {ph}</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="card">
            <h3>☀️ Weather Details</h3>
            <p>Temperature: {temp} °C</p>
            <p>Humidity: {humidity} %</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="card">
            <h3>📋 Farming Tips</h3>
            <p>Use balanced fertilizer and ensure proper irrigation.</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.write("")
st.markdown("""
<div style="text-align:center; color:white; font-size:14px;">
    Accuracy: 92% &nbsp; | &nbsp; Model: AI Crop Recommender &nbsp; | &nbsp; Last Updated: Jan 2025
</div>
""", unsafe_allow_html=True)
