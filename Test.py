import importlib

def import_packages(requirements_file="requirements.txt"):
    with open(requirements_file) as f:
        packages = [line.strip().split("==")[0].split(">=")[0].split("[")[0]
                    for line in f if line.strip() and not line.startswith("#")]

    for pkg in packages:
        try:
            globals()[pkg] = importlib.import_module(pkg)
            print(f"Imported {pkg}")
        except ImportError:
            print(f"Could not import {pkg}")

if __name__ == "__main__":
    import_packages()
    print("hello world, this is Adam Zhu!")
