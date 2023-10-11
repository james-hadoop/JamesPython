from transformers import pipeline

# 翻译
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
res = translator("Ce cours est produit par Hugging Face.")
print(res)
