import plotly.express as px

def generate_sample_plot():
    df = ...  # Load your data here
    fig = px.line(df, x="date", y="value", title="Sample Plot")
    return fig.to_html()
