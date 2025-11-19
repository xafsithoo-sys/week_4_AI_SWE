# dataset_preprocessing.py
# Lightweight script showing preprocessing steps for the Breast Cancer dataset.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

def load_and_prepare(path):
    df = pd.read_csv(path)
    # Example cleaning (adjust to actual CSV columns)
    df = df.dropna()
    X = df.drop("target", axis=1)  # replace 'target' with actual label column name
    y = df["target"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_and_eval(X_train, X_test, y_train, y_test):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print("F1 Score (weighted):", f1_score(y_test, preds, average="weighted"))
    return model

if __name__ == "__main__":
    # Replace with the path to your downloaded CSV
    X_train, X_test, y_train, y_test = load_and_prepare("breast_cancer.csv")
    train_and_eval(X_train, X_test, y_train, y_test)
