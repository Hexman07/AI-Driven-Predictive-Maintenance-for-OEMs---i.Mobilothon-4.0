import dash
from dash import html, dcc

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div(
    style={"font-family": "Arial", "margin": "20px"},
    children=[
        # Header Section
        html.Div(
            style={"background-color": "#e6f7ff", "padding": "10px"},
            children=[
                html.H1(
                    "AI-Driven Energy Optimization for OEM Factories",
                    style={"text-align": "center", "color": "#003366"},
                )
            ],
        ),
        
        # First Row of Images
        html.Div(
            style={"display": "flex", "justify-content": "space-around", "margin-bottom": "20px"},
            children=[
                html.Img(src="/assets/efficiency_score1.png", style={"width": "30%"}),
                html.Img(src="/assets/efficiency_score2.png", style={"width": "30%"}),
                html.Img(src="/assets/efficiency_score3.png", style={"width": "30%"}),
            ],
        ),

        # Second Row with Carousel 1
        html.Div(
            style={"overflow-x": "auto", "white-space": "nowrap", "margin-bottom": "20px"},
            children=[
                html.Img(src="/assets/operational_status.png", style={"width": "30%", "margin-right": "10px"}),
                html.Img(src="/assets/energy_consumption.png", style={"width": "30%", "margin-right": "10px"}),
                html.Img(src="/assets/efficiency_distribution.png", style={"width": "30%", "margin-right": "10px"}),
            ],
        ),

        # Third Row
        html.Div(
            style={"display": "flex", "justify-content": "space-around", "margin-bottom": "20px"},
            children=[
                html.Img(src="/assets/machine_temp1.png", style={"width": "45%"}),
                html.Img(src="/assets/machine_temp2.png", style={"width": "45%"}),
            ],
        ),

        # Fourth Row with Carousel 2
        html.Div(
            style={"overflow-x": "auto", "white-space": "nowrap", "margin-bottom": "20px"},
            children=[
                html.Img(src="/assets/top_10_risk_machines.png", style={"width": "30%", "margin-right": "10px"}),
                html.Img(src="/assets/machine_efficiency_region.png", style={"width": "30%", "margin-right": "10px"}),
                html.Img(src="/assets/factory_clustering.png", style={"width": "30%", "margin-right": "10px"}),
            ],
        ),

        # Fifth Row
        html.Div(
            style={"display": "flex", "justify-content": "space-around", "margin-bottom": "20px"},
            children=[
                html.Img(src="/assets/seasonal_trends.png", style={"width": "45%"}),
                html.Img(src="/assets/average_efficiency_scores.png", style={"width": "45%"}),
            ],
        ),

        # Sixth Row with Carousel 3
        html.Div(
            style={"overflow-x": "auto", "white-space": "nowrap", "margin-bottom": "20px"},
            children=[
                html.Img(src="/assets/most_underperforming.png", style={"width": "30%", "margin-right": "10px"}),
                html.Img(src="/assets/machine_energy_temp.png", style={"width": "30%", "margin-right": "10px"}),
                html.Img(src="/assets/additional_insights.png", style={"width": "30%", "margin-right": "10px"}),
            ],
        ),
    ],
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
