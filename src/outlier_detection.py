import logging
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class OutlierDetection(ABC):
    @abstractmethod
    def detect_outlier(self,df:pd.DataFrame) -> pd.DataFrame:
        pass

class ZScoreOutlierDetection(OutlierDetection):
    def __init__(self,threshold=3):
        self.threshold = threshold

    def detect_outlier(self, df:pd.DataFrame) -> pd.DataFrame:
        logging.info("Detecting outliers using the Z-score method.")
        z_scores = np.abs((df.mean()/df.std()))
        outliers = z_scores > self.threshold
        logging.info(f"Outliers detected with Z-score threshold: {self.threshold}.")
        return outliers
    
class IQROutlierDetection(OutlierDetection):
    def detect_outlier(self,df:pd.DataFrame) -> pd.DataFrame:
        logging.info("Detecting outliers using the IQR method.")
        Q1 = np.quantile(0.25)
        Q3 = np.quantile(0.75)
        IQR = Q3-Q1
        outliers = (df < (Q1 - 1.5 * IQR) | df > (Q3 + 1.5 * IQR))
        logging.info("Outliers detected using the IQR method.")
        return outliers
    
class OutlierDetector:
    def __init__(self,strategy:OutlierDetection):
        self.strategy=strategy

    def set_strategy(self,strategy):
        logging.info(f"Switching outlier detection strategy.")
        self.strategy = strategy

    def detect_outlier(self, df:pd.DataFrame) -> pd.DataFrame :
        logging.info("Executing outlier detection")
        return self.strategy.detect_outlier(df)
    
    def handle_outliers(self,df:pd.DataFrame,method="remove")-> pd.DataFrame:
        outlier = self.detect_outlier(df)
        if method == "remove":
          logging.info("Removing Outliers from Dataset")
          df_cleaned = df[(~ outlier).all(axis=1)]
        elif method == "cap":
           logging.info("Capping outliers from the dataset") 
           df_cleaned = df.clip(lower=df.quantile(0.01),upper=df.quantile(0.99),axis=1) #axis = 1 refers to row
        else:
            logging.warning(f"Unknown method '{method}'. No outlier handling performed.")
            return df
        logging.info("Outliers handling completed")
        return df_cleaned

    def visualize_outlier(self,df:pd.DataFrame,features:list):
        for feature in features:
            plt.figure(figsize=(10,6))
            sns.boxplot(x=df[feature])
            plt.title(f"Boxplot of {feature}")
            plt.show()
        logging.info("Outlier visualization completed.")



        
        