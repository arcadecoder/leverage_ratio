import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

### app layout ###
app.layout = html.Div(
    children=[
        html.Div(
            className="content", children=[
                html.H1("Ratio Calculator"),
            ]),
        html.Div(
            className="inputs",
            children=[
                html.H2("Enter your first number: "),
                dcc.Input(id="Input1", type="text", placeholder="1"),
                html.H2("Enter your second number: "),
                dcc.Input(id="Input2", type="text", placeholder="1")
            ]
        ),
        html.Div(
            id="Output"),
    ])


# 3 figures, amount to find the ratio. The ratio is defined by the users
# callbacks

@app.callback(
    Output("Output", "children"), [
        Input('Input1', "value"), Input('Input2', "value")]
)
def calculate_output(Input1, Input2):
    value = int(Input1) * int(Input2)
    out = html.H1(f"The answer is {value}")
    return out
    """
        if Input1 == int and Input2 == int:
        value = int(Input1)*int(Input2)
        out = html.H1(f"The answer is {value}")
        return out
    else:
        return("Please enter your numbers")
    """


if __name__ == "__main__":
    app.run_server(debug=True)
