
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Qahwa Corner Sales",
    page_icon="☕",
    layout="wide"
)

st.title("Qahwa Corner - Sales Dashboard")
st.write("Coffee shop sales analysis from January to June 2026.")

df = pd.read_csv("cafe_sales.csv")
df["date"] = pd.to_datetime(df["date"])

branches = ["All Branches"] + sorted(df["branch"].unique().tolist())

selected_branch = st.selectbox(
    "Select Branch",
    branches
)

if selected_branch == "All Branches":
    filtered_df = df.copy()
else:
    filtered_df = df[df["branch"] == selected_branch]

total_revenue = filtered_df["total_sar"].sum()

st.metric(
    "Total Revenue",
    f"{total_revenue:,.0f} SAR"
)

st.subheader("Revenue by Product")

product_revenue = (
    filtered_df.groupby("product")["total_sar"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(product_revenue)

st.subheader("Sales Data")
st.dataframe(filtered_df, use_container_width=True)
