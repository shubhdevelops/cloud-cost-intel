import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Cloud Cost Intelligence Platform",
    layout="wide"
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------
df = pd.read_csv("../data/raw/gcp_final_approved_dataset.csv")

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("Cloud Cost Intelligence Platform")

st.markdown(
    "Cloud spend analytics, utilization monitoring, and cost optimization insights."
)

st.divider()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------
total_spend = df["Total Cost (INR)"].sum()
total_services = df["Service Name"].nunique()
total_regions = df["Region/Zone"].nunique()
total_records = len(df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Spend (INR)", f"{total_spend:,.0f}")

with col2:
    st.metric("Services", total_services)

with col3:
    st.metric("Regions", total_regions)

with col4:
    st.metric("Records", total_records)

st.divider()

# --------------------------------------------------
# Top Services by Cloud Spend
# --------------------------------------------------
service_cost = (
    df.groupby("Service Name")["Total Cost (INR)"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(
    service_cost,
    x="Service Name",
    y="Total Cost (INR)",
    title="Top Services by Cloud Spend"
)

st.plotly_chart(fig1, use_container_width=True)

# --------------------------------------------------
# Cloud Spend by Region
# --------------------------------------------------
region_cost = (
    df.groupby("Region/Zone")["Total Cost (INR)"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    region_cost,
    names="Region/Zone",
    values="Total Cost (INR)",
    title="Cloud Spend by Region"
)

st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# Service CPU Utilization Analysis
# --------------------------------------------------
cpu_df = (
    df.groupby("Service Name")["CPU Utilization (%)"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig3 = px.bar(
    cpu_df,
    x="Service Name",
    y="CPU Utilization (%)",
    title="Service CPU Utilization Analysis"
)

st.plotly_chart(fig3, use_container_width=True)

# --------------------------------------------------
# Service Memory Utilization Analysis
# --------------------------------------------------
memory_df = (
    df.groupby("Service Name")["Memory Utilization (%)"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig4 = px.bar(
    memory_df,
    x="Service Name",
    y="Memory Utilization (%)",
    title="Service Memory Utilization Analysis"
)

st.plotly_chart(fig4, use_container_width=True)

# --------------------------------------------------
# Cost Efficiency Analysis
# --------------------------------------------------
efficiency_df = (
    df.groupby("Service Name")
    .agg({
        "CPU Utilization (%)": "mean",
        "Total Cost (INR)": "sum"
    })
    .reset_index()
)

fig5 = px.scatter(
    efficiency_df,
    x="CPU Utilization (%)",
    y="Total Cost (INR)",
    size="Total Cost (INR)",
    color="Service Name",
    hover_name="Service Name",
    title="Cost Efficiency Analysis"
)

st.plotly_chart(fig5, use_container_width=True)

# --------------------------------------------------
# Cost Optimization Analysis
# --------------------------------------------------
st.subheader("Cost Optimization Analysis")

optimization_df = (
    df.groupby("Service Name")
    .agg({
        "CPU Utilization (%)": "mean",
        "Memory Utilization (%)": "mean",
        "Total Cost (INR)": "sum"
    })
    .reset_index()
)

optimization_df = optimization_df.rename(columns={
    "CPU Utilization (%)": "Avg CPU Utilization",
    "Memory Utilization (%)": "Avg Memory Utilization",
    "Total Cost (INR)": "Total Cost (INR)"
})

optimization_df = optimization_df.sort_values(
    by="Total Cost (INR)",
    ascending=False
)

st.dataframe(
    optimization_df,
    use_container_width=True
)
