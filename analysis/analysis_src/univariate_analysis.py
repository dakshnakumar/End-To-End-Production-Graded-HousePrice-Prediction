from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class UnivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, column: str):
        pass

class NumericalUnivariateStrategy(UnivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, column: str):
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

class CategoricalUnivariateStrategy(UnivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, column: str):
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x=column, palette="muted")
        plt.title(f'Count Plot of {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right') # Rotate labels 45 degrees
        plt.tight_layout()
        plt.show()

class UnivariateAnalyzer:
    def __init__(self,strategy:UnivariateAnalysisStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: UnivariateAnalysisStrategy):
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, column: str):
        self._strategy.analyze(df,column=column)

if __name__ == "__main__":
    pass