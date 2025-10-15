# End-to-End House Price Prediction with MLOps

This project demonstrates a production-grade, end-to-end machine learning pipeline for predicting house prices using the Ames Housing dataset. It is built with a focus on MLOps principles, utilizing **ZenML** to create a reproducible, modular, and extensible workflow from data ingestion to model deployment.

## ✨ Features

- **End-to-End MLOps Pipeline**: Orchestrates all steps from data ingestion to model deployment using ZenML.
- **Experiment Tracking**: Integrates with **MLflow** to log model parameters, metrics, and artifacts for every run.
- **Model Deployment**: Deploys the trained model as a REST API service using the MLflow model deployer.
- **Modular Design**: Uses the Strategy Design Pattern for components like data ingestion, feature engineering, and outlier detection, making it easy to extend or modify.
- **Continuous Deployment**: Includes a deployment pipeline that automatically promotes and deploys a model if it meets performance criteria.
- **Containerization**: Uses **Docker** to run pipeline steps and services, ensuring a consistent and isolated environment.

## 🛠️ Tech Stack

- **Orchestration**: [ZenML](https://zenml.io/)
- **Experiment Tracking**: [MLflow](https://mlflow.org/)
- **Machine Learning**: [Scikit-learn](https://scikit-learn.org/)
- **Data Handling**: [Pandas](https://pandas.pydata.org/)

## 📂 Project Structure

```
├── pipelines/
│   ├── training_pipeline.py      # Defines the model training and evaluation pipeline.
│   └── deployment_pipeline.py    # Defines the model deployment and inference pipeline.
├── src/
│   ├── data_splitter.py
│   ├── feature_engineering.py
│   ├── handle_missing_values.py
│   ├── ingest_data.py
│   ├── model_evaluator.py
│   └── outlier_detection.py
├── steps/
│   ├── data_ingestion_step.py
│   ├── data_splitter_step.py
│   ├── feature_engineering_step.py
│   ├── handle_missing_value_step.py
│   ├── model_building_step.py
│   ├── model_evaluator_step.py
│   └── outlier_detection_step.py
├── data/
│   └── archive.zip               # The raw dataset.
├── .gitignore
├── requirements.txt
└── run_pipeline.py               # Script to execute the training pipeline.
└── run_deployment.py             # Script to execute the deployment pipeline.
```

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Conda](https://docs.conda.io/en/latest/miniconda.html) (recommended for environment management)

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/End-To-End-Production-Graded-HousePrice-Prediction.git
cd End-To-End-Production-Graded-HousePrice-Prediction
```

### 3. Set Up the Environment

Create and activate a Conda environment, then install the required packages.

```bash
# Create a new conda environment
conda create --name houseprice-env python=3.8 -y

# Activate the environment
conda activate houseprice-env

# Install dependencies
pip install -r requirements.txt
```

### 4. Configure the ZenML Stack

This project requires a local ZenML stack with MLflow for experiment tracking and model deployment.

```bash
# Install ZenML integrations
zenml integration install mlflow -y

# Register the components
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register mlflow_deployer --flavor=mlflow

# Create and activate the stack
zenml stack register mlflow_stack -o default -a default -e mlflow_tracker -md mlflow_deployer
zenml stack set mlflow_stack
```

## 🏃 How to Run the Pipelines

### 1. Run the Training Pipeline

This will ingest the data, preprocess it, train a model, and log the results to MLflow.

```bash
python run_pipeline.py
```

### 2. Run the Deployment Pipeline

This pipeline deploys the best model as a REST API service and runs a sample prediction.

```bash
python run_deployment.py
```

After running, the script will print the prediction server URL. You can use `sample_predict.py` to send a request or use the `--stop-service` flag to shut down the server.

### 3. View Experiments in MLflow

You can launch the MLflow UI to inspect and compare your runs.

```bash
mlflow ui --backend-store-uri "file:$(zenml stack describe | grep 'artifact_store' -A 2 | grep 'path' | awk -F': ' '{print $2}')/mlruns"
```