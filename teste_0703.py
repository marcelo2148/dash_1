import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Criando uma instância do app Dash
app = dash.Dash(__name__)

# Dados fictícios
df = pd.DataFrame({
    "Categoria": ["Sonic", "Mario", "Ursinhos", "Dinossauros"],
    "Valor": [1, 10, 3, 6]
})

# Criando um gráfico com Plotly
fig = px.bar(df, x="Categoria", y="Valor", title="Gráfico de Barras")

# Layout do app
app.layout = html.Div(children=[
    html.H1("Quantidade de brinquedos do Rafa"),
    dcc.Graph(id='grafico', figure=fig)
])

# Este é o servidor Flask que o Gunicorn precisa
server = app.server

# Executando o servidor (em modo desenvolvimento)
if __name__ == '__main__':
    app.run_server(debug=True)

