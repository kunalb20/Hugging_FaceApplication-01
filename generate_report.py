# generate_report.py
import requests
import json
import time

HUGGING_FACE_API_URL = "https://huggingface.co/api/models"

def fetch_top_models():
    response = requests.get(HUGGING_FACE_API_URL)
    models = response.json()
    # Assuming models list has a 'downloads' key to sort by
    top_models = sorted(models, key=lambda x: x['downloads'], reverse=True)[:10]
    return top_models

def generate_report(models):
    report = "Top 10 Hugging Face Models by Downloads:\n"
    report += "="*40 + "\n"
    for i, model in enumerate(models, 1):
        report += f"{i}. {model['modelId']} - {model['downloads']} downloads\n"
    return report

def save_report(report):
    with open("/reports/top_models_report.txt", "w") as file:
        file.write(report)

def main():
    while True:
        top_models = fetch_top_models()
        report = generate_report(top_models)
        save_report(report)
        # Sleep for 24 hours (86400 seconds) before generating the next report
        time.sleep(86400)

if __name__ == "__main__":
    main()