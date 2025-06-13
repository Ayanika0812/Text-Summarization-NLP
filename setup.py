import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarization-NLP"
AUTHOR_USER_NAME = "Ayanika0812"
SRC_REPO = "TextSummarizerNLP"
AUTHOR_EMAIL = "ayanik2a18@gmail.com"

setuptools.setup(
    name=SRC_REPO,  # This should match your package directory
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for NLP text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",  # ✅ fixed this key
    url=f"https://github.com/Ayanika0812/Text-Summarization-NLP",
    project_urls={
        "Bug Tracker": f"https://github.com/Ayanika0812/Text-Summarization-NLP/issues",
    },
    package_dir={"": "src"},  # ✅ this line had a syntax error
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)


