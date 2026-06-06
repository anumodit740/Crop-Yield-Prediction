# 🌾 Crop Yield Prediction

A machine learning project that predicts agricultural crop yields in India using historical data and weather patterns.

## 📋 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Data Sources](#data-sources)
- [Dataset Details](#dataset-details)
- [APIs Used](#apis-used)
- [Key Features](#key-features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Results & Visualizations](#results--visualizations)

## 🎯 Overview

This project aims to predict crop yields across Indian districts using:
- **Historical agricultural data** (2001-2020)
- **Weather patterns** from Open-Meteo API
- **Machine learning models** for accurate yield forecasting

The project is divided into two distinct periods due to changes in India's administrative districts:
- **Period 1**: 2001-2010 (Original districts)
- **Period 2**: 2011-2020 (Reorganized districts)

## 📁 Project Structure

```
Crop-Yield-Prediction/
├── README.md                           # Project documentation
├── Crop Yield Prediction/              # Main project directory
│   ├── data/                          # Data files
│   │   ├── agriculture_2001-2010.csv # Historical yields (2001-2010)
│   │   └── agriculture_2010-2020.csv # Historical yields 2011-2020)
│   ├── notebooks/                     # Jupyter notebooks
│   ├── models/                        # Trained models
│   └── visualizations/                # Charts and graphs
```

## 📊 Data Sources

### 1. **Open-Meteo API** 🌤️
- **Purpose**: Fetch real-time and historical weather data
- **Data Includes**: Temperature, precipitation, humidity, wind speed
- **URL**: https://open-meteo.com/
- **Usage**: Provides weather features for yield prediction

### 2. **India Data Portal** 🇮🇳
- **Purpose**: Crop yields dataset
- **Dataset**: Area, Production, Yield (APY)
- **URL**: https://ckandev.indiadataportal.com/dataset/area-production-yield-apy/resource
- **Coverage**: Multiple Indian districts and crops (2001-2020)

## 📈 Dataset Details

### Why Two Separate Datasets?

India reorganized its administrative districts in 2011, resulting in different district structures:

| Aspect | 2001-2010 | 2011-2020 |
|--------|-----------|-----------|
| **Period** | 2001-2010 | 2011-2020 |
| **Number of Districts** | Original configuration | Reorganized configuration |
| **Data Points** | Mapped to old districts | Mapped to new districts |
| **Usage** | Historical baseline | Current predictions |

### Dataset Features

- **Temporal Range**: 20 years of data (2001-2020)
- **Geographic Coverage**: All major agricultural districts in India
- **Crop Types**: Multiple crops (Rice, Wheat, Cotton, Sugarcane, etc.)
- **Variables**:
  - Area under cultivation (hectares)
  - Production (tonnes)
  - Yield (tonnes/hectare)
  - Weather parameters
  - Seasonal data

## 🔌 APIs Used

### Open-Meteo
```
Endpoint: https://api.open-meteo.com/v1/forecast
Parameters:
  - latitude, longitude
  - hourly/daily data
  - temperature, precipitation
  - relative_humidity, wind_speed
```

### India Data Portal
```
Dataset: Area, Production, Yield (APY)
Resource: https://ckandev.indiadataportal.com/dataset/area-production-yield-apy/resource
Format: CSV
```

## ⚙️ Key Features

- ✅ Historical yield data analysis
- ✅ Weather data integration
- ✅ District-level predictions
- ✅ Multi-crop support
- ✅ Time-series analysis
- ✅ Data visualization dashboards
- ✅ Machine learning model deployment

## 🛠️ Technologies

- **Languages**: Python 3.8+
- **Libraries**:
  - `pandas` - Data manipulation
  - `numpy` - Numerical computations
  - `scikit-learn` - Machine learning
  - `matplotlib`, `seaborn` - Visualization
  - `jupyter` - Interactive notebooks
  - `requests` - API calls
- **Tools**: Jupyter Notebook, Git

## 🚀 Getting Started

### Prerequisites
```bash
python >= 3.8
pip
git
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Utkarsh5100/Crop-Yield-Prediction.git
cd Crop-Yield-Prediction
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Jupyter Notebooks**
```bash
jupyter notebook
```

## 📊 Results & Visualizations

### Expected Outputs

- 📈 **Yield Trends**: Temporal analysis of crop yields
- 🌡️ **Weather Impact**: Correlation between weather and yields
- 📍 **District Analysis**: Regional yield variations
- 🎯 **Predictions**: ML model forecasts

## 📝 Data Pipeline

```
Raw Data (CSV)
    ↓
Data Cleaning & Preprocessing
    ↓
Feature Engineering (Weather API integration)
    ↓
Exploratory Data Analysis (EDA)
    ↓
Model Training
    ↓
Evaluation & Validation
    ↓
Predictions & Visualizations
```

## 📌 Important Notes

### District Classification
- **agriculture_2001-2010**: Contains data mapped to districts as per 2001 census
- **agriculture_2011-2020**: Contains data mapped to districts as per 2011 reorganization
- These datasets cannot be directly merged without proper district mapping


