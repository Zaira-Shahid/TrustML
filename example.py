import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from trustml.privacy.auditor    import PrivacyAuditor
from trustml.fairness.auditor   import FairnessAuditor
from trustml.robustness.auditor import RobustnessAuditor

X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
sensitive = np.random.randint(0, 2, size=len(y_test))
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

pa = PrivacyAuditor(model, X_train, X_test, y_train, y_test)
pa.membership_inference_attack()
print(f"Privacy Score: {pa.get_privacy_score()}/100")

fa = FairnessAuditor(model, X_test, y_test, sensitive)
fa.run_all()
print(f"Fairness Score: {fa.get_fairness_score()}/100")

ra = RobustnessAuditor(model, X_test, y_test)
ra.run_all()
print(f"Robustness Score: {ra.get_robustness_score()}/100")
