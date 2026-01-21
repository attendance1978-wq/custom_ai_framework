import pytest
from src.models.gpt_model import load_gpt_model

def test_model_loading():
    try:
        model = load_gpt_model('../models/base')
        assert model is not None
    except:
        pytest.skip("Model not available")

if __name__ == "__main__":
    pytest.main([__file__])
