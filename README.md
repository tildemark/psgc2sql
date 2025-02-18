# PSGC to SQL Generator

This repository provides Python scripts to generate SQL INSERT statements for Philippine administrative divisions from the Philippine Standard Geographic Code (PSGC) data. Easily create SQL databases with lists of provinces, cities, municipalities, and barangays in the Philippines.

**Keywords:** PSGC, Philippines, administrative divisions, provinces, cities, municipalities, barangays, SQL, INSERT statements, database, Python

## Scripts

*   **`psgc_to_sql.py`:** Python script to generate SQL INSERT statements for provinces, cities, municipalities, and barangays.
*   **`xlsx_to_csv.py`:** Python script to convert the PSGC Excel (.xlsx) file to CSV format.

## Usage

1.  **Download PSGC Data:** Download the latest PSGC data in Excel format from the PSA website: [https://psa.gov.ph/classification/psgc](https://psa.gov.ph/classification/psgc)
2.  **Convert to CSV:** Use `xlsx_to_csv.py` to convert the Excel file to CSV.
3.  **Generate SQL:** Run `psgc_to_sql.py` to generate the SQL INSERT statements.
4.  **Execute SQL:** Execute the generated SQL statements in your database management tool (e.g., MySQL Workbench, phpMyAdmin) to populate your database.

**Note:** You might need to adjust the scripts to match the exact structure and column names of the PSGC data you download.

## Requirements

*   Python 3.6 or higher
*   `openpyxl` library (install using `pip install openpyxl`)

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

[Choose a license (e.g., MIT License)](https://choosealicense.com/)
