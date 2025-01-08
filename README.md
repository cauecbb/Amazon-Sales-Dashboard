# Dashboard - Amazon Report

This project is a simple dashboard created with **Streamlit** and **Plotly Express** to visualize and analyze data from an Amazon Sales Report.

## Features
- Displays a table showing the count of orders per status.
- Visualizes the order counts with an interactive bar chart.

## Requirements
To run this project, you need:
- Python 3.7 or higher
- The following Python libraries:
  - `streamlit`
  - `pandas`
  - `plotly`

## Installation
1. Clone this repository or download the code.
2. Install the required libraries:
   ```bash
   pip install streamlit pandas plotly
   ```
3. Place the `AmazonSaleReport.csv` file inside a folder named `data` in the project directory.

## Usage
Run the Streamlit app using the command:
```bash
streamlit run app.py
```
Replace `app.py` with the name of the file containing the code above.

## File Structure
```
project-folder/
|-- data/
|   |-- AmazonSaleReport.csv
|-- app.py
```

## About the Code
### Input Data
The dashboard uses a CSV file named `AmazonSaleReport.csv`, which contains sales data. The CSV must include a column named `Status` to categorize order statuses.

### Key Components
1. **Data Loading**: The app reads the CSV file using `pandas`.
   ```python
   df = pd.read_csv('data/AmazonSaleReport.csv')
   ```

2. **Order Status Count**: Calculates the number of orders per status and displays it as a table.
   ```python
   status_count = df['Status'].value_counts().reset_index()
   status_count.columns = ['Status', 'Quantity']
   ```

3. **Interactive Bar Chart**: Creates a bar chart to visualize the order status counts using Plotly Express.
   ```python
   fig = px.bar(status_count, x='Status', y='Quantity', title='Orders per Status')
   st.plotly_chart(fig)
   ```

### User Interface
- The app includes a title: `Dashboard - Amazon Report`.
- It displays the table and chart in an easy-to-read layout using Streamlit.

## Example Output
1. **Table of Order Counts**:
   | Status     | Quantity |
   |------------|----------|
   | Delivered  | 500      |
   | Pending    | 200      |
   | Canceled   | 50       |

2. **Bar Chart**:
   - A bar chart visualizing the number of orders for each status.

## Thanks!

