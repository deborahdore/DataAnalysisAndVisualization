# DataAnalysisAndVisualization

Repo for the course of Data Analysis and Visualization at CentraleDigitalLab@Nice starting from February 2025.

## Useful pointers

- [The Data Visualization Catalogue](https://datavizcatalogue.com)
- [Python Graph Gallery](https://python-graph-gallery.com)
- [Getting Started with Plotly](https://plotly.com/python/getting-started/)
- [Git CheatSheet](git-cheat-sheet-education.pdf)

## Course

| **Date**   | **Topic**                                                  | **Slides**                                                                                                                                                                             | **Code & Data**                                                                                                                                                                                                             |
|------------|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 14/02/2025 | Introduction to Data Analysis <br/> Introduction to Python | [Part 1 - Introduction to Data Analysis](slides/1%20-%20Introduction%20to%20Data%20Analysis.pdf)<br/> [Part 2 - Introduction to Python](slides/2%20-%20Introduction%20to%20Python.pdf) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deborahdore/DataAnalysisAndVisualization/blob/main/notebook/Notebook_Introduction_to_python.ipynb)    |
| 14/02/2025 | Exploratory Data Analysis                                  | [3 - EDA.pdf](slides/3%20-%20EDA.pdf)                                                                                                                                                  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deborahdore/DataAnalysisAndVisualization/blob/main/notebook/Notebook_EDA.ipynb)                       |
| 18/02/2025 | Missing Data                                               | [4 - Missing Values.pdf](slides/4%20-%20Missing%20Values.pdf)                                                                                                                          | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deborahdore/DataAnalysisAndVisualization/blob/main/notebook/Notebook_Missing_Data.ipynb)              |
| 18/02/2025 | Outliers and Data Scaling                                  | [5 - Outliers and Data Scaling.pdf](slides/5%20-%20Outliers%20and%20Data%20Scaling.pdf)                                                                                                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deborahdore/DataAnalysisAndVisualization/blob/main/notebook/Notebook_Outliers_and_Data_Scaling.ipynb) |
| 21/02/2025 | Imbalanced Datasets & Data Augmentation                    | [6 - Imbalanced Datasets & Data Augmentation.pdf](slides/6%20-%20Imbalanced%20Datasets%20%26%20Data%20Augmentation.pdf)                                                                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deborahdore/DataAnalysisAndVisualization/blob/main/notebook/Notebook_Imbalanced_Dataset.ipynb)        |
| 21/02/2025 | Text Data Encoding                                         | [7 - Text Data Encoding.pdf](slides/7%20-%20Text%20Data%20Encoding.pdf)                                                                                                                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deborahdore/DataAnalysisAndVisualization/blob/main/notebook/Notebook_Text_Data_Encoding.ipynb)        |
| 21/02/2025 | Dimensionality Reduction Techniques                        | [8 - Dimensionality Reduction.pdf](slides/8%20-%20Dimensionality%20Reduction.pdf)                                                                                                      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deborahdore/DataAnalysisAndVisualization/blob/main/notebook/Notebook_Dimensionality_reduction.ipynb)  |
| 21/02/2025 | Visualizations                                             | [9 - Visualizations.pdf](slides/9%20-%20Visualizations.pdf)                                                                                                                            |                                                                                                                                                                                                                             |
| 21/02/2025 | Project Work                                               | --                                                                                                                                                                                     | [plotly-example](plotly-example)                                                                                                                                                                                            |
| 26/02/2025 | Project Work                                               | --                                                                                                                                                                                     |                                                                                                                                                                                                                             |
| 4/03/2025  | Project Work <br/> & Project Presentation                  | --                                                                                                                                                                                     |                                                                                                                                                                                                                             |

## **Project Outline**

Form groups of 2 students each.

### **1. Dataset Selection and Understanding**

- Choose a dataset from **[Kaggle](https://www.kaggle.com/datasets)** that interests you.
- The dataset should:
    - Have **diverse features** (numerical & categorical).
    - Be **large enough** for meaningful analysis.
    - Have a **real-world application** (e.g., health, environment, business, sports, etc.).

✅ **Examples of datasets:**

- **Health**: Diabetes trends, heart disease predictors, mental health surveys.
- **Finance**: Stock prices, cryptocurrency trends, loan default prediction.
- **Sports**: FIFA player stats, Olympic medalists, NBA game results.
- **Environment**: Air quality, climate change, forest fires.
- **E-commerce**: Customer purchases, product reviews, sales trends.

### **2. Data Cleaning**

- Handle **missing values** using imputation or removal techniques.
- Address **outliers** using statistical methods (e.g., Z-score, IQR).
- Convert **categorical variables** into numerical formats if needed.
- Normalize/standardize numerical data where necessary.

### **3. Text Data Encoding (If applicable)**

- Encode categorical data (e.g., one-hot encoding for product categories).

### **4. Balance the dataset (If needed)**

- Perform Oversampling or Undersampling if needed.

### **5. Exploratory Data Analysis & Hypothesis Generation**

- Identify key **patterns and trends** in the dataset.
- Formulate a **hypothesis** (e.g., "Higher customer ratings lead to more sales").
- Each student should explore at least 2 different aspect of the hypothesis (e.g. "Visualize ratings though the seasons" and "
  explore the age of the customer that gave the higher ratings").
- Create **basic visualizations** to explore relationships:<br>
  ✅ Correlation heatmaps  
  ✅ Histograms & box plots for distributions  
  ✅ Scatter plots for relationships
- Perform Dimensionality Reduction to visualize your data if needed.

### **6. Data Visualization & Dash App Development**

Build an **interactive Plotly Dash application** that: <br>
✅ Displays **key statistics** in an easy-to-read format.  
✅ Includes **multiple visualizations** (e.g., scatter plots, bar charts, time series).  
✅ Allows **user interaction** (e.g., dropdowns, filters, sliders).

### **7. Insights & Recommendations**

- Summarize key **findings and trends** from the dataset.
- Provide **data-driven recommendations** based on analysis.
- Discuss **challenges faced** and potential future improvements.
