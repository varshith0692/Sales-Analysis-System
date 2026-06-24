import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Sales Analysis System",
    layout="wide"
)

# Reduce padding
st.markdown("""
<style>
.block-container{
    padding-top:1.2rem;
    padding-bottom:1rem;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Sales Analysis System")

# Upload CSV File
uploaded_file = st.file_uploader(
    "Upload Sales CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV safely
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    # Dataset Preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Dataset Information
    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Records", len(df))

    # Convert column names to lowercase for matching
    cols = [c.lower() for c in df.columns]

    # Sales Metric
    with col2:
        if 'sales' in cols:
            sales_col = df.columns[cols.index('sales')]
            sales = pd.to_numeric(df[sales_col], errors='coerce')

            st.metric(
                "Total Sales",
                f"{sales.sum():,.2f}"
            )

    # Profit Metric
    with col3:
        if 'profit' in cols:
            profit_col = df.columns[cols.index('profit')]
            profit = pd.to_numeric(df[profit_col], errors='coerce')

            st.metric(
                "Total Profit",
                f"{profit.sum():,.2f}"
            )

    # Dataset Details
    st.subheader("Dataset Details")

    st.write("Shape:", df.shape)
    st.write("Column Names:")
    st.write(df.columns.tolist())

    st.write("Data Types:")
    st.dataframe(df.dtypes.astype(str))

    # Summary Statistics
    st.subheader("Summary Statistics")
    st.dataframe(df.describe(include='all'))

    # Full Dataset
    st.subheader("Sales Data")

    rows_to_show = st.slider(
        "Number of rows to display",
        min_value=10,
        max_value=min(len(df), 1000),
        value=min(100, len(df))
    )

    st.dataframe(df.head(rows_to_show))

else:
    st.info("Please upload a CSV file.")