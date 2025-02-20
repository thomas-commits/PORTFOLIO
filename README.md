# Portfolio

## Overview

This portfolio consists of two primary tasks:

- **Task 1**: Solving optimization problems using Genetic Algorithms (GA). This task includes:
  - **TSP (Traveling Salesman Problem)** 
  - **Knapsack Problem**
  
- **Task 2**: Classifying emails as spam or ham using an Artificial Immune System (AIS).

Task 1 demonstrates the use of Genetic Algorithms to solve optimization problems, while Task 2 applies AIS for email classification, leveraging immune system-based learning techniques.

## Project Structure

The project is organized into the following modules and files:

### Modules

- **src.data**:
  - `load_data`: Load raw email data.
  - `preprocess`: Preprocess email data, including text extraction and cleaning.
- **src.models**:
  - `ais_csa_aggregator`: Contains functions for initializing antigen representations, training immune system-based classifiers (CSA), and predicting spam/ham emails.
- **src.evaluation**:
  - `metrics`: Functions to evaluate model performance (e.g., confusion matrix, accuracy, ROC curve).
- **results**:
  - `plot_results`: Function to plot results such as classification performance graphs.

### Main Scripts

- **main_1.py**: Implements the Genetic Algorithm (GA) for solving two optimization problems in Task 1:
  - **TSP (Traveling Salesman Problem)**
  - **Knapsack Problem**
  
- **main_2.py**: Implements the Artificial Immune System (AIS) for email classification in Task 2, which classifies emails into **spam** or **ham**.

## Requirements

Before running the project, make sure to install the necessary dependencies. You can generate the required packages using `pip` or `pipreqs`.

### To install the required dependencies:

ONE. Create a virtual environment (recommended).

TWO. Activate the virtual environment:
- On Windows, run: `. \venv\Scripts\activate`
- On Mac/Linux, run: `source venv/bin/activate`

THREE. Install the required packages by running: `pip install -r requirements.txt`

If you don't have a `requirements.txt`, generate it by running: `pip freeze > requirements.txt`

## Usage

### Task 1: Genetic Algorithms for Optimization Problems

#### Problem 1: Traveling Salesman Problem (TSP)

In this part of Task 1, the **Traveling Salesman Problem (TSP)** is solved using a Genetic Algorithm. The program:
- Loads the dataset for TSP.
- Runs the GA to optimize the route.
- Prints the best solution found and plots the results.

TO RUN THE TSP PROBLEM, run: `python main_1.py --tsp`

#### Problem 2: Knapsack Problem

The **Knapsack Problem** is the second optimization problem tackled in Task 1. The program:
- Reads input data (items with weights and profits).
- Runs the GA to optimize the selection of items to maximize profit without exceeding the weight limit.
- Outputs the best solution and visualizes the results.

TO RUN THE KNAPSACK PROBLEM, run: `python main_1.py --knapsack`

### Task 2: Email Classification using Artificial Immune System (AIS)

In Task 2, we apply an **Artificial Immune System (AIS)** to classify emails as **spam** or **ham**. The program:
- Loads and preprocesses the email data.
- Trains the AIS model with the emails.
- Makes predictions on a subset of emails (both spam and ham).
- Evaluates performance using metrics like accuracy, confusion matrix, and ROC curve.
- Visualizes the classification results.

TO RUN THE EMAIL CLASSIFICATION SCRIPT, run: `python main_2.py`

## Expected Output

- **For Task 1**: 
  - **TSP**: The program will print the best route found and plot the results showing the fitness progression.
  - **Knapsack Problem**: The program will display the best solution found for the knapsack problem, including the selected items and total profit.
  
- **For Task 2**:
  - The program will display predictions for randomly selected spam and ham emails.
  - The output will include performance evaluation results, such as confusion matrix and accuracy metrics.
  - The results will be visualized using a confusion matrix and ROC curve.

Example output for the email classification (Task 2):
Predictions for randomly selected SPAM emails: Spam Email 1: [email content here]... Prediction: spam

Predictions for randomly selected HAM emails: Ham Email 1: [email content here]... Prediction: ham

Additionally, you will see performance evaluation results:

Confusion Matrix: [[TP FP] [FN TN]]

## File Descriptions

- **main_1.py**: The first entry point of the project. This file solves the TSP and Knapsack problems using Genetic Algorithms.
- **main_2.py**: The second entry point of the project. This file classifies emails using an Artificial Immune System (AIS).
- **src/data/load_data.py**: Contains the `load_all_emails()` function to load email data.
- **src/data/preprocess.py**: Contains the `preprocess_email()` function to clean and preprocess the email data.
- **src/models/ais_csa_aggregator.py**: Contains functions like `initialize_antigens()`, `train_csa()`, `predict_email()`,

