from transformers import pipeline

# 抽取式问答
question_answerer = pipeline("question-answering")
res = question_answerer(
    question="Where do I work?",
    context="My name is Sylvain and I work at Hugging Face in Brooklyn",
)

print(res)
