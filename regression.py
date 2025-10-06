"""Simple linear regression analysis for SAT and college GPA data."""

import argparse
import sys
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression


REQUIRED_COLUMNS = {"sat", "colgpa"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fit a simple linear regression model predicting college GPA from SAT scores "
            "using data from a CSV file."
        )
    )
    parser.add_argument(
        "csv_path",
        type=Path,
        help="Path to the CSV file containing 'sat' and 'colgpa' columns.",
    )
    return parser.parse_args()


def load_data(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    data = pd.read_csv(csv_path)
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        missing_cols = ", ".join(sorted(missing))
        raise ValueError(
            "The input file must contain the following columns: 'sat' and 'colgpa'. "
            f"Missing columns: {missing_cols}"
        )

    return data


def run_regression(data: pd.DataFrame) -> None:
    X = data[["sat"]]
    y = data["colgpa"]

    model = LinearRegression()
    model.fit(X, y)

    coefficient = float(model.coef_[0])
    intercept = float(model.intercept_)
    r_squared = float(model.score(X, y))

    print("Linear Regression Results")
    print("--------------------------")
    print(f"Intercept: {intercept:.4f}")
    print(f"Slope (SAT coefficient): {coefficient:.4f}")
    print(f"R-squared: {r_squared:.4f}")
    print()
    print(
        "Interpretation: For each additional point increase in SAT, the model "
        f"predicts an average change of {coefficient:.4f} in college GPA."
    )


def main() -> None:
    args = parse_args()

    try:
        data = load_data(args.csv_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    run_regression(data)


if __name__ == "__main__":
    main()
