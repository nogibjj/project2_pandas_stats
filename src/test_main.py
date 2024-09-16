import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from main import (
    summary_statistics,
    plot_histograms,
    plot_correlation,
    create_jupyter,
)

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
    print("test_summary_statistics passed")


def test_plot_histograms():
    df = setup_dataframe()

    # Mock plt.show to prevent actual plotting for tests
    plt.show = lambda: None
    plot_histograms(df, [" income_annum", " loan_amount", " loan_term"], "test_report.md")
    print("test_plot_histograms passed")


def test_plot_correlation():
    df = setup_dataframe()

    plt.show = lambda: None
    plot_correlation(df, [" income_annum", " loan_amount", " loan_term"], "test_report.md")
    print("test_plot_correlation passed")


def test_create_jupyter():
    df = setup_dataframe()
    summary_statistics(df, "test_report.md")
    create_jupyter("test_report.md", "test_report.ipynb")
    print("test_create_jupyter passed")


# Run the tests
test_summary_statistics()
test_plot_histograms()
test_plot_correlation()
test_create_jupyter()