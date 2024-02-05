import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Home",
        page_icon="",
    )

    st.write("# Yield Curve Forecast on Streamlit")
    hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
    st.markdown(hide_default_format, unsafe_allow_html=True)
    st.markdown("*Michael C, 2024-02-05*")
    st.markdown(
        """
        **Streamlit:**

        Explore the capabilities of Streamlit, a platform designed for streamlined data exploration. This interface offers a balance of simplicity and sophistication, providing a professional experience accessible to users of various technical backgrounds.

        **Yield Curve Forecasting:**

        Delve into the world of Yield Curve Forecasting, focusing on the U.S. Yield Curve. This crucial economic indicator offers insights into future market trends. The user-friendly interface facilitates easy navigation and forecasting, making financial analysis an enlightening experience for all users. Welcome to a space where professionalism and approachable finance intersect.

    
    
    """
    )


if __name__ == "__main__":


    run()
