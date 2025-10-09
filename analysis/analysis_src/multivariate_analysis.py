from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class MultivariateAnalysisTemplate(ABC):
    def analyze(self,df:pd.DataFrame):
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)

        @abstractmethod
        def generate_correlation_heatmap(self, df: pd.DataFrame):
            pass
        
        @abstractmethod
        def generate_pairplot(self, df: pd.DataFrame):
            pass

class SimpleMultivariateAnalysis(MultivariateAnalysisTemplate):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        plt.figure(figsize=(12, 8))
        correlation_matrix = df.corr()
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()

    def generate_pairplot(self, df: pd.DataFrame):
        sns.pairplot(df)
        plt.suptitle('Pairplot of Features', y=1.02)
        plt.show()

if __name__ == "__main__":
    pass