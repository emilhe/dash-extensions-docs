import numpy as np
import pandas as pd
from dash_extensions.enrich import DashProxy, html, Output, Input, dcc

# Example data.
data = np.column_stack((np.arange(10), np.arange(10) * 2))
df = pd.DataFrame(columns=["a column", "another column"], data=data)
# Create example app.
app = DashProxy(prevent_initial_callbacks=True)
app.layout = html.Div([html.Button("Download xlsx", id="btn_xslx"), dcc.Download(id="download_xslx")])

@app.callback(Output("download_xslx", "data"), [Input("btn_xslx", "n_clicks")], prevent_initial_call=True)
def generate_xlsx(n_nlicks):

    def to_xlsx(bytes_io):
        xslx_writer = pd.ExcelWriter(bytes_io, engine="xlsxwriter")  # requires the xlsxwriter package
        df.to_excel(xslx_writer, index=False, sheet_name="sheet1")
        xslx_writer.close()

    return dcc.send_bytes(to_xlsx, "some_name.xlsx")


if __name__ == '__main__':
    app.run_server()