import pytest

from src.postagger.model import POSTagger


@pytest.fixture
def tagger() -> POSTagger:
    return POSTagger()

