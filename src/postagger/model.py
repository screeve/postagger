from typing import List

from transformers import pipeline


class POSTagger:
    def __init__(self):
        self._pipeline = pipeline("token-classification", model="Nargizi/screeve-postagger",
                                  aggregation_strategy='average')

    def __call__(self, text: str) -> List[str]:
        predictions = self._pipeline(text)
        output = []
        for prediction in predictions:
            num_words = len(prediction['word'].split())
            output.extend([prediction['entity_group']] * num_words)
        return output


