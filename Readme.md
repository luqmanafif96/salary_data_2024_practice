# QA Salary Analysis 

This project is a Streamlit-based interactive dashboard designed for analyzing QA-related salaries. The dataset includes information about QA roles, recruiters, seniority levels, and salary ranges, making it an insightful tool for job market analysis. all data can be refer [google sheet](https://docs.google.com/spreadsheets/d/1aqhgA6boLvLuPZOBXoeM-T1FJDyxWVFwsK3xvitt9o8/edit?usp=sharing)

## Features

### Visualizations 
1. **Bar Chart - Median Salary by Seniority**
   - Displays the median salary based on seniority levels.
   - Uses differentiated colors for each seniority group.

2. **Heatmap of Average Salary**
   - Shows average salaries for roles and recruiters.
   - Helps identify patterns or discrepancies in pay.

3. **Bubble Chart**
   - Visualizes roles and salaries with bubble sizes indicating salary ranges.
   - Differentiates recruiters with colors.

4. **Box Plot**
   - Analyzes salary distribution across seniority levels.
   - Displays outliers for better insight.

5. **Grouped Bar Chart - Role and Recruiter**
   - Compares median salaries for similar roles across recruiters.
   - Useful for salary benchmarking.

### Data Handling
- Reads a CSV file with salary data.
- Cleans and processes salary values for analysis.
- Calculates median and average salary metrics.

## Prerequisites

- Python 3.7 or higher
- Required Python packages:
  - `streamlit`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `plotly`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/luqmanafif96/salary_data_2024_practice.git
   cd salary_data_2024_practice
   ```

2. Install the required packages:
   ```bash
   pip install streamlit pandas matplotlib seaborn plotly
   ```

3. Place the salary data CSV file (e.g., `Salary Compare 2024 - QA_Test Engineer Dataset (1).csv`) in the project directory.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run <script-name>.py
   ```

2. Access the dashboard in your web browser at:
   `http://localhost:8501`

3. Use the sidebar navigation to select different visualizations.

## Dataset

The dataset should include the following columns:
- `Recruiter`: The recruitment agency.
- `Role`: Job role/title.
- `Seniority`: The level of seniority (e.g., Junior, Senior, Specialist).
- `Min Salary`: Minimum salary offered (integer without commas).
- `Max Salary`: Maximum salary offered (integer without commas).

Example Dataset Structure:
| Recruiter      | Role            | Seniority   | Min Salary | Max Salary |
|----------------|-----------------|-------------|------------|------------|
| Hays           | Test Analyst    | Junior      | 60000      | 80000      |
| Michael Page   | QA Engineer     | Senior      | 85000      | 100000     |

## Customization

1. **Data File Path**:
   Update the `file_path` in the `load_data` function to point to the CSV file.

2. **Visualization Enhancements**:
   Modify plots and layouts by updating the corresponding Streamlit sections in the script.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch.
5. Create a pull request.

## Screenshot 


https://github.com/user-attachments/assets/d451cca7-ca40-43e6-9565-2d9dec51d757


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the chatgpt and recruiter share the report salary for providing an enriched QA dataset for this analysis.

