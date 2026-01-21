# Custom AI Chatbot

A custom AI chatbot built with PyTorch and Transformers.

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Install the package:
   pip install -e .

## Usage

1. Preprocess data:
   python src/data/preprocess.py

2. Train the model:
   chatbot-train

3. Run the API:
   python api/app.py

4. Open web/index.html in browser

## Project Structure

- `src/`: Source code
- `api/`: FastAPI application
- `web/`: Frontend
- `notebooks/`: Jupyter notebooks
- `tests/`: Unit tests
- `models/`: Model files
- `data/`: Data files
