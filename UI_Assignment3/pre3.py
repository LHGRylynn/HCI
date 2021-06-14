import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def line_scatter():
    df = pd.read_csv('lab3-datasets/college-salaries/degrees-that-pay-back.csv')
    df = df.sample(frac=0.5, axis=0, random_state=123)
    df.reset_index(inplace=True, drop=True)
    a = df[
        ["Mid-Career 10th Percentile Salary", "Mid-Career 25th Percentile Salary", "Mid-Career 75th Percentile Salary",
         "Mid-Career 90th Percentile Salary"]]
    fig = go.Figure()
    for i in range(0, len(df)):
        fig.add_trace(go.Scatter(name=df["Undergraduate Major"][i], x=a.columns, y=[df["Mid-Career 10th Percentile Salary"][i],
                                                                            df["Mid-Career 25th Percentile Salary"][i],
                                                                            df["Mid-Career 75th Percentile Salary"][i],
                                                                            df["Mid-Career 90th Percentile Salary"][
                                                                                i]]))
    fig.update_layout(
        title="Mid-Career Percentile Salary",
        yaxis_title="Mid-Career Salary",
    )
    return fig


def bubble_plot():
    df = pd.read_csv('lab3-datasets/college-salaries/degrees-that-pay-back.csv')

    df = df.sample(frac=0.5, axis=0, random_state=123)

    fig = px.scatter(df, x="Starting Median Salary", y="Mid-Career Median Salary",
                     size="Mid-Career 75th Percentile Salary", color="Undergraduate Major", hover_name="Undergraduate Major",
                     log_x=True, size_max=15)
    fig.update_layout(
        title="Median Salary",

    )
    return fig


def bar_chart(value):
    df = pd.read_csv('lab3-datasets/college-salaries/degrees-that-pay-back.csv')

    df = df[value[0] <= df["Percent change from Starting to Mid-Career Salary"]]
    df = df[df["Percent change from Starting to Mid-Career Salary"] <= value[1]]
    fig = px.bar(df, x='Undergraduate Major', y='Percent change from Starting to Mid-Career Salary')
    fig.update_layout(
        # title="Percent Change from Starting to Mid-Career Salary",
        yaxis_title="Growth Rate",
    )
    return fig


def histogram():
    df = pd.read_csv('lab3-datasets/college-salaries/degrees-that-pay-back.csv')
    fig = px.histogram(df, x="Percent change from Starting to Mid-Career Salary")
    fig.update_layout(
        xaxis_title="Growth Rate"
    )
    return fig
