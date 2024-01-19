from imblearn.under_sampling import RandomUnderSampler
rus = RandomUnderSampler(replacement=True,random_state=42)
X = df.drop('Class', axis=1).values
y = df['Class'].values
X_rus, y_rus = rus.fit_resample(X,y)




