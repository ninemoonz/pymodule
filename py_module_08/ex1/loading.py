from __future__ import annotations
import sys


try:
    import pandas as pd
except ImportError:
    pd = None

try:
    import numpy as np
except ImportError:
    np = None

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def dependency_check() -> dict[str, str | None]:
    deps: dict[str, str | None] = {}
    for name in ("numpy", "pandas", "matplotlib"):
        try:
            module = __import__(name)
            deps[name] = module.__version__
        except ImportError:
            deps[name] = None
    return deps


def report_dependencies(dp_result: dict[str, str | None]) -> bool:
    intro = {
        "numpy": "Numerical computation ready",
        "pandas": "Data manipulation ready",
        "matplotlib": "Visualization ready",
    }

    dp_ready: bool = True
    for name, version in dp_result.items():
        if version is not None:
            print(f"[OK] {name} ({version}) - {intro[name]}")
        else:
            dp_ready = False
            print(f"[MISSING] {name}")

    if not dp_ready:
        print("\nTo install packages:")
        print("\tpip install -r requirements.txt # using pip")
        print("\tpoetry install                  # using Poetry\n")
    return dp_ready


def gen_data(n: int = 1000, seed: int | None = None) -> "np.ndarray":
    rnp = np.random.default_rng(seed)
    data = rnp.normal(loc=50, scale=1, size=n)
    return data


def data_analysis(data: np.ndarray) -> "pd.DataFrame":
    df = pd.DataFrame(data, columns=["data_column"])
    print(f"Processing {len(df)} data points...")
    return df


def data_visual(df: "pd.DataFrame",
                filename: str = "matrix_analysis.png") -> None:
    print("Generating visulization...\n")
    plt.hist(df["data_column"], bins=50, color="green")
    plt.title("Matrix Data Analysis")
    plt.xlabel("Range")
    plt.ylabel("Count")
    plt.savefig(filename)
    plt.close()
    print("Analysis complete!")
    print(f"Results saved to: {filename}")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    dp_list: dict[str, str | None] = dependency_check()
    dp_bool: bool = report_dependencies(dp_list)
    if not dp_bool:
        sys.exit(1)
    print()
    print("Analyzing Matrix data...")
    data: np.ndarray = gen_data()
    df: pd.DataFrame = data_analysis(data)
    data_visual(df)
