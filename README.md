# Gaussian Process (GP) model for asteroid exposure time predictions

The model is implemented using PyTorch and [GPyTorch](https://docs.gpytorch.ai/en/stable/index.html). The model itself can be found in GP_evaluation.ipynb and GP_asteroid_prediction.ipynb. GP_evaluation.ipynb is for model evaluation and plotting, and GP_asteroid_prediction.ipynb is a fully trained and final model. The same model structure is used in both files. Data is stored in "data" folder, and processed in the Jupyter notebooks.

#### Usage

The model can be used by running GP_evaluation.ipynb or GP_asteroid_prediction.ipynb. A new model is trained each time a notebook is run. Specific (trained) models are not saved. (Saving a trained model is quite simple to implement, check [GPyTorch documentation](https://docs.gpytorch.ai/en/stable/index.html) for information.) Additional information and settings can be seen and changed at the beginning of both notebooks. Plots can be viewed in the notebooks after running them. Possible result tables are saved as .xlsx files in "results" folder after running the notebooks.

#### Additional notes:

- The code was tested with Python 3.10.3
- Used Python packages:
	- torch 2.2.1
	- gpytorch 1.11
	- pandas 1.5.3
	- scikit-learn 1.3.0
	- tqdm 4.65.0
	- matplotlib 3.7.2
	- scipy 1.11.1
