## Running the application

`conda create -n startup_gpt python=3.9`

`conda activate startup_gpt`

## Using jupyter lab

`conda install -c conda-forge jupyterlab ipykernel`

`python -m ipykernel install --user --name startup_gpt --display-name "startup_gpt"`

`jupyter lab`

## Making slides out of the notebook

`jupyter nbconvert startup_gpt_presentation.ipynb --to slides --post serve --ServePostProcessor.port=8081`

### automatically looks for the slides file being saved and automatically recompiles. Need to do a hard refresh to get the updated content

`python watch_and_convert.py` 
