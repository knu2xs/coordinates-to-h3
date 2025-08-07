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
    CALL conda create -p %CONDA_DIR% -c conda-forge "h3-py>=4.3" "jupyterlab" -y
    GOTO end

:: Start Jupyter Lab with ability to connect from another machine
:jupyter
    CALL conda run -p %CONDA_DIR% python -m jupyterlab --ip=0.0.0.0 --allow-root --NotebookApp.token=""
    GOTO end

:end
    EXIT /B
