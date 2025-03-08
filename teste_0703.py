import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Criando uma instância do app Dash
app = dash.Dash(__name__)

# Dados fictícios
df = pd.DataFrame({
    "Categoria": ["A", "B", "C", "D"],
    "Valor": [10, 20, 30, 40]
})

# Criando um gráfico com Plotly
fig = px.bar(df, x="Categoria", y="Valor", title="Gráfico de Barras")

# Layout do app
app.layout = html.Div(children=[
    html.H1("Dashboard Simples"),
    dcc.Graph(id='grafico', figure=fig)
])

# Executando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
