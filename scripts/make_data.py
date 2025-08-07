from configparser import ConfigParser
import csv
import logging
from pathlib import Path
from typing import Optional
from warnings import warn

import h3


def add_h3_field(
    input_file: Path, 
    output_file: Path, 
    h3_resolution: int = 8,
    longitude_field: str = 'longitude', 
    latitude_field: str = 'latitude',
    output_h3_field_name: Optional[str] = None
):
    """
    Read a CSV file, calculate an H3 index from the coordinate columns and saves result to a new file.

    Args:
        input_file: path to the input CSV file
        output_file: path to the output CSV file
        h3_resolution: H3 resolution to use for calculating the H3 index
        longitude_field: field in input CSV with longitude (X) coordinate values
        latitude_field: field in input CSV with latitude (Y) coordinate values
        output_h3_field_name: field to add to output CSV with H3 indices
    """
    logger.debug(f'Using "{longitude_field}" for X coordinates and "{latitude_field}" for '
                 f"coordinates to calculate H3 indices at H3 level {h3_resolution}.")

    # if an output field name is not explicitly provided, create one
    if output_h3_field_name is None:
        output_h3_field_name = f"h3_{h3_resolution:02d}"

    logger.debug(f'Writing H3 indices to new field named "{output_h3_field_name}"')
    
    # open the source CSV and use a reader to load values as dictionaries
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        # create a list of output field names with the new H3 field appended to the end
        fieldnames = reader.fieldnames + [output_h3_field_name]

        # open the file to output to using a dictionary writer
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            # write the field names in the first row, the header
            writer.writeheader()

            # iterate rows in the reader
            for idx, row in enumerate(reader):
                
                # retrive the coordinate values
                lon_val = row.get(longitude_field)
                lat_val = row.get(latitude_field)

                # check to ensure both values are not none
                if lon_val is None or lat_val is None:
                    warn(f'Cannot get H3 index for row {idx:,} because two coordinates values were not retrieved.')
                    h3_idx = None

                else:
                    h3_idx = h3.latlng_to_cell(float(lat_val), float(lon_val), h3_resolution)
                
                # set the H3 index in the row dictionary
                row[output_h3_field_name] = h3_idx

                # write the row to the output table
                writer.writerow(row)

    logger.info(f"{idx+1:,} rows written to {output_file}")

    return output_file

if __name__ == "__main__":

    # path to project root
    dir_prj = Path(__file__).parent.parent

    # read and configure 
    config = ConfigParser()
    config.read(dir_prj / 'config.ini')

    log_level = config.get('DEFAULT', 'LOG_LEVEL')
    input_csv = dir_prj / config.get('DEFAULT', 'INPUT_TABLE')
    output_csv = dir_prj / config.get('DEFAULT', 'OUTPUT_TABLE')
    lon_fld = config.get('DEFAULT', 'LONGITUDE_FIELD')
    lat_fld = config.get('DEFAULT', 'LATITUDE_FIELD')
    h3_res = config.get('DEFAULT', 'H3_RESOLUTION')

    # use the log level from the config to set up logging
    logger = logging.getLogger(Path(__file__).stem)
    logger.setLevel(level=log_level)

    # add H3 indices and write to output table
    add_h3_field(
        input_file=input_csv, 
        output_file=output_csv,
        h3_resolution=h3_res,
        longitude_field=lon_fld,
        latitude_field=lat_fld
    )
