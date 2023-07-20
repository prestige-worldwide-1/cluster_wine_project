import pandas as pd

def wrangle():
    
    # acquire
    df_r = pd.read_csv('https://query.data.world/s/fgwezltmmhwzdq6frrv7pf6jrl6vps?dws=00000')
    df_w = pd.read_csv('https://query.data.world/s/otk67utgv5232zzz3ooavdfwpcj2vz?dws=00000')
    
    # add color feature and 
    df_r['color'] = 'red'
    df_w['color'] = 'white'
    df = pd.concat([df_r, df_w], axis=0)
    
    # save data
    df.to_csv('wine_data_raw.csv', index=False)
    
    # drop duplicates
    df = df.drop_duplicates()
    
    df.to_csv('wine_data.csv', index=False)
    return df