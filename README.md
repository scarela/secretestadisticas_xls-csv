# Baseball Game Statistics CSV Generator

This project provides both a Streamlit web app and a CLI tool to process baseball game statistics from a `.xls` file and generate two CSV files:
- **Visitor CSV**: Combines 'VisitorBatting' and 'VisitorPitching' sheets
- **Home CSV**: Combines 'HomeBatting' and 'HomePitching' sheets

## Features
- Upload or process a `.xls` file with the required sheets
- Download or generate the processed CSVs for visitor and home teams
- Handles padding and formatting as required for downstream processing
- Automated tests and GitHub Actions integration

## How to Use

### Streamlit Web App
1. Deploy this app on [Streamlit Cloud](https://streamlit.io/cloud) or run locally with:
    ```sh
    streamlit run streamlit_app.py
    ```
2. Upload your `.xls` file containing the sheets:
    - VisitorBatting
    - VisitorPitching
    - HomeBatting
    - HomePitching
3. Download the generated CSV files using the provided buttons.

### CLI Tool
1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Run the script from the terminal:
    ```sh
    python cli_app.py <path/to/your/file.xls>
    ```
   The files `visitor.csv` and `home.csv` will be generated in the current directory.

## Project Structure
- `core.py`: Core logic for data processing
- `cli_app.py`: Command-line interface entry point
- `streamlit_app.py`: Streamlit web app entry point
- `utils.py`: Utility functions for output
- `requirements.txt`: Python dependencies
- `tests/`: Contains test files and sample `.xls` for validation

## Testing and CI
- Unit tests are provided in `tests/test.py` and compare the generated CSVs with the expected files.
- A GitHub Actions workflow automatically runs the tests on every push or pull request.

---

**Author:** Shamil Carela
