# coordinates-to-h3

Convert coordinates to H3 indices from a CSV file.

## Setup

### Create Conda Environment with H3-Py

Clone a Python environment and install `h3-py` to use for looking up H3 indices using the helper command.

``` cmd
make env
```

### Set Options in Config

Set paths to the input and output data in the `config.ini` file. Most notably, set the input and output file locations.

## Running

``` cmd
make data
```

Run the execution code in the Python module, `./scripts/make_data.py`, using the configuration
options from `./config.ini` to copy the source CSV file, add H3 indices, and write to the output
CSV file.

``` cmd
make juptyer
```

Start jupyter notebook using the project environment created using `make env` to run the example noteboook.
