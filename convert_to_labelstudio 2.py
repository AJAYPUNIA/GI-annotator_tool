import json

# Load saved form data
with open("data/annotation_20250712_090623.json") as f:
    data = json.load(f)

# Replace with the real source text (can be fetched dynamically later)
report_text = "Example colonoscopy report..."

# Convert to Label Studio JSON format
output = {
    "data": {
        "text": report_text
    },
    "predictions": [
        {
            "model_version": "v1",
            "result": [
                {
                    "from_name": "indication",
                    "to_name": "text",
                    "type": "choices",
                    "value": {"choices": [data["indication"]]}
                },
                {
                    "from_name": "bowel_prep",
                    "to_name": "text",
                    "type": "choices",
                    "value": {"choices": [data["bowel_prep"]]}
                },
                {
                    "from_name": "num_polyps",
                    "to_name": "text",
                    "type": "number",
                    "value": {"number": data["num_polyps"]}
                }
            ]
        }
    ]
}

# Save output
with open("data/labelstudio_format.json", "w") as f:
    json.dump(output, f, indent=2)

print("Label Studio–style JSON saved.")