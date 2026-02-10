# importing streamlit
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def main():
    st.title("Loan Default Prediction App")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["EDA", "ML Modeling"])

    if page == "EDA":
        show_eda_page()
    elif page == "ML Modeling":
        show_ml_modeling_page()

def show_eda_page():
    st.header("Exploratory Data Analysis")

    # Load dataset
    data_url = "https://raw.githubusercontent.com/josephgitau/project_defcone/refs/heads/main/Data/Loan/Loan_default.csv"
    @st.cache_data
    def load_data():
        return pd.read_csv(data_url)

    df = load_data()

    # Display dataset
    st.subheader("Dataset")
    st.write(df.head())

    # Display basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Visualizations
    st.subheader("Visualizations")

    # Correlation heatmap
    st.write("Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Distribution of target variable
    if 'Loan_Default' in df.columns:
        st.write("Distribution of Loan Default")
        fig, ax = plt.subplots()
        sns.countplot(x='Loan_Default', data=df, ax=ax)
        st.pyplot(fig)

def show_ml_modeling_page():
    st.header("Machine Learning Modeling")

    # Load dataset
    data_url = "https://raw.githubusercontent.com/josephgitau/project_defcone/refs/heads/main/Data/Loan/Loan_default.csv"
    @st.cache_data
    def load_data():
        return pd.read_csv(data_url)

    df = load_data()

    # Check if target column exists
    if 'Loan_Default' not in df.columns:
        st.error("The dataset does not contain the 'Loan_Default' column.")
        return

    # Split data into features and target
    X = df.drop(columns=['Loan_Default'])
    y = df['Loan_Default']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Display results
    st.subheader("Model Performance")
    st.write("Accuracy:", accuracy_score(y_test, y_pred))

    st.subheader("Classification Report")
    st.text(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()