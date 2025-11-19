# Part 3 — Ethical Reflection

Potential biases:
- Dataset imbalance: some teams or case types may be underrepresented causing biased priority predictions.
- Labeling bias: human-labelled priorities might reflect individual manager preferences.
- Feature bias: features correlated with sensitive groups may lead to unfair outcomes.

Mitigation strategies:
- Use fairness metrics (disparate impact, equalized odds).
- Apply mitigation tools like IBM AI Fairness 360: reweighting, adversarial debiasing, or post-processing adjustments.
- Monitor model predictions in production and gather feedback to improve fairness.
