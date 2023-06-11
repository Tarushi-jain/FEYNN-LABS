import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
import plotly.express as px
import plotly.graph_objects as go
# Load the data
df = pd.read_csv('price.csv')
def fun_optimize(var_opt, var_range, var_cost, df):
    fig_PriceVsQuantity = px.scatter(
        df, x="Price", y="Quantity", color="Year", trendline="ols")
    # fit OLS model
    model = ols("Quantity ~ Price", data=df).fit()
    Price = list(range(var_range[0], var_range[1], 10))
    cost = int(var_cost)
    quantity = []
    Revenue = []
    for i in Price:
        demand = model.params[0] + (model.params[1] * i)
        quantity.append(demand)
        Revenue.append((i-cost) * demand)
    profit = pd.DataFrame(
        {"Price": Price, "Revenue": Revenue, "Quantity": quantity})
    max_val = profit.loc[(profit['Revenue'] == profit['Revenue'].max())]
    fig_PriceVsRevenue = go.Figure()
    fig_PriceVsRevenue.add_trace(go.Scatter(
        x=profit['Price'], y=profit['Revenue']))
    fig_PriceVsRevenue.add_annotation(x=int(max_val['Price']), y=int(max_val['Revenue']),text="Maximum Revenue",
                                      showarrow=True,arrowhead=1)
    fig_PriceVsRevenue.update_layout( showlegend=False, xaxis_title="Price",yaxis_title="Revenue")
    fig_PriceVsRevenue.add_vline(x=int(max_val['Price']), line_width=1.5, line_dash="dash",line_color="blue", opacity=0.25)
    return [profit, fig_PriceVsRevenue, fig_PriceVsQuantity, round(max_val['Price'].values[0],2),round(max_val['Revenue'].values[0],3)]




    