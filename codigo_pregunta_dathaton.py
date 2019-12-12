import pandas as pd
df_cars=pd.read_csv('dathaton/Dataset/dfCarsVSDemo.csv') 

df_groupby_=df_cars.groupby(
        ['Symbol'],as_index=False
).agg({
'pickup_datetime':'count'
}
)
statistic, pvalue = stats.ttest_ind(df_groupby__[df_groupby__.Symbol=="U15"].trips, df_groupby__[df_groupby__.Symbol=="YCT"].trips, equal_var=False)
print('',statistic, pvalue)
anova = ols('trips ~ C(Symbol)', data=df_groupby__).fit()
aov_tables = st.stats.anova_lm(anova, typ=2)
aov_tables
df_car_u14=df_cars[df_cars['Symbol']=='U14']
df_groupby_14=df_car_u14.groupby(
        ['nta_code','nta_name','borough'],as_index=False
).agg({
'pickup_datetime':'count',
'population':'mean',
'under_5_years':'mean',
'5-9_years':'mean',
'10-14_years':'mean',
'15-19_years':'mean',
'20-24_years':'mean',
'25-29_years':'mean',
'30-34_years':'mean',
'35-39_years':'mean',
'40-44_years':'mean',
'45-49_years':'mean',
'50-54_years':'mean',
'55-59_years':'mean',
'60-64_years':'mean',
'over_65_years':'mean',
'median_age':'mean',
'people_per_acre':'mean',
'households':'mean',
'median_income':'mean',
'mean_income':'mean'
}
)








df_groupby_14.rename(columns={'pickup_datetime': 'trips'}, inplace=True)
X=df_groupby_14[['population','under_5_years','5-9_years','10-14_years','15-19_years',
				 '20-24_years','25-29_years','30-34_years','35-39_years','40-44_years','45-49_years','50-54_years',
				 '55-59_years','60-64_years','over_65_years','median_age','people_per_acre','households']]
y=df_groupby_14['trips']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
import statsmodels.api as st
X_constant=st.add_constant(X_train)
model1=st.OLS(y_train,X_constant).fit()
model1.summary()





df_car_u15=df_cars[df_cars['Symbol']=='U15']
df_groupby_15=df_car_u15.groupby(
        ['nta_code','nta_name','borough'],as_index=False
).agg({
'pickup_datetime':'count',
'population':'mean',
'under_5_years':'mean',
'5-9_years':'mean',
'10-14_years':'mean',
'15-19_years':'mean',
'20-24_years':'mean',
'25-29_years':'mean',
'30-34_years':'mean',
'35-39_years':'mean',
'40-44_years':'mean',
'45-49_years':'mean',
'50-54_years':'mean',
'55-59_years':'mean',
'60-64_years':'mean',
'over_65_years':'mean',
'median_age':'mean',
'people_per_acre':'mean',
'households':'mean',
'median_income':'mean',
'mean_income':'mean'
}
)
df_groupby_15.rename(columns={'pickup_datetime': 'trips'}, inplace=True)
X=df_groupby_15[['population','under_5_years','5-9_years','10-14_years','15-19_years',
				 '20-24_years','25-29_years','30-34_years','35-39_years','40-44_years','45-49_years','50-54_years',
				 '55-59_years','60-64_years','over_65_years','median_age','people_per_acre','households']]
y=df_groupby_15['trips']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
import statsmodels.api as st
X_constant=st.add_constant(X_train)
model1=st.OLS(y_train,X_constant).fit()
model1.summary()
df_car_yw=df_cars[df_cars['Symbol']=='YCT']
df_groupby_yw=df_car_yw.groupby(
        ['nta_code','nta_name','borough'],as_index=False
).agg({
'pickup_datetime':'count',
'population':'mean',
'under_5_years':'mean',
'5-9_years':'mean',
'10-14_years':'mean',
'15-19_years':'mean',
'20-24_years':'mean',
'25-29_years':'mean',
'30-34_years':'mean',
'35-39_years':'mean',
'40-44_years':'mean',
'45-49_years':'mean',
'50-54_years':'mean',
'55-59_years':'mean',
'60-64_years':'mean',
'over_65_years':'mean',
'median_age':'mean',
'people_per_acre':'mean',
'households':'mean',
'median_income':'mean',
'mean_income':'mean'
}
)
df_groupby_yw.rename(columns={'pickup_datetime': 'trips'}, inplace=True)
X=df_groupby_yw[['population','under_5_years','5-9_years','10-14_years','15-19_years',
				 '20-24_years','25-29_years','30-34_years','35-39_years','40-44_years','45-49_years','50-54_years',
				 '55-59_years','60-64_years','over_65_years','median_age','people_per_acre','households']]
y=df_groupby_yw['trips']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
import statsmodels.api as st
X_constant=st.add_constant(X_train)
model1=st.OLS(y_train,X_constant).fit()
model1.summary()

df_car_g=df_cars[df_cars['Symbol']=='GCT']
df_groupby_g=df_car_g.groupby(
        ['nta_code','nta_name','borough'],as_index=False
).agg({
'pickup_datetime':'count',
'population':'mean',
'under_5_years':'mean',
'5-9_years':'mean',
'10-14_years':'mean',
'15-19_years':'mean',
'20-24_years':'mean',
'25-29_years':'mean',
'30-34_years':'mean',
'35-39_years':'mean',
'40-44_years':'mean',
'45-49_years':'mean',
'50-54_years':'mean',
'55-59_years':'mean',
'60-64_years':'mean',
'over_65_years':'mean',
'median_age':'mean',
'people_per_acre':'mean',
'households':'mean',
'median_income':'mean',
'mean_income':'mean'
}
)


































df_groupby_g.rename(columns={'pickup_datetime': 'trips'}, inplace=True)
X=df_groupby_g[['population','under_5_years','5-9_years','10-14_years','15-19_years',
				 '20-24_years','25-29_years','30-34_years','35-39_years','40-44_years','45-49_years','50-54_years',
				 '55-59_years','60-64_years','over_65_years','median_age','people_per_acre','households']]
y=df_groupby_g['trips']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
import statsmodels.api as st
X_constant=st.add_constant(X_train)
model1=st.OLS(y_train,X_constant).fit()
model1.summary()