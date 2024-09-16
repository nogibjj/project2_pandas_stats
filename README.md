Check CI/CD Status:
(paste here)

# Mini-project #2
### repo title: project2_pandas_stats

Author: Seijung Kim (sk591)

## Overview
This project is for creating a Python that utilizes the Pandas Library to load a dataset and generate different summary statistics for Exploratory Data Analysis. The generated data visualization and summary report should serve as useful tools to understand the dataset and its variables. You can load this repository to a codespace and make the devcontainer execute the Makefile that will run the following: install, format, lint, test.

## TO DO
Requirements:

* Python script using Pandas for descriptive statistics
* Read a dataset (CSV or Excel)
* Generate summary statistics (mean, median, standard deviation)
* Create at least one data visualization

Deliverable:

* Python script 
* CI/CD with badge
* Generated summary report (PDF or markdown) via CI/CD for extra credit or making your own PDF or MD file and pushing it 

## About the Dataset
`loan_approval_dataset.csv`
This project uses the Loan Approval Prediction Dataset, a common dataset used for Prediction Models for machine learning. This dataset was obtained from Kaggle (https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset?resource=download). Because of the length and complexity of this dataset with a lot of variables, the Python script selects the first seven columns only. This dataset is a collection of financial records and associated information used to determine the eligibility of individuals or organizations for obtaining loans from a lending institution. It includes various factors such as cibil score, income, employment status, loan term, loan amount, assets value, and loan status. This dataset is commonly used in machine learning and data analysis to develop models and algorithms that predict the likelihood of loan approval based on the given features.

#### Variables in the dataset
This dataset inclues a total of 13 variables: `loan_id`, `no_of_dependents`, `education`, `self_employed`, `income_annum`, `loan_amount`, `loan_term`, `cibil_score`, `residential_assets_value`, `commercial_assets_value`, `luxury_assets_value`, `bank_asset_value`, `loan_status`. 
* The projects uses the first 7 of the variables introduced above, which are: `loan_id`, `no_of_dependents`, `education`, `self_employed`, `income_annum`, `loan_amount`, `loan_term`.

## Summary Statistics
The `main.py` provides the mean, median, std_dev, range, and variance. You can generated these statistics using the `summary_statistics` function.

## Statistical functions

## Instructions
This repository should contain the following necessary files to build the GitHub workflow and requirements for executing the scripts for data analysis:

* Makefile
* requirements.txt
* .devcontainer (with .devcontainer.json and Dockerfile)
* .github/workflows for GitHub Actions (with main.yml)
* main.py (using Pandas for data analysis)
* test_main.py (with test functions to test the main.py)

1. Once you load this repository, wait for the installation of requirements.txt
2. You can run the following premade commands `make install`, `make format`, `make lint`, `make test`, or `make all`
3. Check whether you are able to display the statistics and data visualization when running `main.py` and `test_main.py`
4. You can check the full summary documentation as a Jupyter Notebook or PDF. Check `summary_report.md` and `summary_report.ipynb`.
5. To check the full status of the CI/CD pipeline, navigate to the Actions tab of your repository on GitHub.