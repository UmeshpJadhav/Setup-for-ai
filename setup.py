from setuptools import find_packages, setup

setup(
    name="Chat Bot",  # replace with your package name
    version="0.0.1",
    author="Umesh Jadhav",
    author_email="umeshjdhav.st@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pinecone-haystack",
        "haystack-ai",
        "fastapi",
        "uvicorn",
        "python-dotenv",
        "pathlib"
    ]
)
