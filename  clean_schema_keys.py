import json
import re

with open("schemas/schema_converted.json") as f:
    schema = json.load(f)

cleaned = {}
for k, v in schema["properties"].items():
    clean_key = re.sub(r"\s+", "_", k.strip())
    cleaned[clean_key] = v

schema["properties"] = cleaned

with open("schemas/schema_cleaned.json", "w") as f:
    json.dump(schema, f, indent=2)

print("Cleaned schema saved to schemas/schema_cleaned.json")