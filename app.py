# import streamlit as st
# import pandas as pd
# import pickle
# from datetime import datetime



# st.set_page_config(
#     page_title="Used Car Valuation Engine",
#     page_icon="🚗",
#     layout="wide"
# )

# st.title("Used Car Valuation & Depreciation Predictor")
# st.markdown("Estimate fair market resale value using ensemble regression on historical vehicle telemetry.")


# model = pickle.load(open("car_price_model.pkl", "rb"))


# st.markdown("""
# <style>

# .stApp{
#     background: #0b0b0b;
#     color: white;
# }


# #MainMenu, footer, header {
#     visibility: hidden;
# }


# .hero {
#     background: linear-gradient(
#         rgba(0,0,0,0.75),
#         rgba(0,0,0,0.75)
#     ),
#     url("https://images.unsplash.com/photo-1503376780353-7e6692767b70");

#     background-size: cover;
#     background-position: center;

#     padding: 90px 50px;
#     border-radius: 25px;
#     text-align: center;
#     margin-bottom: 25px;
# }

# .hero h1{
#     color:#FFD700;
#     font-size:65px;
#     font-weight:800;
# }

# .hero p{
#     font-size:22px;
#     color:white;
# }


# .card{
#     background: rgba(255,255,255,0.05);
#     border:1px solid rgba(255,215,0,0.25);
#     border-radius:20px;
#     padding:25px;
#     backdrop-filter: blur(10px);
#     box-shadow:0px 5px 20px rgba(255,215,0,0.15);
# }
            
#     label {
#     color: #FFD700 !important;
#     font-size: 18px !important;
#     font-weight: 600 !important;
# }


# .stSelectbox label {
#     color: #FFD700 !important;
# }


# .stNumberInput label {
#     color: #FFD700 !important;
# }


# section[data-testid="stSidebar"] * {
#     color: white;
# }


# .stat-box{
#     background:#111111;
#     border:1px solid #FFD700;
#     border-radius:15px;
#     padding:20px;
#     text-align:center;
# }


# .result{
#     background: linear-gradient(
#         135deg,
#         #FFD700,
#         #ffb700
#     );

#     color:black;
#     text-align:center;
#     padding:35px;
#     border-radius:20px;

#     box-shadow:0px 0px 40px rgba(255,215,0,0.6);
# }

# .result h1{
#     font-size:50px;
# }


# .stButton > button{
#     width:100%;
#     height:60px;

#     background: linear-gradient(
#         90deg,
#         #FFD700,
#         #ffb700
#     );

#     color:black;
#     font-size:20px;
#     font-weight:bold;

#     border:none;
#     border-radius:15px;
# }

# .stButton > button:hover{
#     transform:scale(1.02);
#     transition:0.3s;
# }


# section[data-testid="stSidebar"]{
#     background:#111111;
# }

# </style>
# """, unsafe_allow_html=True)

# st.markdown("""
# <div class="hero">
#     <h1>🚘 Luxury Car Price Predictor</h1>
#     <p>Vehicle Valuation System</p>
# </div>
# """, unsafe_allow_html=True)

# c1, c2, c3, c4 = st.columns(4)

# with c1:
#     st.markdown("""
#     <div class="stat-box">
#         <h3>🚗 Cars</h3>
#         <h2>10K+</h2>
#     </div>
#     """, unsafe_allow_html=True)

# with c2:
#     st.markdown("""
#     <div class="stat-box">
#         <h3>🤖 Model</h3>
#         <h2>ML</h2>
#     </div>
#     """, unsafe_allow_html=True)

# with c3:
#     st.markdown("""
#     <div class="stat-box">
#         <h3>⚡ Speed</h3>
#         <h2>< 1 sec</h2>
#     </div>
#     """, unsafe_allow_html=True)

# with c4:
#     st.markdown("""
#     <div class="stat-box">
#         <h3>🎯 Accuracy</h3>
#         <h2>95%+</h2>
#     </div>
#     """, unsafe_allow_html=True)

# st.write("")

# col1, col2 = st.columns(2)

# with col1:
#     year = st.number_input("Manufacturing Year", min_value=2000, max_value=2026, value=2018, step=1)
#     present_price = st.number_input("Current Ex-Showroom Price (in Lakhs ₹)", min_value=0.5, max_value=100.0, value=6.5, step=0.1)
#     kms_driven = st.number_input("Total Kilometers Driven", min_value=0, max_value=500000, value=35000, step=1000)
#     owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])

# with col2:
#     fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
#     seller_type = st.selectbox("Seller Category", ["Dealer", "Individual"])
#     transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])


#     st.markdown('</div>', unsafe_allow_html=True)


# car_age = datetime.now().year - year

# fuel_diesel = 1 if fuel_type == "Diesel" else 0
# fuel_petrol = 1 if fuel_type == "Petrol" else 0

# seller_individual = 1 if seller_type == "Individual" else 0
# transmission_manual = 1 if transmission == "Manual" else 0

# st.write("")


# if st.button("Predict"):

#     try:

#         features = pd.DataFrame(
#             [[
#                 present_price,
#                 kms_driven,                 
#                 owner,
#                 car_age,
#                 fuel_diesel,
#                 fuel_petrol,
#                 seller_individual,          
#                 transmission_manual
#             ]],
#             columns=[
#                 'Present_Price',
#                 'Driven_kms',
#                 'Owner',
#                 'Car_Age',
#                 'Fuel_Type_Diesel',
#                 'Fuel_Type_Petrol',
#                 'Selling_type_Individual',
#                 'Transmission_Manual'
#             ]
#         )

#         prediction = model.predict(features)[0]

#         st.markdown(f"""
#         <div class="result">
#             <h2>💰 Estimated Market Value</h2>
#             <h1>₹ {prediction:.2f} Lakhs</h1>
#         </div>
#         """, unsafe_allow_html=True)

#         st.subheader("Valuation vs. Original Showroom Price")
#         chart_data = pd.DataFrame({
#             "Valuation Stage": ["Original Showroom Price (Lakhs)", "Estimated Resale Value (Lakhs)"],
#             "Price (₹ Lakhs)": [present_price, round(float(prediction), 2)]
#         })
#         st.bar_chart(chart_data.set_index("Valuation Stage"))


#         st.success("Valuation Generated Successfully!")

#     except Exception as e:
#         st.error(f"Prediction Error: {e}")



# st.markdown("---")

import pickle
from datetime import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Used Car Valuation System",
    layout="centered"
)

MODEL_PATH = "car_price_model.pkl"

@st.cache_resource
def load_model(path: str):
    with open(path, "rb") as file:
        return pickle.load(file)

model = load_model(MODEL_PATH)

st.title("Used Car Valuation System")
st.caption("Resale price estimation powered by supervised ensemble regression.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Manufacturing Year", min_value=2000, max_value=2026, value=2018, step=1)
    present_price = st.number_input("Ex-Showroom Price (₹ Lakhs)", min_value=0.5, max_value=100.0, value=6.5, step=0.1)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, value=35000, step=1000)
    owner = st.selectbox("Previous Owners", [0, 1, 2, 3])

with col2:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

car_age = datetime.now().year - year
fuel_diesel = 1 if fuel_type == "Diesel" else 0
fuel_petrol = 1 if fuel_type == "Petrol" else 0
seller_individual = 1 if seller_type == "Individual" else 0
transmission_manual = 1 if transmission == "Manual" else 0

st.write("")

if st.button("Estimate Resale Value", type="primary", use_container_width=True):
    try:
        features = pd.DataFrame(
            [[
                present_price,
                kms_driven,
                owner,
                car_age,
                fuel_diesel,
                fuel_petrol,
                seller_individual,
                transmission_manual
            ]],
            columns=[
                "Present_Price",
                "Driven_kms",
                "Owner",
                "Car_Age",
                "Fuel_Type_Diesel",
                "Fuel_Type_Petrol",
                "Selling_type_Individual",
                "Transmission_Manual"
            ]
        )

        prediction = float(model.predict(features)[0])
        depreciation = prediction - present_price

        st.divider()
        st.metric(
            label="Estimated Market Resale Value",
            value=f"₹ {prediction:.2f} Lakhs",
            delta=f"{depreciation:.2f} Lakhs vs. Showroom Price"
        )

        chart_data = pd.DataFrame({
            "Stage": ["Ex-Showroom Price", "Estimated Resale Value"],
            "Price (₹ Lakhs)": [present_price, round(prediction, 2)]
        })
        st.bar_chart(chart_data.set_index("Stage"))

    except Exception as e:
        st.error(f"Prediction Error: {e}")

st.divider()
with st.expander("Model Architecture & Feature Pipeline"):
    st.markdown("""
    - **Task Type:** Supervised Tabular Regression
    - **Algorithm:** Random Forest Regressor
    - **Feature Engineering:** Temporal age calculation (`Car_Age`) and One-Hot Encoding (`Fuel_Type`, `Selling_type`, `Transmission`)
    - **Evaluation Metrics:** Coefficient of Determination ($R^2$ Score) and Mean Absolute Error (MAE)
    """)
