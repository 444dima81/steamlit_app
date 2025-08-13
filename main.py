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

# --- Боковая панель ---
st.sidebar.header("Настройки фильтрации")

sex_filter = st.sidebar.multiselect(
    "Пол",
    options=tips['sex'].unique(),
    default=tips['sex'].unique()
)

smoker_filter = st.sidebar.multiselect(
    "Курение",
    options=tips['smoker'].unique(),
    default=tips['smoker'].unique()
)

time_filter = st.sidebar.multiselect(
    "Время приема пищи",
    options=tips['time'].unique(),
    default=tips['time'].unique()
)

chart_type = st.sidebar.selectbox(
    "Тип графика",
    ["Scatter", "Box", "Histogram"]
)
point_size = st.sidebar.slider("Размер точек (для Scatter)", 50, 300, 100)
# Header
st.title('Проект по визализации данных')
st.subheader(f"Подбробная Статистика Чаевых ", divider='gray')

# Вывод таблицы
st.markdown("### Общий план данных")
st.dataframe(tips)

# Построение графиков
fig, ax = plt.subplots(figsize=(8, 5))

if chart_type == "Scatter":
    sns.scatterplot(
        data=tips,
        x='total_bill',
        y='tip',
        hue='sex',
        style='smoker',
        s=point_size,
        ax=ax
    )
    ax.set_title("Связь между счетом и чаевыми")

elif chart_type == "Box":
    sns.boxplot(
        data=tips,
        x='day',
        y='total_bill',
        hue='time',
        ax=ax
    )
    ax.set_title("Сумма счетов по дням недели")

elif chart_type == "Histogram":
    sns.histplot(
        data=tips,
        x='total_bill',
        hue='sex',
        ax=ax
    )
    ax.set_title("Распределение суммы счетов")

st.pyplot(fig)