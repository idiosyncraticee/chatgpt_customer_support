`conda create -n startup_gpt python=3.9`

`conda activate startup_gpt`

`jupyter nbconvert startup_gpt_presentation.ipynb --to slides --post serve --ServePostProcessor.port=8081`

`python watch_and_convert.py` automatically looks for the slides file being saved and automatically recompiles.
Need to do a hard refresh to get the updated content

