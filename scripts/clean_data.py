import pandas as pd

def clean_csv(df):
    deleteWords = ['others', 'ponies', 'and', 'all']
    mask = df['pony'].apply(lambda x: all(word.lower() not in deleteWords for word in x.split()))
    df = df[mask].reset_index(drop=True)
    df['pony'] = df['pony'].apply(lambda x: x.lower())
    return df
def getTopPonies(df):
    # Get the top 101 most frequent characters 
    # frequency = number of lines spoken
    top_characters = df['pony'].value_counts().head(101)
    return top_characters


def main():
    df = pd.read_csv('/home/nemo/repos/ethann-github/Network-Modeling-MLP/data/raw_data/clean_dialog.csv')
    NewDf = clean_csv(df)
    top_characters = NewDf['pony'].value_counts().head(101).index.tolist()
    NewDf = NewDf[NewDf['pony'].isin(top_characters)]
    NewDf.to_csv('/home/nemo/repos/ethann-github/Network-Modeling-MLP/data/output/script_output.csv', index=False)

if __name__ == "__main__":  
    main()