from transformers import pipeline

# 零样本分类
classifier = pipeline("zero-shot-classification")

res = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)

print(res)
