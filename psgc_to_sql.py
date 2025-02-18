import csv

def generate_address_inserts_from_psgc(csv_file, province_table, city_table, sub_municipality_table, barangay_table):
    """
    Generates SQL INSERT statements for provinces, cities, sub-municipalities, and barangays 
    from a PSGC CSV file.

    Args:
        csv_file (str): Path to the PSGC CSV file.
        province_table (str): Name of the SQL table for provinces.
        city_table (str): Name of the SQL table for cities/municipalities.
        sub_municipality_table (str): Name of the SQL table for sub-municipalities.
        barangay_table (str): Name of the SQL table for barangays.
    """

    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                geo_level = row['Geographic Level']
                name = row['Name']
                province_name = row['Province Name']
                city_name = row['City/Municipality Name']  # Adjust if different
                sub_municipality_name = row['Sub Municipality Name']  # Adjust if different

                if geo_level in ('City', 'Municipality'):
                    # Insert City/Municipality
                    sql = f"""
                        INSERT INTO {city_table} (city_name, province_id)
                        VALUES ('{name}', (SELECT province_id FROM {province_table} WHERE province_name = '{province_name}'));
                    """
                    print(sql)

                elif geo_level == 'Sub Municipality':  # Adjust if different
                    # Insert Sub Municipality
                    sql = f"""
                        INSERT INTO {sub_municipality_table} (sub_municipality_name, city_id)
                        VALUES ('{name}', (SELECT city_id FROM {city_table} WHERE city_name = '{city_name}' AND province_id = (SELECT province_id FROM {province_table} WHERE province_name = '{province_name}')));
                    """
                    print(sql)

                elif geo_level == 'Barangay':
                    # Insert Barangay
                    if sub_municipality_name:
                        sql = f"""
                            INSERT INTO {barangay_table} (barangay_name, sub_municipality_id, city_id)
                            VALUES (
                                '{name}', 
                                (SELECT sub_municipality_id FROM {sub_municipality_table} WHERE sub_municipality_name = '{sub_municipality_name}' AND city_id = (SELECT city_id FROM {city_table} WHERE city_name = '{city_name}' AND province_id = (SELECT province_id FROM {province_table} WHERE province_name = '{province_name}'))), 
                                (SELECT city_id FROM {city_table} WHERE city_name = '{city_name}' AND province_id = (SELECT province_id FROM {province_table} WHERE province_name = '{province_name}'))
                            );
                        """
                    else:
                        sql = f"""
                            INSERT INTO {barangay_table} (barangay_name, city_id)
                            VALUES (
                                '{name}', 
                                (SELECT city_id FROM {city_table} WHERE city_name = '{city_name}' AND province_id = (SELECT province_id FROM {province_table} WHERE province_name = '{province_name}'))
                            );
                        """
                    print(sql)

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
generate_address_inserts_from_psgc('psgc_data.csv', 'Provinces', 'Cities', 'SubMunicipalities', 'Barangays')