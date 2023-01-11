import pandas as pd

def main():
  df=pd.read_csv('data')
  print(df.head())
  df_small=df[:100000]
  df_small.to_csv('small_data.csv')


if __name__=='__main__':
  main()
