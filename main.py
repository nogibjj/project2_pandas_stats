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
        "loan_id",
        " no_of_dependents",
        " education",
        " self_employed",
        " income_annum",
        " loan_amount",
        " loan_term",
    ]
    df = pd.read_csv(path, usecols=columns)
    return df


# Calculate summary statistics
def summary_statistics(dataframe, report_file):
    summary = dataframe.describe().transpose()
    summary["mean"] = dataframe.mean(numeric_only=True)
    summary["median"] = dataframe.median(numeric_only=True)
    summary["std_dev"] = dataframe.std(numeric_only=True)
    summary["range"] = summary["max"] - summary["min"]
    summary["variance"] = dataframe.var(numeric_only=True)

    # Write output to summary report file
    with open(report_file, "a", encoding="utf-8") as file:
        file.write("### Summary Statistics\n")
        file.write(summary.to_markdown())  # Ensure no extra arguments are passed
        file.write("\n\n")


# Plot histograms for numerical columns and bar graphs for non-numerical columns
def plot_histograms(
    dataframe, numerical_columns, categorical_columns, report_file, bins=20
):
    # Plot histograms for numerical columns
    plt.figure(figsize=(14, 8))
    dataframe[numerical_columns].hist(bins=bins, edgecolor="black", figsize=(14, 8))
    plt.suptitle("Distribution of Numerical Loan Features")
    plt.savefig("Histogram_column_distributions.png")
    plt.close()

    # Plot bar graphs for categorical columns
    for column in categorical_columns:
        plt.figure(figsize=(10, 5))
        dataframe[column].value_counts().plot(kind="bar")
        plt.title(f"Bar Graph of {column.strip()}")
        plt.xlabel(column.strip())
        plt.ylabel("Frequency")
        plt.savefig(f"Bar_graph_{column.strip().replace(' ', '_')}.png")
        plt.close()

    with open(report_file, "a", encoding="utf-8") as file:
        file.write("![Histograms](Histogram_column_distributions.png)\n\n")
        for column in categorical_columns:
            file.write(
                f"![{column.strip()}](Bar_graph_{column.strip().replace(' ', '_')}.png)\n\n"
            )


# Plot correlation heatmap for specified columns and save to the report file
def plot_correlation(dataframe, report_file):
    dataframe_filtered = dataframe.drop(columns=["loan_id"], errors="ignore")
    numeric_columns = dataframe_filtered.select_dtypes(include=["number"]).columns

    # Drop rows with missing values in the numerical columns
    dataframe_filtered = dataframe_filtered[numeric_columns].dropna()
    corr_matrix = dataframe_filtered.corr()
    plt.figure(figsize=(8, 6))
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
        [" income_annum", " loan_amount"],
        [" loan_term", " no_of_dependents"],
        markdown_report,
    )
    plot_correlation(
        df_data,
        markdown_report,
    )

    create_jupyter(markdown_report, notebook_report)
