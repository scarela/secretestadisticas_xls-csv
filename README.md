# Baseball Game Statistics CSV Generator

This Streamlit app allows you to upload a baseball game statistics `.xls` file and generates two CSV files:
- **Visitor CSV**: Combines 'VisitorBatting' and 'VisitorPitching' sheets
- **Home CSV**: Combines 'HomeBatting' and 'HomePitching' sheets

## Features
- Upload a `.xls` file with the required sheets
- Download the processed CSVs for visitor and home teams
- Handles padding and formatting as required for downstream processing

## How to Use
1. Deploy this app on [Streamlit Cloud](https://streamlit.io/cloud) or run locally with `streamlit run pa.py`.
2. Upload your `.xls` file containing the sheets:
    - VisitorBatting
    - VisitorPitching
    - HomeBatting
    - HomePitching
3. Download the generated CSV files using the provided buttons.

## Local Development
1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Run the app:
    ```sh
    streamlit run pa.py
    ```

## File Structure
- `pa.py`: Main Streamlit app
- `requirements.txt`: Python dependencies
- `tests/`: Contains test files and sample `.xls` for validation

## Testing
Unit tests are provided in `tests/test.py` to compare generated CSVs with expected outputs.

---

**Author:** Your Name
