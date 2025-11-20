import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import glob

class RunHeatmap:
    
    @classmethod
    def get_csv_files(self):
        data_path = "./dataset/dataset"
        csv_files = glob.glob(f"{data_path}/*.csv")
        return csv_files 
       
    @classmethod
    def file_to_df_dict(self):
        csv_files = self.get_csv_files()
        df_dict = {}
        for file in csv_files:
            file_name = file.split("/")[-1].replace(".csv", "")
            df_dict[file_name] = pd.read_csv(file)
        return df_dict
    
    @classmethod
    def get_category(self, df_dict, df_name,category_name):
        industry_df = df_dict[df_name][category_name]
        industry_list = []
        for industry in industry_df:
            if industry not in industry_list:
                industry_list.append(industry)
        return industry_list
    
    @classmethod
    def summary_statistics(self, df, drop_columns):
        summary_df = df.describe().drop(drop_columns, axis=1)
        return summary_df
    
    @classmethod
    def plot_heatmap(self, df):
        corr = df.corr(numeric_only=True)
        plt.figure(figsize=(20, 18))
        mask = np.triu(np.ones_like(corr, dtype=bool))
        sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm',
                    linewidths=0.5, annot_kws={"size": 6})
        plt.xticks(rotation=45, ha='right')
        plt.title("Heatmapa korelacji między zmiennymi", fontsize=16)
        plt.show()
        
if __name__ == "__main__":
    df_dict = RunHeatmap.file_to_df_dict()
    print(df_dict.keys())
    df_fi = df_dict["dataset\\Annual_P_L_1_final"]
    summary_fi = RunHeatmap.summary_statistics(df_fi, drop_columns=['BSE Code'])
    print(summary_fi)
    RunHeatmap.plot_heatmap(df_fi)