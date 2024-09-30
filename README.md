### ReadMe Document for Self-Organizing Map (SOM) Project

#### About the Dataset
This dataset contains information about various items and their respective categories. The dataset includes the following columns:

1. Item Code: A unique identifier for each item (numeric or alphanumeric code).
2. Item Name: The name of the item (string format).
3. Category Code: A numerical code representing the category that the item belongs to.
4. Category Name: The name of the category (string format), providing a descriptive label for the category.

The goal of this project is to use a Self-Organizing Map (SOM) to cluster these items based on their `Item Name` and `Category Name`, after converting them into numeric values.

#### Software Requirements
- Python 3.x
- Required Python libraries: `numpy`, `pandas`, `matplotlib`, `sklearn`, and `minisom`

#### Hardware Requirements
- A computer with at least 4GB of RAM (basic system requirements to run Python).

#### How to Run
1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries by running:
   ```bash
   pip install numpy pandas matplotlib sklearn minisom
