:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: VARIABLES                                                                    :
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

SETLOCAL
SET CONDA_DIR="%~dp0env"

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: COMMANDS                                                                     :
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: Jump to command
GOTO %1

:: Perform data preprocessing steps contained in the make_data.py script.
:data
    CALL conda run -p %CONDA_DIR% python scripts/make_data.py
    GOTO end

:: Build the local environment from the environment file
:env
    :: Create new environment and add h3-py
    CALL conda create -p %CONDA_DIR% -c conda-forge "h3-py>=4.3" "jupyterlab"
    GOTO end

:end
    EXIT /B
