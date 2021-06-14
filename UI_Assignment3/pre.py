import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def line_scatter():
    df = pd.read_csv('lab3-datasets/college-salaries/salaries-by-college-type.csv')
    df = df.sample(frac=0.5, axis=0, random_state=123)
    df.reset_index(inplace=True, drop=True)
    a = df[
        ["Mid-Career 10th Percentile Salary", "Mid-Career 25th Percentile Salary", "Mid-Career 75th Percentile Salary",
         "Mid-Career 90th Percentile Salary"]]
    fig = go.Figure()
    for i in range(0, len(df)):
        fig.add_trace(go.Scatter(name=df["School Name"][i], x=a.columns, y=[df["Mid-Career 10th Percentile Salary"][i],
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
    df = pd.read_csv('lab3-datasets/college-salaries/salaries-by-college-type.csv')

    # Sampling
    df = df.sample(frac=0.5, axis=0, random_state=123)
    # df_state = df[df['School Type'] == 'State'].sample(n=15, replace=False, axis=0)
    # df_art = df[df['School Type'] == 'Liberal Arts'].sample(n=10, replace=False, axis=0)
    # df.drop(labels=df[df['School Type'] == 'State'].index, axis=0, inplace=True)
    # df.drop(labels=df[df['School Type'] == 'Liberal Arts'].index, axis=0, inplace=True)
    #
    # df = pd.concat([df, df_art, df_state])

    fig = px.scatter(df, x="Starting Median Salary", y="Mid-Career Median Salary",
                     size="Mid-Career 75th Percentile Salary", color="School Type", hover_name="School Name",
                     log_x=True, size_max=15)
    fig.update_layout(
        title="Median Salary"
    )

    return fig


def bar_chart(value):
    df = pd.read_csv('lab3-datasets/college-salaries/salaries-by-college-type.csv')
    df = df.iloc[df.groupby(['School Name']).apply(
        lambda x: x['Starting Median Salary'].idxmax())]
    # df = df.sample(frac=0.15, axis=0, random_state=123)
    df.reset_index(inplace=True, drop=True)
    df["Percent change from Starting to Mid-Career Salary"] = (
            (df["Mid-Career Median Salary"] - df["Starting Median Salary"]) * 100 / df["Starting Median Salary"])
    df["Percent change from Starting to Mid-Career Salary"] = [format(x, '.1f') for x in
                                                               df["Percent change from Starting to Mid-Career Salary"]]
    df["Percent change from Starting to Mid-Career Salary"] = df[
        "Percent change from Starting to Mid-Career Salary"].astype("float")
    df = df[value[0] <= df["Percent change from Starting to Mid-Career Salary"]]
    df = df[df["Percent change from Starting to Mid-Career Salary"] <= value[1]]
    fig = px.bar(df, x='School Name', y='Percent change from Starting to Mid-Career Salary')
    fig.update_layout(
        yaxis_title="Growth Rate",
    )
    return fig


def histogram():
    df = pd.read_csv('lab3-datasets/college-salaries/salaries-by-college-type.csv')
    df["Percent change from Starting to Mid-Career Salary"] = (
            (df["Mid-Career Median Salary"] - df["Starting Median Salary"]) * 100 / df["Starting Median Salary"])
    df["Percent change from Starting to Mid-Career Salary"] = [format(x, '.1f') for x in
                                                               df["Percent change from Starting to Mid-Career Salary"]]
    df["Percent change from Starting to Mid-Career Salary"] = df[
        "Percent change from Starting to Mid-Career Salary"].astype("float")
    fig = px.histogram(df, x="Percent change from Starting to Mid-Career Salary")
    fig.update_layout(
        xaxis_title="Growth Rate"
    )
    return fig
