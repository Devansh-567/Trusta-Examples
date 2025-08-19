# 🛰️ NASA Mars Rover Anomaly Detection with `trustra`

> **"Can we trust the AI that decides if the Mars Rover should drill?"**

This project simulates a **mission-critical AI system** for NASA’s Mars Rover, using [`trustra`](https://pypi.org/project/trustra/) to ensure **trust, fairness, and reliability** in autonomous decisions.

It demonstrates how `trustra` automatically:
- 🔍 Detects data leakage
- ⚖️ Audits fairness (e.g., sensor bias)
- 📉 Flags data drift
- 📊 Generates a full **auditable HTML trust report**
- 🚀 Delivers high performance with one `fit()` call

## 🚀 Quick Start

Run this to launch the Mars mission simulation:

```bash
# Clone the project
git clone https://github.com/Devansh-567/Trusta-Examples.git
cd Trusta-Examples/1_nasa_mars_rover

# Install trustra (published on PyPI)
pip install trustra

# Run the Mars Rover AI
python nasa_mars_rover_analysis.py
```
---
## 📊 Sample Output
```python
============================================================
✅ TRUSTRA MISSION REPORT COMPLETE
📈 CV AUC: 0.995
⚖️  Fairness Issues: 0
🔍 Total Issues Found: 0
🔧 Best Model: LR
📄 Full Report: trustra_report.html
============================================================
```
## 🧪 Simulated Risks (Automatically Detected)
> ⚖️ Sensor ID bias (rover_sensor_id)
> 🔥 Data leakage in spectral_450nm
> 📉 Drift between training and validation
---

## 🌍 Why This Matters
This isn't just a demo — it's a blueprint for trustworthy AI in space, healthcare, finance, and beyond.
> trustra ensures that when the AI says "drill here", scientists can trust the decision — no black boxes, no surprises.
