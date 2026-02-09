# importing streamlit
import streamlit as st

# Set web application title and description
st.title("Project Genesis")
st.write(
    "This is a web application built using Streamlit"
)
# sample data as display
import pandas as pd

martket_data = {
    "Company": ["Apple", "Google", "Microsoft", "Amazon"],
    "Stock Price": [150, 2800, 300, 3500],
    "Market Cap (Billion USD)": [2500, 1800, 2200, 1700],
}

df = pd.DataFrame(martket_data)

# Display data as a table
st.header("Market Data Table")
st.subheader("Stock Prices and Market Capitalization Table")
st.dataframe(df)

# Display data as a line chart
st.header("Market Data Line Chart")
st.subheader("Stock Prices Line Chart")
st.line_chart(df.set_index("Company")["Stock Price"])   

# Charts
st.header("Market Data Visualization")
st.subheader("Stock Prices")
st.bar_chart(df.set_index("Company")["Stock Price"])

# markdown in streamlit
st.header("Markdown Example")
st.markdown("""
## Data Description

### Input Files

| File | Description | Size | Records |
|------|-------------|------|---------|
| `Train.csv` | Historical customer-product-week data | 275 MB | ~5M rows |
| `Test.csv` | Test set for predictions | 27 MB | ~500K rows |
| `SampleSubmission.csv` | Submission format | 7 MB | ~500K rows |

### Key Columns

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | ID | Unique customer identifier |
| `product_unit_variant_id` | ID | Unique product variant identifier |
| `week_start` | Date | Week start date |
| `purchased_this_week` | Binary | Purchase indicator (0/1) |
| `qty_this_week` | Float | Quantity purchased |
| `customer_category` | Category | Customer segment |
| `customer_status` | Category | Customer status |
| `grade_name` | Category | Product grade |
| `unit_name` | Category | Product unit type |

### Targets

| Target | Type | Description |
|--------|------|-------------|
| `Target_purchase_next_1w` | Binary | Will purchase in next 1 week? |
| `Target_purchase_next_2w` | Binary | Will purchase in next 2 weeks? |
| `Target_qty_next_1w` | Float | Quantity in next 1 week |
| `Target_qty_next_2w` | Float | Quantity in next 2 weeks |

---
""")

# metrics in streamlit
st.header("Metrics Example")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", "1,000,000", "5% increase")
col2.metric("Total Products", "10,000", "-2% decrease")
col3.metric("Total Purchases", "500,000", "10% increase")   

# Streamlit Basics
st.header("Streamlit Basics")
st.markdown("""
## Text and Formatting
- Use `st.write()` for simple text output.
- Use `st.markdown()` for formatted text and markdown support.
## Data Display
- Use `st.dataframe()` to display interactive tables.
- Use `st.table()` for static tables.
            
## Charts and Visualizations
- Use `st.line_chart()`, `st.bar_chart()`, and `st.area_chart()` for quick visualizations.
- For more complex charts, use libraries like Matplotlib or Seaborn and display with `st.pyplot()`.
## Layout and Interactivity
- Use `st.columns()` to create multi-column layouts.
- Use `st.expander()` to hide/show content.
- Use `st.form()` to create interactive forms for user input.
""")