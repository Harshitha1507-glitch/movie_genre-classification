import argparse
from pathlib import Path
import joblib


def load_model(model_path: Path):
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    data = joblib.load(model_path)
    return data["pipeline"], data["encoder"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Predict movie genre from plot text")
    parser.add_argument(
        "--text",
        type=str,
        help="Plot text to classify.",
    )
    parser.add_argument(
        "--model-file",
        type=str,
        default="models/genre_classifier.joblib",
        help="Path to the saved model file.",
    )
    args = parser.parse_args()

    pipeline, encoder = load_model(Path(args.model_file))

    if not args.text:
        print("Please provide text with --text. Example:")
        print("python src\\predict.py --text \"A detective uncovers a conspiracy in a futuristic city.\"")
        return

    text = [args.text]
    prediction = pipeline.predict(text)
    genre = encoder.inverse_transform(prediction)[0]
    print(f"Predicted genre: {genre}")


if __name__ == "__main__":
    main()
