# T5 Paraphraser API

A simple FastAPI-based REST API to rewrite titles and content like a human using the T5 paraphrasing model.

## Endpoints

- `POST /rewrite`
  - Request Body: JSON with `title` and `content`
  - Response: Paraphrased title and content

## Run Locally

```bash
pip install -r requirements.txt
uvicorn rewriter_api:app --host 0.0.0.0 --port 8000
