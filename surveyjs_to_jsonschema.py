import json
import sys
from pathlib import Path

def convert_surveyjs_to_jsonschema(surveyjs):
    schema = {
        "title": "AnnotationForm",
        "type": "object",
        "properties": {},
        "required": []
    }

    for question in surveyjs.get("pages", [])[0].get("elements", []):
        name = question["name"]
        q_type = question.get("type")
        input_type = question.get("inputType")

        prop = {}

        # Handle different question types
        if q_type == "radiogroup" and question.get("choices"):
            prop["type"] = "string"
            prop["enum"] = question["choices"]
        elif q_type == "checkbox":
            prop["type"] = "array"
            prop["items"] = {"type": "string"}
        elif input_type == "number":
            prop["type"] = "integer"
        elif q_type == "ranking":
            prop["type"] = "array"
            prop["items"] = {"type": "string"}
        else:
            prop["type"] = "string"

        # Mark required fields
        if question.get("isRequired"):
            schema["required"].append(name)

        schema["properties"][name] = prop

    return schema

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python surveyjs_to_jsonschema.py input_surveyjs.json output_schema.json")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    with open(input_path) as f:
        surveyjs = json.load(f)

    converted_schema = convert_surveyjs_to_jsonschema(surveyjs)

    with open(output_path, "w") as f:
        json.dump(converted_schema, f, indent=2)

    print(f"✅ Converted schema saved to {output_path}")