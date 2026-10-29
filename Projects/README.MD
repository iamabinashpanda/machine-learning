# ⚡ ML Suite - Enterprise Machine Learning Dashboard

Welcome to **ML Suite**, a comprehensive, interactive Machine Learning hub designed to streamline predictive modeling, time-series forecasting, and classification across real-world domain datasets. 

This repository showcases an end-to-end Machine Learning pipeline—from raw data preprocessing and model serialization to high-performance, polished Streamlit interactive web interfaces.

---

## 🌟 Executive Summary

**ML Suite** brings together multiple custom-trained ML models into a unified web application. The platform serves as a multi-tool dashboard for business intelligence, valuation estimation, sales optimization, and demographic propensity modeling.

### Core Objectives & Goals
* **Unified Interface:** Consolidate multiple distinct Machine Learning models into a single, cohesive user experience.
* **Production-Ready Inference:** Demonstrate low-latency inference pipelines using saved model artifacts (`.joblib`, `.pkl`).
* **Dynamic Visualization:** Interactive parameter selection with real-time UI updates, metrics, and data visualizations.
* **Modern UX Design:** Custom CSS, glassmorphism layouts, light/dark themes, responsive components, and user session simulation.

---

## 🛠️ Stack & Technologies Used

| Category | Technology / Library | Purpose & Implementation Details |
| :--- | :--- | :--- |
| **Core Stack** | `Python 3.11+` | Primary programming language for modeling and backend execution |
| | `Streamlit (v1.30+)` | Full-stack UI/UX framework for rapid web app generation |
| **Machine Learning & Analytics** | `scikit-learn` | Machine learning pipeline engineering, Random Forest, Decision Trees, Logistic Regression |
| | `statsmodels` | SARIMAX time-series modeling, parameter estimation, and forecasting |
| | `joblib` | Model bundle serialization, compression, and deserialization |
| | `pandas` & `numpy` | Feature vector generation, dynamic inputs, data cleaning, and array transformations |
| **Data Visualization & Styling** | `plotly` | High-performance interactive time-series plots with confidence bands |
| | `matplotlib` | Custom static budget allocation charts |
| | `HTML5 / CSS3` | Custom glassmorphism UI components, gradient banners, and responsive layouts |

---

## 📸 Applications & Project Modules

Each module within the suite targets a specific real-world data challenge and predictive domain.

---

### 🔑 Auth & Suite Landing Page
* **Screenshot:** `screenshots/Landing Page.PNG`
* **File:** `login_page.py`, `home.py`

#### Overview & Goal
Provides a modern login interface with session management and a central hub introducing available applications and system metrics.

#### Key Functionality
* Simulated authentication state with customizable user session routing.
* Hero dashboard highlighting active model count, system status, and framework metrics.
* Responsive card layout for quick application navigation.

![Landing Page](screenshots/Landing%20Page.PNG)

---

### 1. 🚘 ValuatAuto — Used Car Price Estimator
* **Screenshot:** `screenshots/Project 1.PNG`
* **File:** `car_price_page.py`

#### Overview & Goal
Evaluates market valuations for pre-owned vehicles based on brand heritage, mileage, manufacturing year, and regional trends in Indian metro cities.

#### Key Functionality
* Dynamic dropdown filtering based on brand-to-model mapping.
* Automatic vehicle age calculation based on current calendar year.
* Real-time price inference using a **Random Forest Regressor** pipeline.
* High-visibility metric cards highlighting output valuation.

![Car Price Predictor](screenshots/Project%201.PNG)

---

### 2. 📈 Advertising Sales Forecasting Dashboard
* **Screenshot:** `screenshots/Project 2.PNG`
* **File:** `sales_predictor_page.py`

#### Overview & Goal
Simulates marketing return-on-investment (ROI) by predicting sales volume based on multi-channel advertising budget spend across TV, Radio, and Newspaper channels.

#### Key Functionality
* Dynamic slider controls for granular channel budget allocation.
* Real-time sales unit prediction compared against baseline performance.
* Matplotlib spend distribution chart comparing advertising allocations across channels.

![Sales Predictor](screenshots/Project%202.PNG)

---

### 3. 🎯 Client Purchase Propensity Classifier
* **Screenshot:** `screenshots/Project 3.PNG`
* **File:** `client_purchase_page.py`

#### Overview & Goal
Classifies whether a prospective target user is likely to purchase a product or service based on demographic indicators (Age, Gender, Salary).

#### Key Functionality
* Soft transparent light-mode styling with interactive input forms.
* **Logistic Regression** binary classification pipeline.
* Model confidence gauge display showing exact purchase probability percentage.

![Client Purchase Predictor](screenshots/Project%203.PNG)

---

### 4. 🏎️ Vehicle Origin Regional Predictor
* **Screenshot:** `screenshots/Project 4.PNG`
* **File:** `vehicle_origin_prediction_page.py`

#### Overview & Goal
Predicts the geographic region of manufacture (US, Europe, Japan) based on engine performance parameters and historical vehicle specifications (1970–1982 data).

#### Key Functionality
* Multi-column form layout capturing engine metrics (Cylinders, Displacement, HP, MPG, Weight, Acceleration).
* Multi-class classification using LabelEncoders and Decision Tree/Ensemble models.
* Class confidence probability breakdown rendered via native chart widgets.
* Inspectable input feature vector formatted as JSON payload.

![Vehicle Origin Predictor](screenshots/Project%204.PNG)

---

### 5. ✈️ SeaPlane Passenger Traffic Forecaster
* **Screenshot:** `screenshots/Project 5.PNG`
* **File:** `seaplane_traffic_forecaster_page.py`

#### Overview & Goal
Generates long-term time-series projections for airline passenger traffic using multiplicative seasonal parameters.

#### Key Functionality
* **SARIMAX (1,1,1) x (0,1,0,12)** time-series predictive modeling with log-transformed history.
* Adjustable forecast horizons ranging from 1 to 48 months.
* Interactive **Plotly** visualization featuring toggleable 95% confidence intervals.
* Export functionality allowing users to download generated forecast data as a CSV.

![SeaPlane Traffic Forecaster](screenshots/Project%205.PNG)

---

## 📦 Requirements & Dependencies

Create a file named `requirements.txt` in the root folder with the following content:

```text
streamlit>=1.30.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.2.0
statsmodels>=0.14.0
joblib>=1.3.0
matplotlib>=3.7.0
plotly>=5.15.0
```

---

## ⚙️ Code Setup & Local Execution

Follow these steps to run the application locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ml-suite.git
cd ml-suite
```

### 2. Create and Activate Virtual Environment
* **Linux/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

### 3. Install Requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch Application
Ensure all model artifacts are placed under `./models/` and screenshots inside `./screenshots/`, then execute:
```bash
streamlit run main.py
```

---

## 📌 Note: Future Engineering Roadmap

> **Note:** The features below outline the architectural vision for transforming this monolithic dashboard into an enterprise-grade production product. These goals are actively in development.

* **Microservices Migration:**
  * Decouple ML inference into high-throughput asynchronous REST endpoints using **FastAPI**.
  * Modernize the front-end interface using **React.js** for custom client control, or retain lightweight **Streamlit** micro-apps per service.
* **Database & Authentication:**
  * Implement **SQL Server** integration for persistent user account storage and role-based feature permissions (Hide/Show specific application features based on user tier).
* **Enterprise Logging & Monitoring:**
  * Build an audit logging system to record input payloads, prediction results, latency metrics, and error rates to SQL Server tables for model monitoring and compliance.