import os
import joblib

# Resolve paths relative to this script's directory
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, '../models/movie_genre_model.pkl')
vectorizer_path = os.path.join(base_dir, '../models/tfidf.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

plot = input("Enter movie plot: ")

plot_vector = vectorizer.transform([plot])

prediction = model.predict(plot_vector)

print("Predicted Genre:", prediction[0])
