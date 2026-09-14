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
    import matplotlib as mpl
except ImportError:
    mpl = None


def dependency_check() -> dict:
    deps: dict = {}
    for name in ("numpy", "pandas", "matplotlib"):
        try:
            module = __import__(name)
            deps[name] = module.__version__
        except ImportError:
            deps[name] = None
    return deps


def report_dependencies(dp_result: dict) -> bool:
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


def gen_data(n=1000, seed=None):
    rnp = np.random.default_rng(seed)
    data = rnp.normal(loc=0, scale=1, size=n)
    return data


def data_analysis(data: list[float]) -> None:
    df = pd.DataFrame(data)
    print(f"Processing {len(df)} data points...")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    dp_list: dict = dependency_check()
    dp_bool: bool = report_dependencies(dp_list)
    if not dp_bool:
        sys.exit(1)
    print()
    data: list[float] = gen_data()
    print("Analyzing Matrix data...")
    data_analysis(data)
