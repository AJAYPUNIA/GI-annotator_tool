import os
import shutil
import time

downloads_path = os.path.expanduser("~/Downloads/schema.json")
target_path = "schemas/schema.json"

# Move schema.json to the schemas folder
if os.path.exists(downloads_path):
    shutil.move(downloads_path, target_path)
    print(f"Moved schema.json to: {os.path.abspath(target_path)}")
    
    # Regenerate dynamic form model using datamodel-codegen
    print("⚙️  Regenerating form schema using datamodel-codegen...")
    os.system(
        "datamodel-codegen --input schemas/schema.json "
        "--input-file-type jsonschema "
        "--output ui/models_dynamic.py "
        "--class-name AnnotationForm"
    )
    time.sleep(1)
    print("Form schema regenerated. Now reload Streamlit to see changes.")
else:
    print("No schema.json found in Downloads folder.")