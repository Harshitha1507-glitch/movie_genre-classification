# Dataset Instructions

Place your dataset CSV file in this folder.

Expected structure:
- `plot`: plot summary or movie description text
- `genre`: movie genre label

Example rows:

plot,genre
"A space crew travels to rescue a stranded astronaut.","Sci-Fi"
"A young detective solves a murder mystery.","Mystery"

If your dataset uses different column names, rename them to `plot` and `genre` or update `src/train.py`.
