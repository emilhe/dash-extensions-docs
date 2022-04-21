## Download

The `Download` component makes it possible for the user to download in-memory data and/or files. As per Dash 1.20.0, it has been merged into `dash-core-components`. It was kept around in `dash-extensions` for some time to facilitate migration, but it has been dropped in `dash-extensions>=0.1.0`. For general documentation, please refer to [the official Plotly docs](https://dash.plotly.com/dash-core-components/download).

### Send bytes

It is a [common misconception](https://stackoverflow.com/questions/62082946/dash-download-in-memory-generated-file-on-button-click-how-to-give-filename/62088521#62088521) that the `send_bytes` utility function takes an argument of type `bytes`, but it does not. It takes a _function_ that writes to `BytesIO`. While this design choice might not seem obvious at first, it was made to improve compatibility with external libraries (`pandas`, `matplotlib`, etc.). To illustrate the syntax, let's look at a few examples. A typical use case for `send_bytes` is to write excel files,

.. dash-proxy:: components.download_excel

Another common use case is figure objects,

.. dash-proxy:: components.download_figure