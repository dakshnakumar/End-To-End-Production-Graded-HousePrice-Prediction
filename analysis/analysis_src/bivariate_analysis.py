
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Abstract class for bivariate analysis strategies
# Create common interface for different bivariate analysis strategies
class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self,df:pd.DataFrame, x:str, y:str):
        pass

# Concrete strategies for different types of bivariate analysis
# Strategy for numerical vs numerical analysis
class NumbericalVsNumericalStrategy(BivariateAnalysisStrategy):
    def analyze(self,df:pd.DataFrame, x:str, y:str):
        plt.figure(figsize=(10,6))
        sns.scatterplot(data=df,x=x,y=y)
        plt.title(f'Scatter Plot of {x} vs {y}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

# Strategy for categorical vs categorical analysis
class CategoricalVsNumericalStategy(BivariateAnalysisStrategy):
    def analyze(self,df:pd.DataFrame, x:str, y:str):
        plt.figure(figsize=(10,6))
        sns.boxplot(data=df,x=x,y=y)
        plt.title(f'Box Plot of {x} vs {y}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

# context class to switch between different strategies
class BivariateAnalyzer():
    def __init__(self,_statergy:BivariateAnalysisStrategy):
        self._statergy = _statergy
    
    def set_strategy(self, strategy:BivariateAnalysisStrategy):
        self._statergy = strategy
    
    def execute_analysis(self, df:pd.DataFrame, x:str, y:str):
       self._statergy.analyze(df,x,y)

if __name__ == "__main__":      
    pass



    



