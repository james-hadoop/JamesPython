from transformers import pipeline

# 情感分类，也可以认为是文本分类任务
classifier = pipeline("sentiment-analysis")
sentences = ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
res = classifier(sentences)
print(res)
