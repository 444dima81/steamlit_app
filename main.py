import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Настройка оформления
st.set_page_config(page_title="Tips Dashboards", layout="wide")
sns.set_theme(style="whitegrid")
tips = pd.read_csv('tips.csv')

#  Боковая панель
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

# Фунция фильтрации
tips_filtered = tips[
    (tips['sex'].isin(sex_filter)) &
    (tips['smoker'].isin(smoker_filter)) &
    (tips['time'].isin(time_filter))
]

# Header
st.title('Проект по визуализации данных')
st.subheader("Подробная статистика чаевых", divider='gray')

# Вывод таблицы
st.markdown("### Отфильтрованные данные")
st.dataframe(tips_filtered)

# Построение графиков 
fig, ax = plt.subplots(figsize=(8, 5))

if chart_type == "Scatter":
    sns.scatterplot(
        data=tips_filtered,
        x='total_bill',
        y='tip',
        hue='sex',
        style='smoker',
        s=point_size,
        ax=ax
    )
    ax.set_title("Связь между счетом и чаевыми")
    ax.set_xlabel("Сумма счёта")
    ax.set_ylabel("Чаевые")

elif chart_type == "Box":
    sns.boxplot(
        data=tips_filtered,
        x='day',
        y='total_bill',
        hue='time',
        ax=ax
    )
    ax.set_title("Сумма счетов по дням недели")
    ax.set_xlabel("День недели")
    ax.set_ylabel("Сумма счёта")

elif chart_type == "Histogram":
    sns.histplot(
        data=tips_filtered,
        x='total_bill',
        hue='sex',
        ax=ax
    )
    ax.set_title("Распределение суммы счетов")
    ax.set_xlabel("Сумма счёта")
    ax.set_ylabel("Количество заказов")

st.pyplot(fig)