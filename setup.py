import pathlib

from setuptools import setup

REPO_ROOT = pathlib.Path(__file__).parent

# Fetch the long description from the readme
with open(REPO_ROOT / "README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name="podcaster",
    include_package_data=True,
    description="Queuer of dreams.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="@vvveracruz",
    license="MIT",
    package_dir={"": "src"},
)