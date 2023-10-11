from transformers import pipeline

# 文本生成，distilgpt2
generator = pipeline("text-generation", model="distilgpt2")
res = generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
print(res)
