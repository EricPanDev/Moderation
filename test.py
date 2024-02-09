import joblib

new_data = [input("Input: ")]

loaded_model = joblib.load('model.pkl')
vectorizer = joblib.load('model_vectorizer.pkl')
new_data_vectorized = vectorizer.transform(new_data)
probabilities = loaded_model.predict_proba(new_data_vectorized)

print("Predictions:")
labels = ['sexual', 'hate', 'violence', 'harassment', 'self-harm', 'sexual/minors', 'hate/threatening', 'violence/graphic']
for label, probs in zip(labels, probabilities):
    print(f"{label}: {probs[0][1]:.2f}")