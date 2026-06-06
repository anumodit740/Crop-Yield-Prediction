import streamlit as st
import pandas as pd
import numpy as np
from Helper import helper as hp

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="wide"
)

# =====================================
# SESSION STATE
# =====================================
st.session_state.setdefault("submit", False)

# =====================================
# INPUT FORM
# =====================================
def show_input_form():
    st.title("🌾 Crop Yield Prediction System")

    col1, col2 = st.columns(2)
    with col1:
        st.selectbox(
            "Select State",
            hp.options()["state_list"],
            key="state",
            index=None
        )

    selected_state = st.session_state.get("state")
    with col2:
        st.selectbox(
            "Select District",
            hp.options()["district_dict"].get(selected_state, []),
            key="district",
            index=None
        )

    col3, col4 = st.columns(2)
    with col3:
        st.selectbox(
            "Select Year",
            list(range(2020, 2035)),   # till 2035
            key="year",
            index=None
        )
    with col4:
        st.selectbox(
            "Select Season",
            hp.options()["season_list"],
            key="season",
            index=None
        )

    st.multiselect(
        "Select Crop(s)",
        hp.options()["crop_list"],
        key="crop"
    )

    col5, col6 = st.columns(2)
    with col5:
        st.selectbox(
            "Unit of Area",
            [
                'ha', 'sq_m', 'sq_km', 'acre', 'sq_ft', 'sq_yd', 'gaj', 'kanal',
                'bigha', 'biswa', 'killa', 'lessa', 'dhur', 'pura', 'chatak',
                'marla', 'katha', 'ground', 'cent', 'murabba', 'guntha', 'karam'
            ],
            key="UnitOfArea",
            index=None
        )
    with col6:
        st.number_input(
            "Area",
            key="area",
            disabled=not bool(st.session_state.get("UnitOfArea"))
        )

    required = ["state", "district", "year", "season", "crop", "UnitOfArea", "area"]
    ready = all(st.session_state.get(k) not in [None, "", []] for k in required)

    if st.button("🚀 Predict", disabled=not ready):
        st.session_state.submit = True
        st.rerun()

# =====================================
# RESULT VIEW
# =====================================
def show_result():

    # -------- RESET / NEW PREDICTION --------
    st.sidebar.title("Navigation")
    if st.sidebar.button("🔄 New Prediction"):
        st.session_state.submit = False
        st.rerun()

    st.title("🌾 Crop Yield Prediction Dashboard")

    # -------- LOCATION --------
    lat, lon = hp.extraction_lat_lon_values(
        st.session_state.state,
        st.session_state.district
    )

    # -------- WEATHER DATA --------
    env_data = hp.api_data(
        st.session_state.year,
        st.session_state.season.lower(),
        lat, lon
    )

    # -------- WEATHER SUMMARY --------
    st.subheader("🌦 Weather Summary")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🌡 Avg Temp (°C)", round(env_data["temperature_2m_mean"].mean(), 2))
    c2.metric("💧 Avg Humidity (%)", round(env_data["relative_humidity_2m_mean"].mean(), 2))
    c3.metric("🌬 Avg Wind (m/s)", round(env_data["wind_speed_10m_mean"].mean(), 2))
    c4.metric("🌧 Total Rainfall (mm)", round(env_data["precipitation_sum"].sum(), 2))

    # -------- PREDICTION INPUT --------
    data_for_prediction = {
        "crop_year": st.session_state.year,
        "season": st.session_state.season,
        "crop": st.session_state.crop,
        "area": hp.unit_conversion(
            st.session_state.area,
            st.session_state.UnitOfArea
        ),
        "temperature_2m_mean": env_data["temperature_2m_mean"].mean(),
        "precipitation_sum": env_data["precipitation_sum"].sum(),
        "relative_humidity_2m_mean": env_data["relative_humidity_2m_mean"].mean(),
        "wind_speed_10m_mean": env_data["wind_speed_10m_mean"].mean(),
        "latitude": lat,
        "longitude": lon,
    }

    prediction = hp.predicction(data_for_prediction)

    # -------- PREDICTION RESULT --------
    st.subheader("🌾 Estimated Crop Yield & Production")

    df = pd.DataFrame(prediction)

    df["Yield"] = df["Yield"] / hp.conversion_factor_Ha_to_X(
        st.session_state.UnitOfArea
    )
    df["Production (Ton)"] = df["Yield"] * st.session_state.area

    st.dataframe(df, use_container_width=True)

    best_crop = df.loc[df["Yield"].idxmax(), "Crop"]
    st.success(f"✅ Best Performing Crop: **{best_crop.upper()}**")

    # -------- WEATHER GRAPHS --------
    st.subheader("📈 Weather Trends")

    st.line_chart(
        env_data,
        x="date",
        y=[
            "temperature_2m_mean",
            "precipitation_sum",
            "relative_humidity_2m_mean",
            "wind_speed_10m_mean"
        ]
    )

    # -------- RAW DATA --------
    with st.expander("📄 View Raw Weather Data"):
        st.dataframe(env_data, use_container_width=True)

    # -------- DOWNLOAD --------
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇ Download Prediction CSV",
        csv,
        "crop_yield_prediction.csv",
        "text/csv"
    )

    st.info(
        "ℹ️ Predictions are based on historical weather data "
        "and a CatBoost machine learning model trained on Indian agriculture data (2001–2020)."
    )

# =====================================
# APP FLOW
# =====================================
if not st.session_state.submit:
    show_input_form()
else:
    show_result()
