<<<<<<< HEAD
# Movie Genre Classification

This project predicts a movie's genre from its plot summary or other text using machine learning.

## Project structure

- `dataset/` - place your dataset file here
- `src/` - training and prediction scripts
- `models/` - saved model files after training
- `notebooks/` - project notebook or documentation
- `requirements.txt` - Python dependencies
- `.gitignore` - files and folders to exclude from git

## Step-by-step instructions

1. Place your dataset file in `dataset/`.
   - Recommended filename: `movie_genre_dataset.csv`
   - Required columns: `plot` (or `summary`) and `genre`

2. Create and activate a Python virtual environment.
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies.
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Train the model.
   ```powershell
   python src\train.py
   ```
   - This script loads the dataset, trains a TF-IDF + Logistic Regression model, evaluates it, and saves it to `models/genre_classifier.joblib`.

5. Predict genre for a new plot summary.
   ```powershell
   python src\predict.py --text "A group of friends embark on a space adventure to save their planet."
   ```

6. Add your files to git and push to GitHub.
   ```powershell
   git init
   git add .
   git commit -m "Initial movie genre classification project"
   ```
   Then create a GitHub repository and add it as a remote:
   ```powershell
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```

## Recommended workflow

- Start in `notebooks/` by exploring the data and visualizing genre distributions.
- Use `src/train.py` to train and evaluate models.
- Save the best model in `models/` and document results in the README or a notebook.

## Notes

- If your dataset column names differ, rename them to `plot` and `genre` or adjust `src/train.py` accordingly.
- If the dataset is large, keep it outside git or only include a sample.
=======
# Movie Genre Classification using Machine Learning

## Project Overview

This project predicts the genre of a movie based on its plot summary using Natural Language Processing (NLP) and Machine Learning techniques.

## Objective

To build a machine learning model that can automatically classify movie genres from textual descriptions of movie plots.

## Dataset

The dataset contains movie titles, genres, and plot summaries.

Files used:

* train_data.txt
* test_data.txt
* test_data_solution.txt

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* TF-IDF Vectorization
* VS Code
* Git & GitHub

## Machine Learning Models

The following models were implemented and compared:

1. Naive Bayes
2. Logistic Regression
3. Support Vector Machine (SVM)

## Workflow

1. Data Loading
2. Data Preprocessing
3. Text Cleaning
4. TF-IDF Feature Extraction
5. Model Training
6. Model Evaluation
7. Genre Prediction

## Project Structure

Movie-Genre-Classification/
│
├── dataset/
├── notebooks/
├── models/
├── src/
├── README.md
├── requirements.txt
└── .gitignore

## Results

Model accuracies:

* Naive Bayes: XX%
* Logistic Regression: XX%
* SVM: XX%

Best Model: SVM

## Future Improvements

* Use Word Embeddings (Word2Vec/GloVe)
* Hyperparameter Tuning
* Deploy as a Web Application using Streamlit

## Author

Harshitha Vijay Anand
Machine Learning Internship Project
>>>>>>> 7dcac390b62c81d1077e4b9d095182a8e6e3a437
