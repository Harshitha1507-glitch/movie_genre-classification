"""
Prepare dataset CSVs from extracted text files in the `dataset/` folder.
Parses files with lines like:
- train_data.txt: id ::: title ::: genre ::: plot
- test_data.txt: id ::: title ::: plot
- test_data_solution.txt: id ::: title ::: genre ::: plot

Generates:
- dataset/train.csv (id,title,genre,plot)
- dataset/test.csv (id,title,plot)
- dataset/test_solution.csv (id,title,genre,plot) if solution present
"""
from pathlib import Path
import csv

DATA_DIR = Path(__file__).resolve().parents[1] / "dataset"


def find_nested_file(name: str) -> Path | None:
    for p in DATA_DIR.rglob(name):
        if p.is_file():
            return p
    return None


def parse_lines(path: Path, expect_genre: bool):
    rows = []
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(" ::: ")
            if expect_genre:
                if len(parts) < 4:
                    # try to be lenient
                    continue
                idx, title, genre, plot = parts[0], parts[1], parts[2], " ::: ".join(parts[3:])
                rows.append({"id": idx.strip(), "title": title.strip(), "genre": genre.strip(), "plot": plot.strip()})
            else:
                # expect id, title, plot
                if len(parts) < 3:
                    continue
                idx, title, plot = parts[0], parts[1], " ::: ".join(parts[2:])
                rows.append({"id": idx.strip(), "title": title.strip(), "plot": plot.strip()})
    return rows


def write_csv(path: Path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print(f"Wrote {len(rows)} rows to {path}")


def main():
    # train
    train_src = find_nested_file("train_data.txt")
    if train_src:
        print("Found train source:", train_src)
        train_rows = parse_lines(train_src, expect_genre=True)
        write_csv(DATA_DIR / "train.csv", train_rows, ["id", "title", "genre", "plot"])
    else:
        print("No train_data.txt found")

    # test
    test_src = find_nested_file("test_data.txt")
    if test_src:
        print("Found test source:", test_src)
        test_rows = parse_lines(test_src, expect_genre=False)
        write_csv(DATA_DIR / "test.csv", test_rows, ["id", "title", "plot"])
    else:
        print("No test_data.txt found")

    # test solution
    sol_src = find_nested_file("test_data_solution.txt")
    if sol_src:
        print("Found test solution source:", sol_src)
        sol_rows = parse_lines(sol_src, expect_genre=True)
        write_csv(DATA_DIR / "test_solution.csv", sol_rows, ["id", "title", "genre", "plot"])
    else:
        print("No test_data_solution.txt found")


if __name__ == "__main__":
    main()
