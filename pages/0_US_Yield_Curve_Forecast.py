import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# import yaml


# Create 3D plot
def create_3d_plot(df, start_year, end_year):

    df = df[(df["Date"] >= str(start_year)) & (df["Date"] <= str(end_year))]
    df = df.pivot(index="Date", columns="MaturityYear", values="YieldValue")

    zlist = df.values
    xlist = df.columns
    ylist = df.index

    opacity = 0.7

    trace1 = dict(
        type="surface",
        x=xlist,
        y=ylist,
        z=zlist,
        hoverinfo="x+y+z",
        hovertemplate="Maturity Year: %{x:.1f}<br>Date: %{y}<br>Yield: %{z:.2f}%<br><extra></extra>",
        lighting={
            "ambient": 0.95,
            "diffuse": 0.99,
            "fresnel": 0.01,
            "roughness": 0.01,
            "specular": 0.01,
        },
        colorscale=[
            [0, "rgb(230,245,254)"],
            [0.4, "rgb(123,171,203)"],
            [0.8, "rgb(40,119,174)"],
            [1, "rgb(37,61,81)"],
        ],  # customized
        opacity=opacity,
        showscale=False,
        scene="scene",
    )

    data = [trace1]

    layout_3d = dict(
        # autosize=True,
        autosize=False,
        width=1000,
        height=600,
        font=dict(
            size=12,
            color="#CCCCCC",
        ),
        margin=dict(
            t=5,
            l=1,
            b=5,
            r=5,
        ),
        showlegend=False,
        hovermode="closest",
        scene=dict(
            aspectmode="manual",
            aspectratio=dict(x=2, y=5, z=1.5),
            camera=dict(
                up=dict(x=0, y=0, z=1),
                center=dict(x=0.5, y=0.5, z=-0.0),
                eye=dict(x=4.24358, y=2.22741, z=0.847),
                # eye=dict(x=2.5, y=2.5, z=0.5)
            ),
            xaxis={
                "showgrid": True,
                "title": "Maturity Year",
                "type": "category",
                "zeroline": False,
                "categoryorder": "array",
                "categoryarray": list(reversed(xlist)),
            },
            yaxis={
                "showgrid": True,
                "title": "Date",
                "type": "date",
                "zeroline": False,
            },
            zaxis={
                "title": "Yield (%)",
            },
        ),
    )

    figure = go.Figure(data=data, layout=layout_3d)
    return figure


st.set_page_config(page_title="US Yield Curve Forecast", page_icon="")

df = pd.read_csv("data/us_yields.csv")

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df.sort_values(by=["Date"], inplace=True)

# Add a slider for selecting the date range
year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=df["Date"].min().year,
    max_value=df["Date"].max().year,
    value=(df["Date"].min().year, df["Date"].max().year),
    step=1,
)


# Create the 3D plot based on the selected date range
fig = create_3d_plot(df, year_range[0], year_range[1])

# Show the 3D plot using st.plotly_chart
st.plotly_chart(fig)
