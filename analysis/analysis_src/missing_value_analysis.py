from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class MissingValues(ABC):
    def analyze(self, df: pd.DataFrame):
        self.identify_missing_values(df)
        self.visualize_missing_values(df)

    @abstractmethod
    def identify_missing_values(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def visualize_missing_values(self, df: pd.DataFrame):
        pass

class SimpleMissingValuesAnalysis(MissingValues):
    def identify_missing_values(self, df: pd.DataFrame):
        print("Missing values per column:")
        print(df.isnull().sum())
        print("\nPercentage of missing values per column:")
        print(df.isnull().sum() / len(df) * 100)

    def visualize_missing_values(self, df: pd.DataFrame):
        plt.figure(figsize=(12, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        plt.title('Missing Values Heatmap')
        plt.show()


if __name__ == "__main__":
    pass    