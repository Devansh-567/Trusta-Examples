# 🛡️ Trustra — Trust-First AutoML Framework

> **"One `fit()`. Full trust."**

Trustra is a **next-generation, open-source AutoML framework** that doesn't just maximize accuracy — it **ensures model integrity** by automatically detecting **data leakage, bias, drift, and instability** — and generating **auditable trust reports**.

Unlike traditional AutoML tools, **Trustra enforces responsibility by design**.

## 🚀 Why Trustra?

Most AutoML tools focus on *"How accurate is the model?"*  
Trustra asks:  
> ❓ **"Can we trust this model?"**  
> ❓ **"Is it fair?"**  
> ❓ **"Is it safe for production?"**

We built Trustra because:
- Real-world models fail due to **hidden data issues**, not poor algorithms
- Bias goes undetected until it harms users
- Drift creeps in silently
- Teams waste weeks on manual validation

👉 **Trustra automates trust.**

## ✨ Key Features

| Feature | Description |
|-------|-------------|
| 🔍 **Data Quality Checks** | Detects missing values, duplicates, class imbalance, and **data leakage** |
| ⚖️ **Fairness Audit** | Automatically audits bias across sensitive features using **Demographic Parity & Equalized Odds** |
| 📉 **Drift Detection** | Flags feature drift between train/validation using KS test |
| 🧠 **Auto Model Selection** | Uses **Optuna** to find the best model and hyperparameters |
| 📊 **Trust Report** | Generates a **self-contained HTML report** with model performance and detected issues |
| 🚀 **Simple API** | Just `model.fit(X_train, y_train)` — no complex pipelines |

## 🏆 Results on Benchmark Data

| Metric | Result |
|-------|--------|
| **CV AUC** | 0.995 |
| **Bias (DPD)** | 0.051 (Low) |
| **Data Issues Found** | 0 |
| **Training Time** | < 10 seconds |

## 🚀 Quick Start

```bash
# Install from PyPI
pip install trustra

# Use in your Python script
from trustra import TrustRA

model = TrustRA(target="target_column", sensitive_features=["gender"])
model.fit(X_train, y_train, X_val, y_val)
```
- Generates: trustra_report.html — fully interactive, offline-ready.
---

## 📚 Motivation
AI is powerful — but untrusted AI is dangerous.
From biased hiring models to faulty credit scoring, bad models cause real harm.

Trustra was built to:
- Democratize responsible AI
- Automate model validation
- Empower data scientists, auditors, and compliance teams
- Make trust the default, not an afterthought
---

## 🛠 Tech Stack
- Python 3.9+
- Optuna – Hyperparameter tuning
- Scikit-learn – Model training
- Plotly – Interactive visualizations
- Fairlearn – Fairness metrics
- Jinja2 – HTML report templating
---

## 📄 License
MIT License
Copyright © 2025 Devansh Singh
---

## 👤 Author
> Devansh Singh
> devansh.jay.singh@gmail.com
> "Built Trustra to make AI trustworthy, one model at a time. "
