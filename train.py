import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
import joblib

data = []
with open('dataset.jsonl', 'r') as file:
    for line in file:
        sample = json.loads(line)
        for key in ['S', 'H', 'V', 'HR', 'SH', 'S3', 'H2', 'V2']:
            if key not in sample:
                sample[key] = 0
        data.append(sample)

df = pd.DataFrame(data)
X_text = df['prompt']
y = df[['S', 'H', 'V', 'HR', 'SH', 'S3', 'H2', 'V2']]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_text)

joblib.dump(vectorizer, 'model_vectorizer.pkl')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(model, 'model.pkl')