import pandas as pd
from sklearn.model_selection import train_test_split

def wrangle():
    
    # acquire
    df_r = pd.read_csv('https://query.data.world/s/fgwezltmmhwzdq6frrv7pf6jrl6vps?dws=00000')
    df_w = pd.read_csv('https://query.data.world/s/otk67utgv5232zzz3ooavdfwpcj2vz?dws=00000')
    
    # add color feature and 
    df_r['red'] = 1
    df_w['red'] = 0
    df = pd.concat([df_r, df_w], axis=0)
    
    # save data
    df.to_csv('wine_data_raw.csv', index=False)
    
    # drop duplicates
    df = df.drop_duplicates()
    
    df.to_csv('wine_data.csv', index=False)
    return df

def split_data(df, test_size=.15, validate_size=.15, stratify_col=None, random_state=None):
    '''
    take in a DataFrame and return train, validate, and test DataFrames;
    return train, validate, test DataFrames.
    '''
    # no stratification
    if stratify_col == None:
        # split test data
        train_validate, test = train_test_split(df, test_size=test_size, random_state=random_state)
        # split validate data
        train, validate = train_test_split(train_validate, test_size=validate_size/(1-test_size),
                                                                           random_state=random_state)
    # stratify split
    else:
        # split test data
        train_validate, test = train_test_split(df, test_size=test_size,
                                                random_state=random_state, stratify=df[stratify_col])
        # split validate data
        train, validate = train_test_split(train_validate, test_size=validate_size/(1-test_size),
                                           random_state=random_state, stratify=train_validate[stratify_col])       
    return train, validate, test
