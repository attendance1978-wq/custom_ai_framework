from setuptools import setup, find_packages

setup(
    name="custom-ai-chatbot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.20.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.20.0",
        "pydantic>=2.0.0",
    ],
    entry_points={
        'console_scripts': [
            'chatbot-train=src.models.train:train_model',
            'chatbot-chat=src.inference.chat:main',
        ],
    },
)
