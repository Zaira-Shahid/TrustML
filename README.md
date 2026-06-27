

## 📈 Trust Score Formula

| Grade | Score | Meaning |
|-------|-------|---------|
| A | 90-100 | Highly Trustworthy |
| B | 75-89  | Trustworthy |
| C | 60-74  | Moderate Risk |
| D | 45-59  | High Risk |
| F | 0-44   | Critical Risk |

---

## 🔬 Research

This toolkit is part of a Final Year Project in BS Software Engineering
with domain focus in Machine Learning.

**Paper:** Coming Soon

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 👩‍💻 Author

Built with ❤️ for safer, fairer, and more trustworthy AI.
'''

with open("README.md", "w") as f:
    f.write(readme)

# requirements.txt
req = """numpy>=1.21.0
scikit-learn>=1.0.0
pandas>=1.3.0
matplotlib>=3.4.0
"""
with open("requirements.txt", "w") as f:
    f.write(req)

# example.py
example = """
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import sys
sys.path.insert(0, '.')

from trustml.privacy.auditor    import PrivacyAuditor
from trustml.fairness.auditor   import FairnessAuditor
from trustml.robustness.auditor import RobustnessAuditor

# Dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
sensitive = np.random.randint(0, 2, size=len(y_test))

# Model
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

print("\\n" + "="*48)
print("  TrustML — Unified ML Trust Audit Toolkit")
print("="*48 + "\\n")

# Privacy
print("[1/3] Privacy Audit")
pa = PrivacyAuditor(model, X_train, X_test, y_train, y_test)
pa.membership_inference_attack()
privacy_score = pa.get_privacy_score()

# Fairness
print("\\n[2/3] Fairness Audit")
fa = FairnessAuditor(model, X_test, y_test, sensitive)
fa.run_all()
fairness_score = fa.get_fairness_score()

# Robustness
print("\\n[3/3] Robustness Audit")
ra = RobustnessAuditor(model, X_test, y_test)
ra.run_all()
robustness_score = ra.get_robustness_score()

# Trust Score
trust = round(privacy_score*0.35 + fairness_score*0.35 + robustness_score*0.30, 1)
print(f"\\n{'='*48}")
print(f"  TRUST SCORE : {trust}/100")
print(f"{'='*48}")
"""
with open("example.py", "w") as f:
    f.write(example)

# .gitignore
with open(".gitignore", "w") as f:
    f.write("__pycache__/\n*.pyc\n*.ipynb\n.ipynb_checkpoints/\n*.json\n")

print("✅ README.md created!")
print("✅ requirements.txt created!")
print("✅ example.py created!")
print("✅ .gitignore created!")
print("\n📁 Files ready for GitHub upload!")
