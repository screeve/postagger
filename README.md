# Part-of-Speech Tagger
Part-of-speech tagging functionality for Georgian language. screeve-postagger is a small encoder model trained on Georgian National Corpus for part-of-speech tagging Georgian senteces

You can use this model with Transformers pipeline for token-classifcation.


```python
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

model = AutoModelForTokenClassification.from_pretrained("Nargizi/screeve-postagger")
tokenizer = AutoTokenizer.from_pretrained("Nargizi/screeve-postagger")

tagger = pipeline("token-classification", model=model, tokenizer=tokenizer)

ka_sentence = "მე მივდივარ სახლში."
resutls = tagger(ka_sentence, aggregation_strategy='average')
print(results)
```

Label descriptions:

Abbreviation|Description
-|-
V| Verb
N | Noun
Pron | Pronoun
Interj | Interjection
A |Person’s name
Adv | Adverb
Cj | Conjunction
Punct | Punctuation
Num | Number
Pp |Preposition
