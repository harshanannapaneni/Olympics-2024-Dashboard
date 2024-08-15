import pandas as pd
from dash import Dash, dcc, html, callback, Input, Output
from plotly import express as px

# Load the data
athletes = pd.read_csv("./src/athletes.csv")

# Calculate the number of athletes by country
athlete_count_by_country = athletes['country'].value_counts().reset_index()
athlete_count_by_country.columns = ['country', 'Athlete Count']
# athlete_count_by_country = athlete_count_by_country[athlete_count_by_country['Athlete Count']>100]
# Initialize Dash app
app = Dash(__name__)

# Layout of the app with custom styling
app.layout = html.Div(
    style={'backgroundColor': '#282a36', 'color': '#f8f8f2', 'height': '100vh', 'padding': '20px'},
    children=[
        html.H1(
            children='Athlete Participation by Country',
            style={'color': '#50fa7b'}  # Green color for the header
        ),

        dcc.Graph(
            id='bar-chart',
            figure=px.bar(
                athlete_count_by_country,
                x='country',
                y='Athlete Count',
                title='Number of Athletes by Country',
                color_discrete_sequence=['#8be9fd', '#ffb86c', '#ff79c6', '#bd93f9', '#ff5555', '#f1fa8c'],
                template='plotly_dark'  # Use plotly's dark template
            ),
            config={'displayModeBar': False},  # Optionally hide the mode bar
            style={
                'backgroundColor': '#282a36',  # Dark background for the chart area
                'padding': '10px',
                'borderRadius': '10px',
                'boxShadow': '0px 0px 10px #44475a'
            }
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
