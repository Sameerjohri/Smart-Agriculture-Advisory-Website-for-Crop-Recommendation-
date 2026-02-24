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

div.block-container {
    padding-top: 3rem ;
}
.card {
    background: linear-gradient(90deg, #ADD8E6, #FFFFFF);
    color: black !important;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
    text-align: center;
    min-height: 170px;
    margin-bottom: 20px;
    animation: fadeIn 0.6s ease-in-out;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}


.header {
    background-color: rgba(255,255,255,0.92);
    padding: 5px;
    border-radius: 15px;
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
    color: white ;
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

div.stButton > button {
    background: linear-gradient(90deg, #ff7f00, #ff9a1f) !important;
    color: white !important;
    font-weight: bold;
    border-radius: 12px;
    height: 50px;
    border: none;
    font-size: 16px;
    transition: 0.3s ease-in-out;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #e67300, #ff7f00) !important;
    transform: scale(1.02);
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
    background: linear-gradient(90deg, #1e7f3f, #f1c40f);
    border-radius: 15px;
    text-align: center;
    margin:0 0 20px 0;
}
.header-container h1 {
    font-size: 42px;
    color: green;
    text-shadow: 
        -1px -1px 0 black,
         1px -1px 0 black,
        -1px  1px 0 black,
         1px  1px 0 black;
}
.header-container p {
    font-size: 18px;
    color: green;
    text-shadow: 
        -1px -1px 0 black,
         1px -1px 0 black,
        -1px  1px 0 black,
         1px  1px 0 black;
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
    background-color: rgba(255,255,255,0.70);
    padding: 0px;
    border-radius: 15px;
    margin-bottom: 20px;
    color: black;
">
<h3>🧪 Enter Soil & Weather Details</h3>
</div>
""", unsafe_allow_html=True)

# INPUT SECTION 
col1, col2, col3 = st.columns(3)
N = col1.number_input("Nitrogen (N)", min_value=0, max_value=140, value=None, placeholder="Enter Nitrogen")
P = col2.number_input("Phosphorus (P)", min_value=0, max_value=145, value=None, placeholder="Enter Phosphorus")
K = col3.number_input("Potassium (K)", min_value=0, max_value=205, value=None, placeholder="Enter Potassium")
col4, col5, col6, col7 = st.columns(4)
temp = col4.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=None, placeholder="Enter Temperature")
humidity = col5.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=None, placeholder="Enter Humidity")
ph = col6.number_input("pH Level", min_value=0.0, max_value=14.0, value=None, placeholder="Enter pH")
rainfall = col7.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=None, placeholder="Enter Rainfall")


all_filled = None not in (N, P, K, temp, humidity, ph, rainfall)

#  BUTTON 
col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])
with col_btn2:
    predict = st.button(
        "🌾 Predict Crop",
        use_container_width=True,
        key="predict_btn",
        disabled=not all_filled
    )

if not all_filled:
    st.markdown("""
    <div style="
        background-color: rgba(255, 255, 0,0.45);
        border-radius: 10px;
        color: red;
        font-weight: 700;
        text-shadow: 1px 1px 1px rgba(0,0,0,1);
        margin-top: 10px;
        text-align: center;
    ">
        ℹ Please fill all input fields to enable prediction.
    </div>
    """, unsafe_allow_html=True)
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
    if None in (N, P, K, temp, humidity, ph, rainfall):
        st.warning("⚠ Please fill all input fields before prediction.")
    else:
      with st.spinner("🔍 Analyzing soil and climate data..."):
        crop = predict_crop(N, P, K, temp, humidity, ph, rainfall)

        st.markdown("""
<div style="
    background-color: rgba(0,255,0,0.95);
    padding: 14px 18px;
    border-radius: 12px;
    color: black;
    font-weight: 600;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    margin: 15px 0;
    text-align: center;
">
    ✅ Prediction generated successfully!
</div>
""", unsafe_allow_html=True)

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

