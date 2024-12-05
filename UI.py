import streamlit as st
import joblib
import numpy as np

# Load the trained AdaBoost model
model = joblib.load('adaboost_model.pkl')

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        font-size:36px;
        font-weight:bold;
        text-align:center;
        color:#5b2a8c;
        margin-bottom: 20px;
    }
    .subheader {
        font-size:18px;
        text-align:center;
        color:#34495e;
        margin-bottom: 30px;
    }
    .predict-btn {
        background-color: #3498db;
        color: white;
        padding: 10px 25px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        margin-top: 20px;
    }
    .predict-btn:hover {
        background-color: #2980b9;
    }
    .result {
        font-size:24px;
        font-weight:bold;
        text-align:center;
        margin-top:20px;
    }
    .footer {
        font-size:16px;
        color: #ffffff;
        background: linear-gradient(90deg, #2E86C1, #5DADE2);
        text-align: center;
        padding: 15px 0;
        border-top: 2px solid #154360;
        margin-top: 50px;
    }
    .animation-container {
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Subheader
st.markdown('<p class="title">🌧️ Rain  Prediction System</p>', unsafe_allow_html=True)

# Create input form with collapsible sections
with st.expander("Enter Weather Details", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0, step=0.1, help="Enter the rainfall in mm.")
        wind_gust_speed = st.number_input("💨 Wind Gust Speed (km/h)", min_value=0.0, step=0.1, help="Enter the wind gust speed in km/h.")
        humidity_9am = st.number_input("💧 Humidity at 9am (%)", min_value=0, max_value=100, help="Enter the humidity level at 9am.")

    with col2:
        humidity_3pm = st.number_input("💧 Humidity at 3pm (%)", min_value=0, max_value=100, help="Enter the humidity level at 3pm.")
        cloud_9am = st.number_input("☁️ Cloud Cover at 9am (oktas)", min_value=0, max_value=8, help="Enter the cloud cover at 9am in oktas.")
        cloud_3pm = st.number_input("☁️ Cloud Cover at 3pm (oktas)", min_value=0, max_value=8, help="Enter the cloud cover at 3pm in oktas.")

# Add a prediction button
if st.button("🌟 Predict"):
    # Prepare input data as a 2D array
    input_data = np.array([[rainfall, wind_gust_speed, humidity_9am, humidity_3pm, cloud_9am, cloud_3pm]])

    # Add a spinner for loading effect
    with st.spinner("Calculating Prediction..."):
        prediction = model.predict(input_data)
    
    # Display prediction result dynamically with animations
    if prediction[0] == 1:  # Rain
        st.markdown('<p class="result" style="color:#e74c3c;">🌧️ Prediction: Rain</p>', unsafe_allow_html=True)
        
    else:  # No Rain
        st.markdown('<p class="result" style="color:#27ae60;">☀️ Prediction: No Rain</p>', unsafe_allow_html=True)
        
# Footer
st.markdown(
    """
    <div class="footer">
        © 2024 Rain Prediction System | Developed by <span style='color: #FAD7A0;'>ChandraPrakash</span>, 
        <span style='color: #FAD7A0;'>Vivek</span>, and <span style='color: #FAD7A0;'>Hrishikesh</span>
    </div>
    """,
    unsafe_allow_html=True
)
