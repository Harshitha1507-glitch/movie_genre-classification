import argparse
from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
import joblib


def find_dataset_file(dataset_path: Path) -> Path:
    csv_files = list(dataset_path.glob("*.csv"))
    if len(csv_files) == 1:
        return csv_files[0]
    if len(csv_files) > 1:
        raise FileNotFoundError(
            "More than one CSV found in dataset/. Please keep only one dataset CSV or pass --dataset-file."
        )
    raise FileNotFoundError("No CSV dataset found in dataset/. Place your dataset file there.")


def load_dataset(dataset_file: Path) -> pd.DataFrame:
    data = pd.read_csv(dataset_file)
    if "plot" not in data.columns and "summary" not in data.columns:
        raise ValueError("Dataset must contain a 'plot' or 'summary' column.")
    if "genre" not in data.columns:
        raise ValueError("Dataset must contain a 'genre' column.")
    text_col = "plot" if "plot" in data.columns else "summary"
    data = data[[text_col, "genre"]].rename(columns={text_col: "plot"})
    data = data.dropna(subset=["plot", "genre"])
    data["plot"] = data["plot"].astype(str)
    data["genre"] = data["genre"].astype(str)
    return data


def build_pipeline() -> Pipeline:
    return Pipeline(
        [
            ("tfidf", TfidfVectorizer(stop_words="english", max_df=0.8)),
            ("clf", LogisticRegression(max_iter=1000, solver="liblinear")),
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Train movie genre classification model")
    parser.add_argument(
        "--dataset-file",
        type=str,
        default=None,
        help="Path to the dataset CSV file. If not set, the script searches dataset/*.csv.",
    )
    parser.add_argument(
        "--model-output",
        type=str,
        default="models/genre_classifier.joblib",
        help="Output path for the saved model.",
    )
    args = parser.parse_args()

    dataset_path = Path("dataset")
    dataset_path.mkdir(exist_ok=True)

    dataset_file = Path(args.dataset_file) if args.dataset_file else find_dataset_file(dataset_path)
    print(f"Loading dataset from: {dataset_file}")

    data = load_dataset(dataset_file)
    print(f"Loaded {len(data)} rows.")

    encoder = LabelEncoder()
    data["genre_label"] = encoder.fit_transform(data["genre"])

    X_train, X_test, y_train, y_test = train_test_split(
        data["plot"], data["genre_label"], test_size=0.2, random_state=42, stratify=data["genre_label"]
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    print("\nEvaluation")
    print("----------")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\nClassification report:")
    print(classification_report(y_test, y_pred, target_names=encoder.classes_))

    output_path = Path(args.model_output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"pipeline": pipeline, "encoder": encoder}, output_path)
    print(f"Saved model to {output_path}")


if __name__ == "__main__":
    main()
