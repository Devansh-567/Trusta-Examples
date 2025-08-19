"""
🚀 NASA Mars Rover - Trust-First AI Decision System
Using trustra for mission-critical anomaly detection
"""

# 🔥 Import trustra — the trust-first AutoML framework
from trustra import TrustRA

import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

print("📡 Loading simulated Mars Rover dataset...")

# Simulated Mars Rover Spectral Data
# Features: 8 spectral bands, density, thermal response
# Target: 1 = organic anomaly (possible life), 0 = normal mineral

X, y = make_classification(
    n_samples=5000,
    n_features=10,
    n_classes=2,
    n_redundant=2,
    n_informative=8,
    n_clusters_per_class=2,
    class_sep=0.8,
    random_state=42
)

# Create realistic feature names
feature_names = [
    "spectral_450nm", "spectral_530nm", "spectral_600nm", "spectral_700nm",
    "spectral_850nm", "spectral_1000nm", "spectral_1200nm", "spectral_1500nm",
    "soil_density", "thermal_emissivity"
]
X = pd.DataFrame(X, columns=feature_names)
y = pd.Series(y, name="is_anomalous")

# Simulate rover sensor ID (sensitive feature — could introduce bias)
X["rover_sensor_id"] = np.random.choice([1, 2, 3], size=len(X))  # Sensors A/B/C

# Split data
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

# 🔥 Simulate data leakage (dangerous but realistic)
X_train["spectral_450nm"] += 0.3 * y_train
X_val["spectral_450nm"] += 0.3 * y_val

print(f"✅ Dataset ready: {X_train.shape[0]} training samples")
print(f"⚠️  Simulated data leakage in 'spectral_450nm'")

# 🛡️ TRUSTRA — Trust-First AI for Space Missions
print("\n🚀 Deploying TrustRA for Mars Rover AI Validation...\n")

model = TrustRA(
    target="is_anomalous",
    sensitive_features=["rover_sensor_id"],  # Audit sensor fairness
    timeout=120  # Allow longer tuning for mission-critical use
)

# Run full trust-first pipeline
model.fit(X_train, y_train, X_val, y_val)

# 📡 Predict on new samples
print("\n📡 Predicting on new Martian samples...")
sample = X_val.iloc[:5]
preds = model.predict(sample)
probs = model.predict_proba(sample)[:, 1]

for i, (p, prob) in enumerate(zip(preds, probs)):
    print(f"Sample {i+1}: {'🔴 ANOMALY' if p else '🟢 Normal'} "
          f"(Confidence: {prob:.2f})")

# 📊 Final Mission Report
print("\n" + "="*60)
print("✅ TRUSTRA MISSION REPORT COMPLETE")
print(f"📈 CV AUC: {model.trainer_.best_score_:.3f}")
print(f"⚖️  Fairness Issues: {len([i for i in model.issues if 'bias' in i.lower()])}")
print(f"🔍 Total Issues Found: {len(model.issues)}")
print(f"🔧 Best Model: {model.trainer_.best_model_name_.upper()}")
print(f"📄 Full Report: trustra_report.html")
print("="*60)

print("\n🛰️  Decision approved for rover action. Proceed with drilling.")
