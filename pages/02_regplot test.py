import streamlit as st
import common
import matplotlib.pyplot as plt
import seaborn as sns

common.page_config()

st.title("Regplot Visualization")

df_summary = common.get_sales()

df_date = df_summary['Measurement date'].str.split(" ", n=1, expand=True)

df_summary['date'] = df_date[0]
df_summary['time'] = df_date[1]
df_summary = df_summary.drop(['Measurement date'], axis=1)

df_0 = df_summary.groupby(['date'], as_index=False).agg({'SO2':'mean', 'NO2':'mean', 'O3':'mean', 'CO':'mean', 'PM10':'mean', 'PM2.5':'mean'})

variables = [('NO2', 'PM10'), ('NO2', 'PM2.5'), ('CO', 'PM10'), ('CO', 'PM2.5'),
             ('SO2', 'PM10'), ('SO2', 'PM2.5'), ('O3', 'PM10'), ('O3', 'PM2.5')]

for i, (x_var, y_var) in enumerate(variables):
    row = i // 2
    col = i % 2

    sns.regplot(x=x_var, y=y_var, data=df_0, ax=ax[row, col], ci=99, line_kws={'color': 'red'})
    slope, intercept, r_value, p_value, std_err = linregress(df_0[x_var], df_0[y_var])
    equation = f'R-squared: {r_value**2:.2f}'
    ax[row, col].text(0.05, 0.95, equation, transform=ax[row, col].transAxes, fontsize=12, verticalalignment='top', color='green')

plt.tight_layout()
plt.show()
