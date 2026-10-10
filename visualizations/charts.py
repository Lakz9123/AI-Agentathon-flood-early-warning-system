import plotly.graph_objects as go

# Custom colors for Mission Command Glass aesthetic
CYAN = "#00F2FE"
RED = "#EF4444"
ORANGE = "#F59E0B"
GREEN = "#10B981"
DARK_NAVY = "#0B0E14"
GLASS_BG = "rgba(255, 255, 255, 0.02)"
GRID_COLOR = "rgba(0, 242, 254, 0.1)"

def get_base_layout(title, yaxis_title=""):
    return dict(
        title={'text': title, 'font': {'color': CYAN, 'family': 'Courier New, monospace', 'size': 14}},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E2E8F0', family='Courier New, monospace'),
        margin=dict(l=30, r=20, t=40, b=20),
        xaxis=dict(showgrid=False, color=CYAN, tickfont=dict(size=10)),
        yaxis=dict(title=yaxis_title, showgrid=True, gridcolor=GRID_COLOR, gridwidth=1, griddash='dot', color=CYAN, tickfont=dict(size=10)),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=10))
    )

def create_risk_gauge(score):
    """Creates a gauge chart for the flood risk score."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={'font': {'color': CYAN, 'size': 40, 'family': 'Courier New, monospace'}},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': CYAN, 'tickfont': {'color': CYAN, 'family': 'Courier New, monospace'}},
            'bar': {'color': CYAN, 'thickness': 0.3},
            'bgcolor': GLASS_BG,
            'borderwidth': 1,
            'bordercolor': GRID_COLOR,
            'steps': [
                {'range': [0, 39], 'color': "rgba(16, 185, 129, 0.2)"},
                {'range': [40, 69], 'color': "rgba(245, 158, 11, 0.2)"},
                {'range': [70, 100], 'color': "rgba(239, 68, 68, 0.2)"}],
            'threshold': {
                'line': {'color': RED, 'width': 2},
                'thickness': 0.4,
                'value': 70}
        }
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': CYAN, 'family': 'Courier New, monospace'},
        margin=dict(l=20, r=20, t=20, b=20),
        height=200
    )
    return fig

def create_rainfall_chart(forecast_mm):
    """Creates a bar chart showing rainfall forecast."""
    fig = go.Figure(data=[
        go.Bar(name='Forecast', x=['Next 24h'], y=[forecast_mm], marker_color=CYAN, width=0.4)
    ])
    fig.update_layout(**get_base_layout('Precipitation Forecast (mm)', 'mm'), height=200)
    fig.add_hline(y=100, line_dash="dot", line_color=RED, annotation_text="Heavy", annotation_font_color=RED, annotation_font_size=10)
    return fig

def create_water_level_chart(current, danger):
    """Creates a chart comparing current water level to danger level."""
    fig = go.Figure(data=[
        go.Bar(name='Current', x=['Level'], y=[current], marker_color=CYAN, width=0.3),
        go.Bar(name='Danger', x=['Level'], y=[danger], marker_color=RED, width=0.3)
    ])
    fig.update_layout(**get_base_layout('Hydro-gauge Level (m)', 'Height (m)'), barmode='group', height=200)
    return fig

def create_citizen_complaints_chart(count):
    """Creates a simple bar chart for citizen complaints."""
    fig = go.Figure(data=[
        go.Bar(name='Complaints', x=['Today'], y=[count], marker_color=ORANGE, width=0.4)
    ])
    fig.update_layout(**get_base_layout('Telemetry Signals', 'Count'), height=200)
    return fig
