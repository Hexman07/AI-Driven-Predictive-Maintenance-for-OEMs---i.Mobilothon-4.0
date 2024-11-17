import dash
from dash import html

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div(
    style={"font-family": "Arial", "margin": "20px", "background-color": "#F5F5F5"},
    children=[
        # Header Section
        html.Div(
            style={
                "background-color": "#88B3E1",
                "padding": "20px",
                "border-radius": "8px",
                "display": "flex",
                "justify-content": "space-between",
                "align-items": "center",
            },
            children=[
                html.H1("DASHBOARD", style={"color": "white", "margin": "0"}),
                html.H2(
                    "AI-Driven Energy Optimization for OEM Factories",
                    style={"color": "white", "margin": "0"},
                ),
            ],
        ),
        # Section 1
        html.Div(
            style={
                "margin-top": "32px",
                "padding": "20px",
                "background-color": "white",
                "border-radius": "8px",
            },
            children=[
                html.H3(
                    "Efficiency Score Over Time",
                    style={"text-align": "center", "color": "#88B3E1"},
                ),
                html.Div(
                    style={
                        "overflow-x": "auto",
                        "white-space": "nowrap",
                        "margin-top": "16px",
                    },
                    children=[
                        html.Img(
                            src=f"/assets/efficiency_score_{i}.png",
                            style={
                                "width": "30%",
                                "margin-right": "10px",
                                "border-radius": "8px",
                            },
                        )
                        for i in range(1, 9)  # 8 graphs
                    ],
                ),
            ],
        ),
        # Section 2
        html.Div(
            style={
                "margin-top": "32px",
                "padding": "20px",
                "background-color": "white",
                "border-radius": "8px",
            },
            children=[
                html.H3(
                    "Operational Status Distribution",
                    style={"text-align": "center", "color": "#88B3E1"},
                ),
                html.Img(
                    src="/assets/operational_status.png",
                    style={"width": "100%", "border-radius": "8px", "margin-top": "16px"},
                ),
            ],
        ),
        # Section 3
        html.Div(
            style={
                "margin-top": "32px",
                "padding": "20px",
                "background-color": "white",
                "border-radius": "8px",
            },
            children=[
                html.H3(
                    "Total Energy Consumption by Machine Type",
                    style={"text-align": "center", "color": "#88B3E1"},
                ),
                html.Img(
                    src="/assets/energy_consumption.png",
                    style={"width": "100%", "border-radius": "8px", "margin-top": "16px"},
                ),
            ],
        ),
        # Section 4
        html.Div(
            style={
                "margin-top": "32px",
                "padding": "20px",
                "background-color": "white",
                "border-radius": "8px",
            },
            children=[
                html.H3(
                    "Distribution of Machine Efficiency Scores",
                    style={"text-align": "center", "color": "#88B3E1"},
                ),
                html.Img(
                    src="/assets/efficiency_distribution.png",
                    style={"width": "100%", "border-radius": "8px", "margin-top": "16px"},
                ),
            ],
        ),
        # Section 5
        html.Div(
            style={
                "margin-top": "32px",
                "padding": "20px",
                "background-color": "white",
                "border-radius": "8px",
            },
            children=[
                html.H3(
                    "Machine Temperature for Each Machine Type",
                    style={"text-align": "center", "color": "#88B3E1"},
                ),
                html.Div(
                    style={
                        "overflow-x": "auto",
                        "white-space": "nowrap",
                        "margin-top": "16px",
                    },
                    children=[
                        html.Img(
                            src=f"/assets/machine_temp_{i}.png",
                            style={
                                "width": "30%",
                                "margin-right": "10px",
                                "border-radius": "8px",
                            },
                        )
                        for i in range(1, 14)  # 13 graphs
                    ],
                ),
            ],
        ),
        # Section 6
        html.Div(
            style={
                "margin-top": "32px",
                "padding": "20px",
                "background-color": "white",
                "border-radius": "8px",
            },
            children=[
                html.H3(
                    "Top 10 High Risk Machines for Downtime (Excluding ‘Off’)",
                    style={"text-align": "center", "color": "#88B3E1"},
                ),
                html.Img(
                    src="/assets/top_risk_machines.png",
                    style={"width": "100%", "border-radius": "8px", "margin-top": "16px"},
                ),
            ],
        ),
        # Sections 7 to 12 (Similar Structure)
        *[
            html.Div(
                style={
                    "margin-top": "32px",
                    "padding": "20px",
                    "background-color": "white",
                    "border-radius": "8px",
                },
                children=[
                    html.H3(
                        section_title,
                        style={"text-align": "center", "color": "#88B3E1"},
                    ),
                    html.Div(
                        style={
                            "overflow-x": "auto",
                            "white-space": "nowrap",
                            "margin-top": "16px",
                        }
                        if is_carousel
                        else {},
                        children=[
                            html.Img(
                                src=img_src,
                                style={
                                    "width": "30%" if is_carousel else "100%",
                                    "margin-right": "10px" if is_carousel else "0",
                                    "border-radius": "8px",
                                },
                            )
                            for img_src in img_sources
                        ]
                        if is_carousel
                        else html.Img(
                            src=img_sources[0],
                            style={
                                "width": "100%",
                                "border-radius": "8px",
                                "margin-top": "16px",
                            },
                        ),
                    ),
                ],
            )
            for section_title, img_sources, is_carousel in [
                (
                    "Machine Efficiency by Region and Machine Type",
                    ["/assets/efficiency_region.png"],
                    False,
                ),
                (
                    "Factory Clustering by Energy and Efficiency",
                    ["/assets/factory_clustering.png"],
                    False,
                ),
                (
                    "Machine Temperature vs Energy Consumption",
                    ["/assets/temp_vs_energy.png"],
                    False,
                ),
                (
                    "Seasonal Trends in Energy Consumption",
                    ["/assets/seasonal_trends.png"],
                    False,
                ),
                (
                    "Average Efficiency Scores",
                    [f"/assets/efficiency_score_{i}.png" for i in range(1, 13)],
                    True,
                ),
                (
                    "Most Underperforming Machine in Each Factory",
                    ["/assets/underperforming_machines.png"],
                    False,
                ),
            ]
        ],
    ],
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)


