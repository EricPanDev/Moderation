import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
import joblib

# Step 1: Read the JSONL file and extract the data
data = []
with open('dataset.jsonl', 'r') as file:
    for line in file:
        sample = json.loads(line)
        # Set missing keys to 0
        for key in ['S', 'H', 'V', 'HR', 'SH', 'S3', 'H2', 'V2']:
            if key not in sample:
                sample[key] = 0
        data.append(sample)

# Step 2: Preprocess the data
df = pd.DataFrame(data)
X_text = df['prompt']  # Features
y = df[['S', 'H', 'V', 'HR', 'SH', 'S3', 'H2', 'V2']]  # Labels

# Step 3: Vectorize the text features using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_text)

joblib.dump(vectorizer, 'model_vectorizer.pkl')

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Create a RandomForestClassifier model
model = RandomForestClassifier()

# Step 6: Train the model
model.fit(X_train, y_train)

# Step 7: Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Step 8: Save the trained model
joblib.dump(model, 'model.pkl')