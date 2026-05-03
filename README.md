# 🌫️ Air Quality Index (AQI) Prediction

> Predict air pollution levels accurately using Machine Learning — powered by **XGBoost**, Linear Regression, and Random Forest.

---

## 📌 Overview

Air pollution is one of the most critical environmental challenges of our time. This project builds a **Machine Learning pipeline** to predict the **Air Quality Index (AQI)** based on pollutant concentration data. By leveraging multiple regression models and rigorous evaluation, the system helps identify pollution trends and provide actionable insights for air quality monitoring.

---

## 🚀 Key Features

- 📊 **Exploratory Data Analysis (EDA)** — Visualize pollutant distributions, correlations, and seasonal trends
- 🧹 **Data Preprocessing** — Handles missing values, outliers, feature scaling, and encoding
- 🤖 **Multiple ML Models** — Trains and evaluates Linear Regression, Random Forest, and XGBoost
- 🏆 **XGBoost as Best Model** — Achieves highest accuracy through gradient boosting
- 🔧 **Hyperparameter Tuning** — Optimized model performance via GridSearchCV / RandomizedSearchCV
- 📈 **Model Evaluation** — Comprehensive metrics: MAE, RMSE, R² Score
- 🔍 **Feature Importance Analysis** — Identify key pollutants driving AQI levels

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.x |
| **ML Libraries** | Scikit-learn, XGBoost |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Notebook** | Jupyter Notebook |

---

## 📂 Project Structure

```
Air_quality_prediction/
│
├── Air-Quality-Index-AQI-Prediction/   # Core project directory
│   ├── data/                           # Raw and processed datasets
│   ├── notebooks/                      # Jupyter notebooks for EDA & modeling
│   ├── models/                         # Saved trained models
│   ├── src/                            # Source scripts
│   │   ├── preprocessing.py            # Data cleaning & feature engineering
│   │   ├── train.py                    # Model training pipeline
│   │   ├── evaluate.py                 # Evaluation metrics & reporting
│   │   └── predict.py                  # Inference / prediction script
│   └── requirements.txt                # Python dependencies
│
├── .gitignore
└── README.md
```

---

## 📊 Models & Performance

| Model | MAE | RMSE | R² Score |
|---|---|---|---|
| Linear Regression | — | — | — |
| Random Forest | — | — | — |
| **XGBoost** ✅ | **Best** | **Best** | **Best** |

> ✅ **XGBoost** outperformed other models and was selected as the final model for AQI prediction.

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/chandankumarcp/Air_quality_prediction.git
cd Air_quality_prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Notebook

```bash
jupyter notebook
```

Open the relevant notebook inside the `notebooks/` directory to explore EDA, model training, and evaluation.

### 4. Train the Model

```bash
python src/train.py
```

### 5. Make Predictions

```bash
python src/predict.py --input <your_data.csv>
```

---

## 🌡️ AQI Categories

| AQI Range | Category | Health Impact |
|---|---|---|
| 0 – 50 | 🟢 Good | Minimal impact |
| 51 – 100 | 🟡 Satisfactory | Minor breathing discomfort for sensitive people |
| 101 – 200 | 🟠 Moderate | Discomfort on prolonged exposure |
| 201 – 300 | 🔴 Poor | Breathing discomfort on exertion |
| 301 – 400 | 🟣 Very Poor | Respiratory illness on prolonged exposure |
| 401 – 500 | ⚫ Severe | Severe health effects |

---

## 🔬 ML Pipeline

```
Raw Data
   │
   ▼
Data Preprocessing
(Missing values, Outliers, Scaling)
   │
   ▼
Feature Engineering
(Pollutant ratios, Lag features)
   │
   ▼
Model Training
(Linear Regression → Random Forest → XGBoost)
   │
   ▼
Hyperparameter Tuning
(GridSearchCV / RandomizedSearchCV)
   │
   ▼
Evaluation & Selection
(MAE, RMSE, R² Score)
   │
   ▼
Best Model: XGBoost ✅
```

---

## 📈 Key Pollutants Used

- **PM2.5** — Fine particulate matter
- **PM10** — Coarse particulate matter
- **NO₂** — Nitrogen Dioxide
- **SO₂** — Sulfur Dioxide
- **CO** — Carbon Monoxide
- **O₃** — Ozone

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 👤 Author

**Chandan Kumar**

- GitHub: [@chandankumarcp](https://github.com/chandankumarcp)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## ⭐ Show Your Support

If you found this project helpful, please consider giving it a **⭐ star** on GitHub — it means a lot!

---

*Built with ❤️ for cleaner air and better insights.*
