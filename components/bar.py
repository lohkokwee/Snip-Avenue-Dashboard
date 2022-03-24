import plotly.graph_objects as go

def get_bar(x, y, x_label, y_label):

    fig = go.Figure(go.Bar(
        x = x, 
        y = y, 
        text = y, 
        textposition = 'auto')
    )

    fig.update_layout(
        xaxis_title_text = x_label,
        yaxis_title_text = y_label,
    )

    return fig