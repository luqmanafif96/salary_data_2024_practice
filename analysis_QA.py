import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Data
def load_data():
    file_path = "Salary Compare 2024 - QA_Test Engineer Dataset (1).csv"
    data = pd.read_csv(file_path, skiprows=2)
    data.columns = [ "Recruiter", "Role", "Seniority", "Salary Range", "Min Salary", "Max Salary"]
    # data = data.drop(columns=["Index"], errors="ignore")
    data["Min Salary"] = data["Min Salary"].str.replace(",", "").astype(int)
    data["Max Salary"] = data["Max Salary"].str.replace(",", "").astype(int)
    return data

data = load_data()

# Streamlit App Layout
st.title("QA Salary Analysis Dashboard")
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Choose Visualization", [
    "Bar Chart - Median Salary by Seniority",  
    "Bubble Chart", 
    "Box Plot", 
    "Grouped Bar Chart - Role and Recruiter"
])

if choice == "Bar Chart - Median Salary by Seniority":
    st.subheader("Median Salary by Seniority")

    grouped_data = data.groupby("Seniority")["Min Salary", "Max Salary"].median()
    grouped_data["Median Salary"] = grouped_data.mean(axis=1)
    grouped_data = grouped_data.reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        data=grouped_data, 
        x="Seniority", 
        y="Median Salary", 
        palette="Set2", 
        ax=ax
    )

    ax.set_title("Median Salary by Seniority")
    ax.set_ylabel("Median Salary (MYR)")
    ax.set_xlabel("Seniority")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    st.pyplot(fig)


elif choice == "Bubble Chart":
    st.subheader("Bubble Chart of Roles, Recruiters, and Salaries")
    data["Bubble Size"] = (data["Max Salary"] - data["Min Salary"]) / 1000
    fig = px.scatter(
        data,
        x="Role",
        y="Max Salary",
        size="Bubble Size",
        color="Recruiter",
        title="Bubble Chart of Roles and Salary Range",
        labels={"Max Salary": "Salary (MYR)"}
    )
    st.plotly_chart(fig)

elif choice == "Box Plot":
    st.subheader("Salary Distribution by Seniority Level")
    salary_data = pd.melt(
        data,
        id_vars=["Seniority"],
        value_vars=["Min Salary", "Max Salary"],
        var_name="Salary Type",
        value_name="Salary",
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=salary_data, x="Seniority", y="Salary", palette="pastel", ax=ax)
    ax.set_title("Salary Distribution by Seniority Level")
    ax.set_ylabel("Salary (MYR)")
    ax.set_xlabel("Seniority Level")
    st.pyplot(fig)

elif choice == "Grouped Bar Chart - Role and Recruiter":
    st.subheader("Median Salary by Role and Recruiter")

    grouped_data = (
        data.groupby(["Role", "Recruiter"])[["Min Salary", "Max Salary"]]
        .median()
        .mean(axis=1)  # Calculate the median salary and combine Min/Max
        .reset_index(name="Median Salary")
    )

    fig, ax = plt.subplots(figsize=(14, 8))
    sns.barplot(
        data=grouped_data,
        x="Role",
        y="Median Salary",
        hue="Recruiter",
        palette="viridis",
        ax=ax,
    )

    ax.set_title("Median Salary by Role and Recruiter")
    ax.set_ylabel("Median Salary (MYR)")
    ax.set_xlabel("Role")
    plt.xticks(rotation=45, ha="right")
    ax.legend(title="Recruiter", loc="upper right")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    st.pyplot(fig)
