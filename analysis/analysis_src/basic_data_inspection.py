from abc import ABC , abstractmethod
import pandas as pd

class DataInspectionStatergy(ABC):
    @abstractmethod
    def inspect(self, data: pd.DataFrame) :
        pass

class DataTypeInscpectionStatergy(DataInspectionStatergy):
    def inspect(self, df: pd.DataFrame) :
        print("\n Data Types and Non-Null Counts:")
        print(df.info())

class SummaryStatisticsInspectionStartergy(DataInspectionStatergy):
    def inspect(self,df:pd.DataFrame):
        print("\n Summary Statistics:")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=[0]))


class DataInspector():
    def __init__(self, strategy: DataInspectionStatergy):
        self._strategy = strategy

    def set_startegy(self, strategy: DataInspectionStatergy):
        self._strategy = strategy

    def execute_inspection(self, df:pd.DataFrame):
        self._strategy.inspect(df)


if __name__ == "__main__":
    pass