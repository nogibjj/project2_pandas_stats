import pandas as pd
import matplotlib.pyplot as plt
import nbformat as nbf
import pytest
from io import StringIO
from main import summary_statistics, plot_histograms, plot_correlation, create_jupyter

# Sample data with column names including leading spaces
sample_data = """loan_id, no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term
1,0,Graduate,No,50000,200000,15
2,1,Not Graduate,Yes,60000,150000,10
3,2,Graduate,No,70000,250000,20
4,1,Graduate,Yes,80000,300000,25
5,0,Not Graduate,No,90000,350000,30
"""

# Function to create DataFrame from sample data using StringIO
def setup_dataframe():
    return pd.read_csv(StringIO(sample_data))


def test_summary_statistics():
    df = setup_dataframe()
    summary_statistics(df, "test_report.md")

    with open("test_report.md", "r", encoding="utf-8") as file:
        content = file.read()

    assert "### Summary Statistics" in content
    assert "mean" in content
    assert "median" in content
    assert "std_dev" in content
    assert "range" in content
    assert "variance" in content


def test_plot_histograms():
    df = setup_dataframe()

    # Mock plt.savefig to prevent actual file writing for tests
    plt.savefig = lambda *args, **kwargs: None

    plot_histograms(
        df,
        [" income_annum", " loan_amount", " loan_term"],
        [" no_of_dependents"],
        "test_report.md",
    )

    with open("test_report.md", "r", encoding="utf-8") as file:
        content = file.read()

    assert "![Histograms](Histogram_column_distributions.png)" in content
    assert "![no_of_dependents](Bar_graph_no_of_dependents.png)" in content


def test_plot_correlation():
    df = setup_dataframe()

    # Mock plt.savefig to prevent actual file writing for tests
    plt.savefig = lambda *args, **kwargs: None

    plot_correlation(df, "test_report.md")

    with open("test_report.md", "r", encoding="utf-8") as file:
        content = file.read()

    assert "![Correlation Matrix](Correlation_matrix.png)" in content


def test_create_jupyter():
    df = setup_dataframe()
    summary_statistics(df, "test_report.md")
    create_jupyter("test_report.md", "test_report.ipynb")

    with open("test_report.ipynb", "r", encoding="utf-8") as file:
        nb_content = file.read()

    assert "### Summary Statistics" in nb_content

    # Cleanup
    import os

    os.remove("test_report.md")
    os.remove("test_report.ipynb")


# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
