import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nbformat as nbf

# File paths
file_path = "loan_approval_dataset.csv"
markdown_report = "summary_report.md"
notebook_report = "summary_report.ipynb"

# I am only reading the first seven columns in the csv
def read_csv_file(path):
    columns = [
        'loan_id', ' no_of_dependents', ' education', ' self_employed', 
        ' income_annum', ' loan_amount', ' loan_term'
    ]
    df = pd.read_csv(path, usecols=columns)
    return df


# Calculate summary statistics
def summary_statistics(dataframe, report_file):
    summary = dataframe.describe().transpose()
    summary["mean"] = dataframe.mean(numeric_only=True)
    summary["median"] = dataframe.median(numeric_only=True)
    summary["std_dev"] = dataframe.std(numeric_only=True)
    # I also included range and variance statistics
    summary["range"] = summary["max"] - summary["min"]
    summary["variance"] = dataframe.var(numeric_only=True)

    # Write output to summary report file
    with open(report_file, "a", encoding="utf-8") as file:
        file.write("### Summary Statistics\n")
        file.write(summary.to_string())
        file.write("\n\n")


# Plot histograms for specified columns and save to the report file
def plot_histograms(dataframe, columns, report_file, bins=20):
    plt.figure(figsize=(12, 6))
    dataframe[columns].hist(bins=bins, edgecolor="black", figsize=(14, 8))
    plt.suptitle("Distribution of Loan Features")

    plt.savefig("Histogram_column_distributions.png")
    with open(report_file, "a", encoding="utf-8") as file:
        file.write("![Histograms](Histogram_column_distributions.png)\n\n")


# Plot correlation heatmap for specified columns and save to the report file
def plot_correlation(dataframe, columns, report_file):
    plt.figure(figsize=(8, 6))
    corr_matrix = dataframe[columns].corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")

    plt.savefig("Correlation_matrix.png")
    with open(report_file, "a", encoding="utf-8") as file:
        file.write("![Correlation Matrix](Correlation_matrix.png)\n\n")


# Create a Jupyter notebook with the content of the Markdown
def create_jupyter(report_file, notebook_file):
    nb = nbf.NotebookNode()
    nb.cells = []

    # Read the Markdown content
    with open(report_file, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # Convert Markdown to a notebook cell
    notebook_cell = nbf.NotebookNode(
        cell_type="markdown", metadata={}, source=markdown_content
    )

    nb.cells.append(notebook_cell)

    # Save the notebook to a file
    with open(notebook_file, "w", encoding="utf-8") as file:
        nbf.write(nb, file)


if __name__ == "__main__":
    # Reading the data with specific columns
    df_data = read_csv_file(file_path)

    # Writing summary statistics to the summary report file
    summary_statistics(df_data, markdown_report)

    # Generating plots and saving them in the summary report file
    plot_histograms(
        df_data,
        [" income_annum", " loan_amount", " loan_term", " no_of_dependents"],
        markdown_report,
    )
    plot_correlation(
        df_data,
        [" income_annum", " loan_amount", " loan_term", " no_of_dependents"],
        markdown_report,
    )

    create_jupyter(markdown_report, notebook_report)