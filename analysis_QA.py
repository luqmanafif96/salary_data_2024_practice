import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Data
def load_data():
    file_path = "Salary Compare 2024 - QA_Test Engineer Dataset (1).csv"
    # try the data 
    try :
        data = pd.read_csv(file_path, encoding="utf-8")
        st.success("File loaded successfully!")
    except FileNotFoundError:
        st.error(f"File not found. Make sure it is in the correct location: {file_path}")
    except Exception as e:
        st.error(f"An error occurred while loading the file: {e}")

    # data = pd.read_csv(file_path, skiprows=2)

    data.columns = [ "Recruiter", "Role", "Seniority", "Salary Range", "Min Salary", "Max Salary"]
    data["Min Salary"] = data["Min Salary"].str.replace(",", "").astype(int)
    data["Max Salary"] = data["Max Salary"].str.replace(",", "").astype(int)
    return data

data = load_data()

# Streamlit App Layout
st.title("QA Salary Analysis Dashboard")
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Choose Visualization", ["Heatmap", "Bubble Chart", "Box Plot"])

# if choice == "Bar Chart":
#     st.subheader("Salary Range by Role")
#     fig, ax = plt.subplots(figsize=(10, 6))
#     x = range(len(data["Role"]))
#     ax.bar(x, data["Min Salary"], width=0.4, label="Min Salary")
#     ax.bar(x, data["Max Salary"], width=0.4, label="Max Salary", bottom=data["Min Salary"])
#     ax.set_xticks(x)
#     ax.set_xticklabels(data["Role"], rotation=45, ha="right")
#     ax.set_title("Salary Range by Role")
#     ax.set_ylabel("Salary (MYR)")
#     ax.legend()
#     st.pyplot(fig)

# elif choice == "Heatmap":
if choice == "Heatmap":
    st.subheader("Heatmap of Average Salary by Recruiter and Role")
    data["Avg Salary"] = (data["Min Salary"] + data["Max Salary"]) / 2

    # Handle duplicates by aggregating (e.g., averaging) the duplicate combinations
    heatmap_data = (
        data.groupby(["Role", "Recruiter"])["Avg Salary"]
        .mean()
        .unstack(fill_value=0)  # Converts to pivot table with no missing values
    )
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="coolwarm", ax=ax)
    ax.set_title("Average Salary by Recruiter and Role")
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
