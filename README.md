# PolyReg

A small Python package for performing polynomial regression on given data using the mean squared error loss function

## Overview

Polynomial regression extends simple linear regression by incorporating higher degree polynomial terms, allowing a model to capture nonlinear patterns in data.

This project provides python code for experimenting with polynomial regression, with NumPy for numerical computation and Matplotlib for visualisation on given data and predictions on potential future data.

Aimed to complement some of the learning in machine learning.

## Installation

### Prerequisites

- Python 3.8 or later
- pip

### Clone the repository

```bash
git clone https://github.com/MattyAy0001/polyreg.git
cd polyreg
```

### Install dependencies and the package

Install the project in editable mode:

```bash
python -m pip install -e .
```

This installs the package and its declared dependencies. Editable mode also means that changes to the source code are available without reinstalling the package.

## Usage

The `demo/` directory contains examples using given sample data for exploring the project.
The demo files may be executed using the following commands:

```bash
python demo1.py
python demo2.py
```

## Example of use

Vandermonde matrix can be obtained for a given vector x and specified polynomial degree n by importing the vandermonde function:

```python
from vandermonde import Vandermonde

x = [1,2,3,4]
n = 4
Vander = vandermonde(x,len(x),n)
print(Vander)
```

## Project Structure

```text
polyreg/
├── demo/           # Demonstration scripts and examples
├── polyreg/        # Main package code
├── pyproject.toml  # Project metadata and dependencies
└── README.md       # Project documentation and instructions
```

## Dependencies

The project declares the following dependencies in `pyproject.toml`:

- **NumPy** — numerical operations and array computation.
- **Matplotlib** — data visualisation and plotting.


