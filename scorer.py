from sklearn.metrics import log_loss, confusion_matrix
from sklearn.model_selection import train_test_split
import xgboost as xgb
import numpy as np

def scorer(X, y):
    X_tr, X_cv, y_tr, y_cv = train_test_split(X, y, test_size=0.2, random_state=0)
    params = {}
    params['objective'] = 'binary:logistic'
    params['eval_metric'] = 'logloss'
    params['eta'] = 0.02
    params['max_depth'] = 4

    d_train = xgb.DMatrix(X_tr, label=y_tr)
    d_valid = xgb.DMatrix(X_cv, label=y_cv)

    watchlist = [(d_train, 'train'), (d_valid, 'valid')]

    bst = xgb.train(params, d_train, 400, watchlist, early_stopping_rounds=50, verbose_eval=10)
    d_cv = xgb.DMatrix(X_cv)
    y_cv_pred = bst.predict(d_cv)

    print("Score is", log_loss(y_cv, y_cv_pred))

    d_all = xgb.DMatrix(X, label=y)
    y_pred = bst.predict(d_all)
    y_pred = np.vectorize(lambda x: 1 if x >= 0.5 else 0)(y_pred)
    print(confusion_matrix(y, y_pred))

    return y_pred