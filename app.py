import streamlit as st
import base64
from src.prediction import predict_crop


#  PAGE CONFIG 
st.set_page_config(
    page_title="Smart Agriculture Advisor",
    page_icon="🌱",
    layout="wide"
)

# BACKGROUND IMAGE 
def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: 100% 100%;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("Background.png")

#  CSS 
st.markdown("""
<style>
/* General */
.card {
    background-color: rgba(255, 255, 255, 0.92);
    color: black !important;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
    text-align: center;
    min-height: 170px;
    margin-bottom: 15px;
}


.header {
    background-color: rgba(255,255,255,0.92);
    padding: 10px;
    border-radius: 15px;
    margin-top: 5px;
    margin-bottom: 10px;
    text-align: center;
    
}

.big {
    font-size: 32px;
    font-weight: bold;
}

.sub {
    font-size: 16px;
    color: #555;
}
/* Make all input boxes white */
div[data-baseweb="input"] > div {
    background-color: white !important;
}

div[data-baseweb="input"] input {
    background-color: white !important;
    color: black !important;
}

/* Number input box background */
div[data-baseweb="base-input"] {
    background-color: white !important;
}

/* Dropdowns */
div[data-baseweb="select"] > div {
    background-color: white !important;
}

/* Remove transparency */
.stNumberInput input {
    background-color: white !important;
}

/* Label background styling */
label {
    background-color: black;
    padding: 4px 8px !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    color: white !important;
}

/* Extra fix for Streamlit labels */
.stNumberInput label,
.stTextInput label,
.stSelectbox label {
    background-color: black;
    padding: 4px 8px !important;
    border-radius: 6px !important;
    color: white !important;
}

/* Orange Predict Button */
div.stButton > button {
    background-color: #ff7f00 !important;   /* Orange */
    color: white !important;               /* White text */
    font-weight: bold;
    border-radius: 10px;
    height: 45px;
    border: none;
}

/* Hover Effect */
div.stButton > button:hover {
    background-color: #e67300 !important;  /* Darker orange on hover */
    color: white !important;
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

# HEADER 
st.markdown("""
<style>
.header-container {
    background: linear-gradient(90deg, #1e7f3f, #2ecc71);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 20px;
}
.header-container h1 {
    margin: 0;
    font-size: 36px;
}
.header-container p {
    margin: 5px 0 0 0;
    font-size: 18px;
}
</style>

<div class="header-container">
    <h1>🌱 Smart Agriculture Advisor</h1>
    <p>AI-Powered Crop Recommendation System</p>
</div>
""", unsafe_allow_html=True)

# INPUT CARD 
st.markdown("""
<div style="
    background-color: rgba(255,255,255,0.95);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
    color: black !important;
">
<h3>🧪 Enter Soil & Weather Details</h3>
</div>
""", unsafe_allow_html=True)

# INPUT SECTION 
col1, col2, col3 = st.columns(3)
N = col1.number_input("Nitrogen (N)", 0, 140, 70)
P = col2.number_input("Phosphorus (P)", 0, 145, 40)
K = col3.number_input("Potassium (K)", 0, 205, 35)

col4, col5, col6, col7 = st.columns(4)
temp = col4.number_input("Temperature (°C)", 0.0, 60.0, 28.0)
humidity = col5.number_input("Humidity (%)", 0.0, 100.0, 65.0)
ph = col6.number_input("pH Level", 0.0, 14.0, 6.5)
rainfall = col7.number_input("Rainfall (mm)", 0.0, 300.0, 100.0)


#  BUTTON 
col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])
with col_btn2:
    predict = st.button("🌾 Predict Crop", use_container_width=True)

st.write("")
#  DASHBOARD OUTPUT 
crop_tips = {

    "apple": "Requires cool climate and well-drained loamy soil. Prune regularly and ensure proper irrigation.",
    
    "banana": "Prefers warm and humid climate. Apply potassium-rich fertilizer and maintain proper drainage.",
    
    "blackgram": "Grows well in warm climate with moderate rainfall. Avoid waterlogging and use phosphorus fertilizer.",
    
    "chickpea": "Requires cool dry climate. Avoid excessive nitrogen fertilizer and ensure proper drainage.",
    
    "coconut": "Needs tropical climate and sandy loam soil. Provide regular irrigation and organic manure.",
    
    "coffee": "Requires moderate rainfall and shade. Maintain slightly acidic soil and proper pruning.",
    
    "cotton": "Needs warm temperature and moderate rainfall. Apply balanced NPK fertilizer and ensure good drainage.",
    
    "grapes": "Requires warm dry climate. Proper pruning and potassium fertilization improves fruit quality.",
    
    "jute": "Grows well in warm humid climate with high rainfall. Ensure fertile alluvial soil.",
    
    "kidneybeans": "Requires moderate rainfall and well-drained soil. Avoid excessive nitrogen.",
    
    "lentil": "Prefers cool season and dry climate. Requires less water and good drainage.",
    
    "maize": "Needs moderate rainfall and well-drained soil. Apply nitrogen-rich fertilizer.",
    
    "mango": "Requires tropical climate and well-drained soil. Avoid water stagnation.",
    
    "mothbeans": "Grows in dry and arid regions. Requires less irrigation and sandy soil.",
    
    "mungbean": "Prefers warm climate. Ensure proper drainage and phosphorus-rich fertilizer.",
    
    "muskmelon": "Requires warm dry climate and sandy loam soil. Avoid overwatering.",
    
    "orange": "Needs well-drained soil and moderate climate. Apply organic manure regularly.",
    
    "papaya": "Requires warm humid climate. Avoid waterlogging and use balanced fertilizers.",
    
    "pigeonpeas": "Grows well in semi-arid climate. Requires less irrigation and nitrogen fixation.",
    
    "pomegranate": "Prefers dry climate. Requires well-drained soil and controlled irrigation.",
    
    "rice": "Requires high rainfall and standing water during early growth stage.",
    
    "watermelon": "Needs warm climate and sandy soil. Avoid excessive watering."
}

if predict:

    crop = predict_crop(N, P, K, temp, humidity, ph, rainfall)

    tips = crop_tips.get(crop.lower(),
                         "Follow recommended agricultural practices.")
    
    
    soil_status = "Balanced"

    if N < 50:
        soil_status = "Low Nitrogen"
    elif P < 40:
        soil_status = "Low Phosphorus"
    elif K < 40:
        soil_status = "Low Potassium"


    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)

    # -------- Row 1 --------
    with row1_col1:
        st.markdown(f"""
        <div class="card">
            <h3>🌾 Recommended Crop</h3>
            <p class="big">{crop.upper()}</p>
        </div>
        """, unsafe_allow_html=True)

    with row1_col2:
        st.markdown(f"""
        <div class="card">
            <h3>🌱 Soil Condition</h3>
            <p>pH Level: {ph}</p>
            <p>Soil Status: {soil_status}</p>
              
        </div>
        """, unsafe_allow_html=True)

    # -------- Row 2 --------
    with row2_col1:
        st.markdown(f"""
        <div class="card">
            <h3>☀️ Weather Details</h3>
            <p>Temperature: {temp} °C</p>
            <p>Humidity: {humidity} %</p>
            <p>Rainfall: {rainfall} mm</p>
        </div>
        """, unsafe_allow_html=True)

    with row2_col2:
        st.markdown(f"""
        <div class="card">
            <h3>📋 Farming Tips</h3>
            <p>{tips}</p>
        </div>
        """, unsafe_allow_html=True)


# FOOTER 
st.write("")

st.markdown("""
<div style="
    text-align:center; 
    color:white; 
    font-size:15px; 
    background: linear-gradient(90deg, #1e7f3f, #2ecc71);
    padding:15px; 
    border-radius:10px;
    margin-top:30px;
">
    🚀 Model Accuracy: 92% &nbsp;       | &nbsp; AI Crop Recommender &nbsp;        | &nbsp; Updated:  March 2026
</div>
""", unsafe_allow_html=True)

