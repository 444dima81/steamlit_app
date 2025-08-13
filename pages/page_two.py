import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import date, timedelta

# Настройка оформления
st.set_page_config(page_title="Tips Dashbords", layout="wide")
sns.set_theme(style="whitegrid")
tips = pd.read_csv('tips.csv')

sns.set_theme(style="whitegrid")

st.title("Визуализации по данным чаевых")
# 1
st.subheader("Гистограмма суммы счёта", divider='rainbow')
st.markdown("##### Сумма счетов/кол-во заказов")
fig, ax = plt.subplots()
sns.histplot(data=tips, x="total_bill", kde=True, ax=ax, color="skyblue")
ax.set_xlabel('Сумма счетов')
ax.set_ylabel('Колиечество заказов')
st.pyplot(fig)

# 2
st.subheader("Связь между суммой счёта и чаевыми", divider='rainbow')
st.markdown("##### Сумма счетов/кол-во чаевых")
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip", ax=ax, color="orange")
ax.set_xlabel('Сумма счетов')
ax.set_ylabel('Количество чаевых')
st.pyplot(fig)

# 3
st.subheader("Boxplot суммы счётов по дням недели и времени", divider='rainbow')
st.markdown("##### День недели/Сумма счетов")
fig, ax = plt.subplots()
sns.boxplot(data=tips, x="day", y="total_bill", hue="time", ax=ax, palette="Set2")
ax.set_xlabel('День недели')
ax.set_ylabel('Сумма счетов')
st.pyplot(fig)

# 4
st.subheader("Гистограммы чаевых по времени дня", divider='rainbow')
st.markdown("##### Чаевые/Кол-во заказов по времени дня ")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(tips[tips["time"] == "Lunch"]["tip"], ax=axes[0], color="pink", kde=True)
axes[0].set_xlabel('Чаевые')
axes[0].set_ylabel('Кол-во Заказов')
axes[0].set_title("Lunch")
sns.histplot(tips[tips["time"] == "Dinner"]["tip"], ax=axes[1], color="blue", kde=True)
axes[1].set_xlabel('Чаевые')
axes[1].set_ylabel('Кол-во Заказов')
axes[1].set_title("Dinner")

st.pyplot(fig)