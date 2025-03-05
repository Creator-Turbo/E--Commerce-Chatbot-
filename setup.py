from setuptools import setup, find_packages

setup(
    name="E-Commerce-Chatbot",  # Replace with your project name
    version="0.1",  # Version number
    author="Bablu kumar pandey",
    author_email="bablupandey446@gmail.com",
    description="A E-Commerce chatbot using Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Creator-Turbo/E--Commerce-Chatbot-",  
    packages=find_packages(), 
    include_package_data=True,
    install_requires=[
        "langchain-astradb",
        "sentence-transformers",
        "langchain",
        "langchain_huggingface",
        "datasets",
        "pypdf",
        "python-dotenv",
        "flask",
    ],
)
