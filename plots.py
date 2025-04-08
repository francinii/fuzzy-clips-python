import plotly.graph_objects as go

def plot_membership(variable, eval_value=None, title="", xaxis_title="", var_label="", y_max=1):
    fig = go.Figure()

    for term_name in variable.terms:
        fig.add_trace(go.Scatter(
            x=variable.universe,
            y=variable[term_name].mf,
            name=term_name.capitalize()
        ))

    if eval_value is not None:
        fig.add_trace(go.Scatter(
            x=[eval_value, eval_value],
            y=[0, y_max],
            mode='lines',
            name=f'{var_label} = {round(eval_value, 2)}',
            line=dict(color='black', dash='dash')
        ))

    fig.update_layout(
        title=dict(text=title, font=dict(size=18, color='darkblue')),
        xaxis_title=xaxis_title,
        xaxis_title_font=dict(size=10),
        yaxis_title='Grado de Membresía',
        yaxis_title_font=dict(size=10),
        font=dict(size=12),
        width=800,
        height=400,
        yaxis=dict(range=[0, y_max]),
        legend=dict(orientation="h", y=-0.3, x=0.5, xanchor="center")
    )

    return fig