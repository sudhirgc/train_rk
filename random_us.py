from imblearn.under_sampling import smote
rus = smote()
X = df.drop('Class', axis=1).values
y = df['Class'].values
X_rus, y_rus = rus.fit_resample(X,y)




