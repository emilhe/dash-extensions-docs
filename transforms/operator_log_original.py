...

@app.callback(Output("log", "children"), Input("btn", "n_clicks"), State("log", "children"))
def append_to_log(n_clicks, current_log):
    log_entry = f"{datetime.datetime.now().isoformat()}: BUTTON CLICKED (n_clicks={n_clicks})"
    log = current_log + [dmc.ListItem(log_entry)]
    return log

...
