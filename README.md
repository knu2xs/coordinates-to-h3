# coordinates-to-h3

Convert coordinates to H3 indices from a CSV file.

## Setup

### Create Conda Environment with H3-Py

Clone the default ArcGIS Pro Conda environment, `arcgispro-py3`  and install `h3-py` to use for looking up H3 indices using the helper command.

``` cmd
make env
```

### Set Options in Config

Set paths to the input and output data in the `config.ini` file.

## Running

Run `./scripts/make_data.py`, the Python module with the necessary function included in the file
using the helper command.

`make data`
