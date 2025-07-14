import os
import shutil
import subprocess

downloads_path = os.path.expanduser("~/Downloads/schema.json")
schema_path = "schemas/schema.json"

# ✅ STEP 1: Only move new schema if it exists
if os.path.exists(downloads_path):
    shutil.move(downloads_path, schema_path)
    print(f"✅ Moved schema.json to: {schema_path}")
else:
    print("⚠️ No new schema found. Using existing schema.json.")

# ✅ STEP 2: Convert to JSON Schema (always, from current file)
converted_path = "schemas/schema_converted.json"
subprocess.run([
    "python", "surveyjs_to_jsonschema.py", 
    schema_path, converted_path
])
print("✅ Converted to JSON Schema")

# ✅ STEP 3: Regenerate Python model from converted schema
subprocess.run([
    "datamodel-codegen",
    "--input", converted_path,  # ✅ FIXED
    "--input-file-type", "jsonschema",
    "--output", "ui/models_dynamic.py",
    "--class-name", "AnnotationForm"
])
print("✅ Generated models_dynamic.py from updated schema.")