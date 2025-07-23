from fastapi import FastAPI
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = FastAPI()

# Load model and tokenizer
model_name = "Vamsi/T5_Paraphrase_Paws"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

class Article(BaseModel):
    title: str
    content: str

def rewrite_text(text):
    input_text = "paraphrase: " + text.strip().replace("\n", " ") + " </s>"
    encoding = tokenizer.encode_plus(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(
        input_ids=encoding["input_ids"],
        attention_mask=encoding["attention_mask"],
        max_length=512,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        temperature=0.9,
        num_return_sequences=1
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.post("/rewrite")
async def rewrite_article(article: Article):
    return {
        "title": rewrite_text(article.title),
        "content": rewrite_text(article.content)
    }
