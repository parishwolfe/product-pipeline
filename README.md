# Product Pipeline

[![CodeQL](https://github.com/parishwolfe/product-pipeline/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/parishwolfe/product-pipeline/actions/workflows/github-code-scanning/codeql) [![PEP8 Style Check](https://github.com/parishwolfe/product-pipeline/actions/workflows/pep8.yaml/badge.svg)](https://github.com/parishwolfe/product-pipeline/actions/workflows/pep8.yaml)

This project is an ai based data pipeline. You start by suppling an idea for a category of t-shirt. When the pipeline runs, it does a number of things:

- generates `p` number of patterns using the supplied `idea`
- generates an image with a transparent background with the generated text
- uploads these images to github
- lists and publishes all the new patterns on printify

From there, Printify takes over and the following things happen

- products are synced with shopify, and a number of other retailers
- orders are automatically sent to the print provider when a sale is made

## Running Locally

There are two ways this can be run. The first is as a command line utility, and the second is as a web service.
to run it as a command line utility, run the following command:

```bash
python3.12 product_pipeline.py -p 10 "Idea for a t-shirt"
```

In order to run the application as a web service, run the following command:

```bash
uvicorn product_pipeline:app --host localhost --port 8080 --reload
```

## Deployment

### Google Cloud Functions

Stay tuned for the deployment to GCP!

## Reuqired Environment Variables

Run the following command to generate the required `.env` file. Replace the empty strings with the appropriate values.

```bash
cat <<EOF > .env
PRINTIFY_API_KEY=""
OPENAI_API_KEY=""
GH_PAT=""
GH_UPLOAD_REPO=""
GH_CONTENT_PREFIX=""
EOF
```

Additionally, the shopify utility requires these envronment variables to be set:

```bash
echo 'SHOPIFY_API_KEY=""' >> .env
echo 'SHOPIFY_API_SECRET=""' >> .env
echo 'SHOPIFY_SHOP_NAME=""' >> .env
```

## Running Tests

Formal unit tests are not yet implemented. However, all the functions have a manual test if you run the script directly.

### Main Project

`clear && flake8 --ignore=E501 --exclude=.venv`  

### FastAPI Component

```bash
curl -X POST "http://localhost:8080/process_patterns" \
-H "Content-Type: application/json" \
-d '{"patterns": 1, "idea": "unit testing"}'
```

### Image Utility

`python3.12 image_util.py`  

### AI Utility

`python3.12 ai_util.py`  
