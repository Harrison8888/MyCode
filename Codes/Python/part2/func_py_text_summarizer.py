# func_py_text_summarizer.py
import re
from collections import Counter

def func_py_text_summarizer(text, top_n=5):
    text = re.sub(r"[^\w\s]", "", text.lower())
    words = text.split()
    word_counts = Counter(words)
    return dict(word_counts.most_common(top_n))

sample_text = """
Artificial intelligence and machine learning are transforming the world. AI models process large amounts of data 
to find patterns and make decisions. Machine learning algorithms are widely used in industries like healthcare, 
finance, and autonomous vehicles.
"""

print(func_py_text_summarizer(sample_text, 5))
