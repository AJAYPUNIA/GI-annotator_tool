import streamlit as st
import importlib
import json, os, time
from datetime import datetime
import subprocess

# Run update_schema_pipeline.py automatically
print("Checking for new schema...")
subprocess.run(["python", "update_schema_pipeline.py"])
st.set_page_config(page_title="GI Annotation App", layout="wide")

schema_timestamp = os.path.getmtime("schemas/schema.json")
st.caption(f"Schema last updated: {datetime.fromtimestamp(schema_timestamp).strftime('%Y-%m-%d %H:%M:%S')}")

# Function to load model dynamically
def load_model():
    import ui.models_dynamic
    importlib.reload(ui.models_dynamic)
    return ui.models_dynamic.AnnotationForm

# Reload schema and regenerate model
if st.button("Reload Schema and Refresh Form"):
    with st.spinner("Reloading schema and regenerating form..."):

        # Convert if schema.json is still in SurveyJS format
        os.system("python surveyjs_to_jsonschema.py schemas/schema.json schemas/schema_converted.json")

        # Generate the Pydantic model from converted schema
        os.system(
            "datamodel-codegen --input schemas/schema_converted.json "
            "--input-file-type jsonschema "
            "--output ui/models_dynamic.py "
            "--class-name AnnotationForm"
        )

        # Reload the dynamic model class
        import ui.models_dynamic
        importlib.reload(ui.models_dynamic)
        AnnotationForm = ui.models_dynamic.AnnotationForm

        time.sleep(1)
        st.rerun()

# Always use the latest model
AnnotationForm = load_model()

# Render form
from streamlit_pydantic import pydantic_input
st.title("GI Annotation App")
# Layout: Side-by-side Source Document + Annotation Form
col1, col2 = st.columns([1, 2])  # 1:2 ratio for left and right panel

with col1:
    st.markdown("### Source Document")
    source_text = st.text_area("Paste or load clinical report here", height=300)

with col2:
    st.markdown("### Annotation Form")
    data = pydantic_input("Annotation Form", model=AnnotationForm)
# Show real-time preview
if data:
    st.subheader("Live Preview of Form Data")
    st.json(data)

    # Ask user for a custom filename
    custom_name = st.text_input("Enter filename (without .json):", "")
        # Save form data and source document
if data and st.button("Save Form Data"):
    os.makedirs("data", exist_ok=True)

    # Use user-specified filename or timestamp fallback
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    default_filename = f"annotation_{timestamp}.json"
    user_filename = st.text_input("Optional: Enter file name", value=default_filename)
    filename = f"data/{user_filename}"

    # Save both source text and form data
    with open(filename, "w") as f:
        json.dump({
            "source_text": source_text,
            "form_data": data
        }, f, indent=2)

    st.success(f"Form data saved successfully as: {filename}")