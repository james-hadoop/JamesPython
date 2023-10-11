from transformers import pipeline

# 完形填空
under_masker = pipeline("fill-mask")
res = under_masker("This course will teach you all about <mask> models.", top_k=2)

print(res)
