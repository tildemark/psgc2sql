<?php

/**
 * Generates SQL INSERT statements for provinces, cities, sub-municipalities, and barangays
 * from a PSGC CSV file.
 *
 * @param string $csvFile Path to the PSGC CSV file.
 * @param string $provinceTable Name of the SQL table for provinces.
 * @param string $cityTable Name of the SQL table for cities/municipalities.
 * @param string $subMunicipalityTable Name of the SQL table for sub-municipalities.
 * @param string $barangayTable Name of the SQL table for barangays.
 */
function generateAddressInsertsFromPsgc(
    string $csvFile,
    string $provinceTable,
    string $cityTable,
    string $subMunicipalityTable,
    string $barangayTable
): void {
    if (($handle = fopen($csvFile, "r"))!== FALSE) {
        // Skip the header row
        fgetcsv($handle); 

        while (($data = fgetcsv($handle, 1000, ","))!== FALSE) {
            $geoLevel = $data; // Assuming 'Geographic Level' is in the first column
            $name = $data;     // Assuming 'Name' is in the second column
            $provinceName = $data; // Assuming 'Province Name' is in the third column
            $cityName = $data;     // Assuming 'City/Municipality Name' is in the fourth column
            $subMunicipalityName = $data; // Assuming 'Sub Municipality Name' is in the fifth column

            if ($geoLevel == 'City' || $geoLevel == 'Municipality') {
                // Insert City/Municipality
                $sql = "INSERT INTO $cityTable (city_name, province_id) ".
                       "VALUES ('$name', (SELECT province_id FROM $provinceTable WHERE province_name = '$provinceName'));";
                echo $sql. "<br>";

            } elseif ($geoLevel == 'Sub Municipality') {
                // Insert Sub Municipality
                $sql = "INSERT INTO $subMunicipalityTable (sub_municipality_name, city_id) ".
                       "VALUES ('$name', (SELECT city_id FROM $cityTable WHERE city_name = '$cityName' AND province_id = (SELECT province_id FROM $provinceTable WHERE province_name = '$provinceName')));";
                echo $sql. "<br>";

            } elseif ($geoLevel == 'Barangay') {
                // Insert Barangay
                if (!empty($subMunicipalityName)) {
                    $sql = "INSERT INTO $barangayTable (barangay_name, sub_municipality_id, city_id) ".
                           "VALUES ('$name', (SELECT sub_municipality_id FROM $subMunicipalityTable WHERE sub_municipality_name = '$subMunicipalityName' AND city_id = (SELECT city_id FROM $cityTable WHERE city_name = '$cityName')), (SELECT city_id FROM $cityTable WHERE city_name = '$cityName'));";
                    
                } else {
                    $sql = "INSERT INTO $barangayTable (barangay_name, city_id) ".
                           "VALUES ('$name', (SELECT city_id FROM $cityTable WHERE city_name = '$cityName'));";
                }
                echo $sql. "<br>";
            }
        }
        fclose($handle);
    } else {
        echo "Error opening the file.";
    }
}

// Example usage:
generateAddressInsertsFromPsgc('psgc_data.csv', 'Provinces', 'Cities', 'SubMunicipalities', 'Barangays'); ?>