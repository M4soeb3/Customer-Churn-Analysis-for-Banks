import dash
from dash import dcc, html
import plotly.express as px

app = dash.Dash(__name__)

# Churn Distribution Pie Chart
churn_dist = data['Exited'].value_counts()
fig_churn = px.pie(
    values=churn_dist, 
    names=["Retained", "Churned"], 
    title="Customer Churn Distribution"
)

# Feature Importance Bar Chart
fig_importance = px.bar(
    x=[features[i] for i in indices],
    y=importances[indices],
    labels={"x": "Feature", "y": "Importance"},
    title="Feature Importance in Churn Prediction"
)

app.layout = html.Div([
    html.H1("Customer Churn Analysis Dashboard"),
    
    html.Div([
        html.H3("Churn Distribution"),
        dcc.Graph(figure=fig_churn)
    ]),
    
    html.Div([
        html.H3("Feature Importance"),
        dcc.Graph(figure=fig_importance)
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
