import numpy as np
import pandas as pd
from dash import Dash, html, Output, Input, dcc

# Example data.
data = np.column_stack((np.arange(10), np.arange(10) * 2))
df = pd.DataFrame(columns=["a column", "another column"], data=data)
# Create example app.
app = Dash(prevent_initial_callbacks=True)
app.layout = html.Div([html.Button("Download xlsx", id="btn"), dcc.Download(id="download")])

@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
def generate_xlsx(n_nlicks):

    def to_xlsx(bytes_io):
        xslx_writer = pd.ExcelWriter(bytes_io, engine="xlsxwriter")  # requires the xlsxwriter package
        df.to_excel(xslx_writer, index=False, sheet_name="sheet1")
        xslx_writer.save()

    return dcc.send_bytes(to_xlsx, "some_name.xlsx")


if __name__ == '__main__':
    app.run_server()