# Gaussian Process (GP) model for asteroid exposure time predictions

The model is implemented using PyTorch and GPyTorch. The model itself can be found in GP_evaluation.ipynb and GP_asteroid_prediction.ipynb. GP_evaluation.ipynb is for model evaluation and plotting, and GP_asteroid_prediction.ipynb is a fully trained and final model. The same model structure is used in both files. Data is stored in "data" folder, and processed in the Jupyter notebooks.

#### Usage

The model can be used by running GP_evaluation.ipynb or GP_asteroid_prediction.ipynb. Additional information and settings can be seen and changed at the beginning of both notebooks. Plots can be viewed in the notebooks after running them. Possible result tables are saved as .xlsx files in "results" folder after running the notebooks.

#### Additional notes:

- The code was tested with Python 3.10.3
- Used Python packages:
	- torch
	- gpytorch
	- pandas
	- sklearn
	- tqdm
	- matplotlib
	- scipy
