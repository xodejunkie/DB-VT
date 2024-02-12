import plotly.express as px
import pandas as pd

def generate_sample_plot():
    # Example data
    df = pd.DataFrame({
        "Date": pd.date_range("2021-01-01", periods=30),
        "Value": range(30)
    })

    fig = px.line(df, x="Date", y="Value", title="Sample Data Visualization")
    return fig.to_html()
