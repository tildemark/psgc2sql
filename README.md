# PSGC to SQL Generator and Data Exporter for Philippine Administrative Divisions

This repository provides Python and PHP scripts to generate SQL INSERT statements for Philippine administrative divisions from the Philippine Standard Geographic Code (PSGC) data. It also includes scripts to extract data from the generated SQL database and export it in various formats.

Easily create and manage SQL databases with lists of provinces, cities, municipalities, and barangays in the Philippines.

**Keywords:** PSGC, Philippines, administrative divisions, provinces, cities, municipalities, barangays, SQL, INSERT statements, database, Python, PHP, CSV, JSON, XML

## Scripts

*   **`psgc_to_sql.py`:** Python script to generate SQL INSERT statements for provinces, cities, municipalities, and barangays.
*   **`xlsx_to_csv.py`:** Python script to convert the PSGC Excel (.xlsx) file to CSV format.
*   **`psgc_to_sql.php`:** PHP script to generate SQL INSERT statements for provinces, cities, municipalities, and barangays.
*   **`extract_data.py`:** Python script to extract data from the SQL database and export it in SQL, CSV, JSON, and XML formats.
*   **`extract_data.php`:** PHP script to extract data from the SQL database and export it in SQL, CSV, JSON, and XML formats.

## Usage

### Generating the SQL Database

1.  **Download PSGC Data:**
    * Download the latest PSGC data in Excel format from the PSA website: [https://psa.gov.ph/classification/psgc](https://psa.gov.ph/classification/psgc)
    * **OR** use the sample PSGC file provided in this repository (`sample_psgc_data.xlsx`).
2.  **Convert to CSV (if necessary):** Use `xlsx_to_csv.py` to convert the Excel file to CSV.
3.  **Generate SQL:**
    * Run `psgc_to_sql.py` (Python) or `psgc_to_sql.php` (PHP) to generate the SQL INSERT statements.
4.  **Create Tables:** Use the provided SQL code (`create_tables.sql`) to create the necessary tables in your database.
5.  **Execute SQL:** Execute the generated SQL INSERT statements in your database management tool (e.g., MySQL Workbench, phpMyAdmin) to populate your database.

### Extracting Data from the Database

1.  **Configure Database Connection:** 
    * **Important:** Update the `db_config` dictionary in `extract_data.py` (Python) or `$dbConfig` array in `extract_data.php` (PHP) with your actual database credentials.
2.  **Run the Script:** 
    * Execute `extract_data.py` (Python) or `extract_data.php` (PHP) to extract data from the specified tables and export it in SQL, CSV, JSON, and XML formats.

## Contents

*   **`sample_psgc_data.xlsx`:** Sample PSGC data file.
*   **`create_tables.sql`:** SQL code to create the necessary database tables.

## Requirements

*   Python 3.6 or higher
*   `openpyxl` library (install using `pip install openpyxl`)
*   `mysql.connector` library (install using `pip install mysql-connector-python`)
*   PHP 7.0 or higher with PDO extension enabled

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

[[MIT License](https://github.com/tildemark/psgc2sql?tab=MIT-1-ov-file)]
