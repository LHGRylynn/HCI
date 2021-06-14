import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

import pre, pre2, pre3

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='dropdown-value',
            options=[
                {'label': 'salaries by college type', 'value': 'type'},
                {'label': 'salaries by degrees', 'value': 'degree'},
                {'label': 'salaries by region', 'value': 'region'}
            ],
            value='type'
        ),
    ], style={'width': '20%', 'margin': '20px'}),
    html.Div([
        dcc.Graph(
            id='bubble-plot',
            figure=pre.bubble_plot()
        )], style={'width': '40%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(
            id='line-scatter',
            figure=pre.line_scatter()
        )
    ], style={'width': '60%', 'display': 'inline-block'}),
    html.H4(["Percent Change from Starting to Mid-Career Salary"], style={'margin-left': '20px'}),
    html.Div([
        dcc.Tabs(id="tabs-styled-with-props", value='tab-1', children=[
            dcc.Tab(label='Count', value='tab-1'),
            dcc.Tab(label='Detail', value='tab-2'),
        ], colors={
            "border": "white",
            "primary": "DeepSkyBlue",
            "background": "white"
        }),
    ], style={'width': '20%', 'display': 'inline-block', 'margin': '20px'}),
    html.Div(id='tabs-content-props'),

])


@app.callback(Output('tabs-content-props', 'children'),
              Input('tabs-styled-with-props', 'value'),
              Input('dropdown-value', 'value'))
def render_content(tab, dropdown):
    if tab == 'tab-1':
        if dropdown == 'type':
            return html.Div([
                dcc.Graph(
                    id='type-histogram',
                    figure=pre.histogram()
                )
            ])
        elif dropdown == 'region':
            return html.Div([
                dcc.Graph(
                    id='region-histogram',
                    figure=pre2.histogram()
                )
            ])
        elif dropdown=='degree':
            return html.Div([
                dcc.Graph(
                    id='degree-histogram',
                    figure=pre3.histogram()
                )
            ])
        return html.Div([
            dcc.Graph(
                id='type-histogram',
                figure=pre.histogram()
            )
        ])
    elif tab == 'tab-2':
        return html.Div([
            dcc.RangeSlider(
                id='my-range-slider',
                min=0,
                max=135,
                step=5,
                value=[35, 65]
            ),
            html.Div(id='output-container-range-slider', style={'margin-left': '20px'}),
        ])


@app.callback(
    Output('output-container-range-slider', 'children'),
    Input('my-range-slider', 'value'),
    Input('dropdown-value', 'value'))
def update_output(value, dropdown):
    if dropdown == 'type':
        return html.Div([
            'Growth Rate Range: {}'.format(value),
            dcc.Graph(
                id='bar-chart',
                figure=pre.bar_chart(value)
            ),
        ])
    elif dropdown == 'region':
        return html.Div([
            'Growth Rate Range: {}'.format(value),
            dcc.Graph(
                id='bar-chart',
                figure=pre2.bar_chart(value)
            ),
        ])
    elif dropdown == 'degree':
        return html.Div([
            'Growth Rate Range: {}'.format(value),
            dcc.Graph(
                id='bar-chart',
                figure=pre3.bar_chart(value)
            ),
        ])
    return html.Div([
        'Growth Rate Range: {}'.format(value),
        dcc.Graph(
            id='bar-chart',
            figure=pre.bar_chart(value)
        ),
    ])


@app.callback(
    Output('bubble-plot', 'figure'),
    Output('line-scatter', 'figure'),
    Input('dropdown-value', 'value'))
def update_bubble(value):
    if value == "region":
        return pre2.bubble_plot(), pre2.line_scatter()
    elif value == "type":
        return pre.bubble_plot(), pre.line_scatter()
    elif value == "degree":
        return pre3.bubble_plot(),pre3.line_scatter()
    return pre.bubble_plot(), pre.line_scatter()


if __name__ == '__main__':
    app.run_server(debug=True)
