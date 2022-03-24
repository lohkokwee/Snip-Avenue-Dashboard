import plotly.graph_objects as go

def get_line(x, y, x_label, y_label):

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x = x,
        y = y,
        name = 'linear',
        line_shape = 'spline',
        text = y,
        textposition = 'top center'
    ))

    fig.update_layout(
        xaxis_title_text = x_label,
        yaxis_title_text = y_label,
        xaxis = dict(showgrid = False),
    )

    return fig