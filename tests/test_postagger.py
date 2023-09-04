from src.postagger.model import POSTagger


def test_postagger(tagger: POSTagger) -> None:
    assert tagger('მე მივდივარ სახლში') == ['Pron', 'V', 'N']


