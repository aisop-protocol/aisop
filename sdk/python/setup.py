from setuptools import setup, find_packages

setup(
    name="aisop",
    version="0.1.0",
    description="Official Python SDK for the AISOP Protocol",
    author="AISOP Maintainers",
    author_email="creator@aisop-protocol.freedom",
    url="https://github.com/aisop-protocol/aisop",
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.0.0"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "aisop=aisop.cli:main",
        ],
    },
)
