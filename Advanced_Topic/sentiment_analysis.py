import spacy
from spacy.util import minibatch, compounding
from spacy.training import Example
import warnings

warnings.filterwarnings("ignore")

nlp = spacy.load("en_core_web_sm")

# Example training data
train_data = [
    ("I love this product!", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("This is the worst experience ever.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("I don't like this.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("Absolutely fantastic service!", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("I am very disappointed with the quality.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("Great value for money.", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("I will never buy this again.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("The product exceeded my expectations.", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("Terrible customer support.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("I am extremely happy with my purchase.", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("The item arrived broken.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("Excellent quality and fast shipping.", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("Not worth the price.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("I am satisfied with the product.", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("The worst purchase I've ever made.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("Highly recommend this to everyone.", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("The product does not match the description.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("Very happy with the service.", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("The quality is subpar.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("I will definitely buy this again.", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("bad",{"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("good",{"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
]


# Add a text classifier to the pipeline if it's not already there
if "textcat" not in nlp.pipe_names:
    textcat = nlp.add_pipe("textcat", last=True)
else:
    textcat = nlp.get_pipe("textcat")

# Add labels to the text classifier
textcat.add_label("POSITIVE")
textcat.add_label("NEGATIVE")

# Training the model
optimizer = nlp.begin_training()
for i in range (10):  # Number of iterations
    losses = {}
    batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        texts, annotations = zip(*batch)
        examples = [Example.from_dict(nlp.make_doc(text), annotation) for text, annotation in zip(texts, annotations)]
        nlp.update(examples, sgd=optimizer, drop=0.2, losses=losses)

# Test the model
test_text = input("Enter your statement: ")
doc = nlp(test_text)


if doc.cats['POSITIVE']-doc.cats['NEGATIVE'] < 0.1 and doc.cats['POSITIVE']-doc.cats['NEGATIVE']>0:
    output = "Neutral"
elif doc.cats['POSITIVE']-doc.cats['NEGATIVE'] > 0.1:
    output = "Positive"
else:
    output = "Negative"

print(output)
print(doc.cats)