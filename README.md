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
