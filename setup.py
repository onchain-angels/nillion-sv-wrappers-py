from setuptools import setup, find_packages

setup(
    name="nillion-sv-wrappers-py",
    version="0.1.0",
    description="Python implementation of wrappers for Nillion (SecretVault and NilQL)",
    author="Andre Teves",
    url="https://github.com/onchain-angels/nillion-sv-wrappers-py",
    packages=find_packages(include=["nillion_sv_wrappers", "nillion_sv_wrappers.*"]),
    package_dir={"": "src"},
    install_requires=[
        "httpx>=0.28.0",
        "PyJWT>=2.10.0",
        "python-decouple>=3.4",
        "nilql @ git+https://github.com/NillionNetwork/nilql-py.git#egg=nilql",
        "ecdsa>=0.19.0",
        "cryptography>=44.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
