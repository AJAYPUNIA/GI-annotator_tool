# GI_annotator_tool


hem out alongside clinical reports, and export the results for easy analysis.

What This Tool Does-----
Design your own forms using a Google Forms–like interface (SurveyJS).
Convert form design to code automatically using a Pydantic schema.
Load clinical text side-by-side with the form.
Save both the form data and source text in one structured JSON file.
Use saved files for comparison between human annotations and LLM-generated outputs.


Key Features-----
Supports dynamic form creation through SurveyJS
Automatically builds a data model (schema.json) from your form
Renders the form live using Streamlit
Lets you save your entries with or without the source document
Allows download of the completed form + clinical note as a .json file


Setup-----
# Clone the repo
git clone https://github.com/AJAYPUNIA/GI-annotator_tool.git
cd GI-annotator_tool

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt


Launch the App-----
streamlit run app.py
