import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        .main{
            background-color:#f8fafc;
        }

        .stMetric{
            background:white;
            padding:15px;
            border-radius:15px;
            box-shadow:0 2px 8px rgba(0,0,0,0.1);
        }

        h1{
            color:#2563eb;
        }

        h2{
            color:#1e40af;
        }

        h3{
            color:#0f172a;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
