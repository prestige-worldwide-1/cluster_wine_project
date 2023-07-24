import pandas as pd

from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score

from sklearn.preprocessing import MinMaxScaler

from sklearn.cluster import KMeans

from wrangle import split_data


def preprecess_data(df):
    
    # split data
    train, validate, test = split_data(df)
    
    # MinMax scale features
    scaler = MinMaxScaler()
    
    train = pd.concat([pd.DataFrame(data=scaler.fit_transform(train.drop(columns=['quality'])),
                                   columns=train.drop(columns=['quality']).columns),
                      train[['quality']].reset_index().iloc[:,1]],
                      axis=1)
    validate = pd.concat([pd.DataFrame(data=scaler.transform(validate.drop(columns=['quality'])),
                                       columns=validate.drop(columns=['quality']).columns),
                             validate[['quality']].reset_index().iloc[:,1]],
                             axis=1)

    test = pd.concat([pd.DataFrame(data=scaler.transform(test.drop(columns=['quality'])),
                                       columns=test.drop(columns=['quality']).columns),
                         test[['quality']].reset_index().iloc[:,1]],
                         axis=1)
    
    # create 1st group of clusters
    feats1 = ['fixed acidity', 'chlorides', 'alcohol']

    kmeans1 = KMeans(n_clusters=4, random_state=123).fit(train[feats1])

    train['clusters_1'] = kmeans1.predict(train[feats1])
    validate['clusters_1'] = kmeans1.predict(validate[feats1])
    test['clusters_1'] = kmeans1.predict(test[feats1])

    # create 2nd group of clusters
    feats2 = ['fixed acidity', 'alcohol']

    kmeans2 = KMeans(n_clusters=4, random_state=123).fit(train[feats2])

    train['clusters_2'] = kmeans2.predict(train[feats2])
    validate['clusters_2'] = kmeans2.predict(validate[feats2])
    test['clusters_2'] = kmeans2.predict(test[feats2])
    
    # create 3rd group of clusters
    feats3 = ['free sulfur dioxide', 'residual sugar', 'alcohol']

    kmeans3 = KMeans(n_clusters=4, random_state=123).fit(train[feats3])

    train['clusters_3'] = kmeans3.predict(train[feats3])
    validate['clusters_3'] = kmeans3.predict(validate[feats3])
    test['clusters_3'] = kmeans3.predict(test[feats3])
    
    # encode clusters
    train = pd.concat([train, 
                        pd.get_dummies(train[['clusters_1','clusters_2','clusters_3']].astype(str))],
                        axis=1)
    validate = pd.concat([validate, 
                            pd.get_dummies(validate[['clusters_1','clusters_2','clusters_3']].astype(str))],
                            axis=1)
    test = pd.concat([test, 
                        pd.get_dummies(test[['clusters_1','clusters_2','clusters_3']].astype(str))],
                        axis=1)
    
    return train, validate, test

def run_baseline_model(train, test, features, target):
    
    # split X and y
    X_train = train[features]
    X_test = test[features]

    y_train = train[target]
    y_test = test[target]
    
    # run model
    dummy = DummyRegressor().fit(X_train, y_train)    
    
    # RMSE
    train_rmse = mean_squared_error(y_train, dummy.predict(X_train), squared=False)
    test_rmse = mean_squared_error(y_test, dummy.predict(X_test), squared=False)
    # R2
    train_r2 = r2_score(y_train, dummy.predict(X_train))
    test_r2 = r2_score(y_test, dummy.predict(X_test))
    
    print(f'Train:\tRMSE = {train_rmse}\tR2 = {train_r2}')
    print(f'Test:\tRMSE = {test_rmse}\tR2 = {test_r2}')
    
    return train_rmse, train_r2, test_rmse, test_r2

def run_linear_model(train, test, features, target):
    
    # split X and y
    X_train = train[features]
    X_test = test[features]

    y_train = train[target]
    y_test = test[target]
    
    # run model
    lm = LinearRegression().fit(X_train, y_train)    
    
    # RMSE
    train_rmse = mean_squared_error(y_train, lm.predict(X_train), squared=False)
    test_rmse = mean_squared_error(y_test, lm.predict(X_test), squared=False)
    # R2
    train_r2 = r2_score(y_train, lm.predict(X_train))
    test_r2 = r2_score(y_test, lm.predict(X_test))
    
    print(f'Train:\tRMSE = {train_rmse}\tR2 = {train_r2}')
    print(f'Test:\tRMSE = {test_rmse}\tR2 = {test_r2}')
    
    return train_rmse, train_r2, test_rmse, test_r2