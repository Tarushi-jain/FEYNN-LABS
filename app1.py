import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import optimize_price
import optimize_quantity
import dash_daq as daq

group_colors = {"control": "pink", "reference": "purple"}

# Load the data
df = pd.read_csv('price.csv')
df.head()
df.shape

# App layout
def create_banner():
    st.markdown(
        """
        # PRICE OPTIMIZATION
        """
    )
    # st.title("PRICE OPTIMIZATION")
    # st.image("./assets/dash-logo-new.png")

def main():
    # Create the banner
    create_banner()

    # Input widgets
    st.sidebar.markdown("## OPTIMIZE")
    selected_var_opt = st.sidebar.radio(
        "Select variable to optimize:",
        ["Price", "Quantity"],
        index=0
    )

    st.sidebar.markdown("## OPTIMIZATION RANGE")
    my_range_slider = st.sidebar.slider(
        "Select range for optimization:",
        min_value=0,
        max_value=500,
        value=(200, 400),
        step=1,
        format="%d"
    )

    st.sidebar.markdown("## FIXED COST")
    selected_cost_opt = st.sidebar.number_input(
        "Enter fixed cost:",
        min_value=0,
        max_value=10000,
        value=100
    )

    # Output section
    st.subheader("SIMULATED RESULT")

    try:
        if isinstance(selected_var_opt, str):
            selected_var_opt = selected_var_opt.lower()

            if selected_var_opt == 'price':
                res, fig_PriceVsRevenue, fig_PriceVsQuantity, opt_Price, opt_Revenue = optimize_price.fun_optimize(
                    selected_var_opt, my_range_slider, selected_cost_opt, df)
                # res = np.round(res.sort_values('Revenue', ascending=True), decimals=2)

                if opt_Revenue > 0:
                    st.subheader(f"The maximum revenue of {opt_Revenue} is achieved by optimizing {selected_var_opt.lower()} of {opt_Price}, fixed cost of {selected_cost_opt} and optimization was carried for {selected_var_opt.lower()} range between {my_range_slider}")
                else:
                    st.subheader(f"For the fixed cost of {selected_cost_opt} and {selected_var_opt.lower()} range between {my_range_slider}, you will incur a loss in revenue")

                st.dataframe(res.to_dict('records'))

                # Display figures
                if selected_var_opt.lower() == 'price':
                    st.subheader("PRICE VS QUANTITY")
                    st.plotly_chart(fig_PriceVsQuantity)

                st.subheader("MAXIMIZING REVENUE")
                st.plotly_chart(fig_PriceVsRevenue)

            else:
                res, fig_QuantityVsRevenue, fig_PriceVsQuantity, opt_Quantity, opt_Revenue = optimize_quantity.fun_optimiz(
                    selected_var_opt, my_range_slider, selected_cost_opt, df)

            res = np.round(res.sort_values('Revenue', ascending=True), decimals=2)

            # st.dataframe(res)

            if opt_Revenue > 0:
                st.subheader("The maximum revenue is achieved by optimizing {} of {}, fixed cost of {}, and optimization was carried for {} range between {}".format(
                    selected_var_opt, opt_Revenue, selected_cost_opt, selected_var_opt, my_range_slider))
            else:
                st.subheader("For the fixed cost of {} and {} range between {}, you will incur a loss in revenue".format(
                    selected_cost_opt, selected_var_opt, my_range_slider))

        else:
            st.error("Selected variable to optimize must be a string.")

    except Exception as e:
        st.error('Something went wrong with interaction logic:')


if __name__ == "__main__":
    main()
