from pathlib import Path
from setuptools import setup


if __name__ == "__main__":
    setup(
        scripts=list(map(str, Path("bin").rglob("*"))),
    )
