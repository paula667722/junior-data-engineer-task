# Junior Data Engineer – Recruitment Task

Solution for the recruitment task: implementing `add_virtual_column` for a pandas DataFrame.

## What it does
- Creates a new column based on a simple expression: `col_a + col_b`, `col_a - col_b`, `col_a * col_b`
- Validates column names (letters and underscores only)
- Returns an empty DataFrame when the input or expression is invalid

## Files
- `solution.py` – implementation
- `test_virtual_column 1.py` – unit tests used to verify the solution

## How to run tests
```bash
python -m pytest -q "test_virtual_column 1.py"
