import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date, timedelta

# Настройка оформления
st.set_page_config(page_title="Apple Dashboard", layout="wide")
sns.set_theme(style="whitegrid")

# Сайдбар
st.sidebar.header("Настройки")

start_date = st.sidebar.date_input(
    "Дата начала",
    value=date.today() - timedelta(days=180)
)
end_date = st.sidebar.date_input(
    "Дата окончания",
    value=date.today()
)

chart_type = st.sidebar.selectbox(
    "Тип графика",
    ["Линейный"]
)

# Загрузка данных 
ticker = "AAPL"
data = yf.download(ticker, start=start_date, end=end_date)

# Заголовок + дата
st.title(f"Котировки Apple")
st.subheader(f"Данные за {start_date} — {end_date}", divider=True)
st.markdown("График для анализа котировок Apple")

# Построение графика
if not data.empty:
    if chart_type == "Линейный":
        fig, ax = plt.subplots(figsize=(10, 5))
        close_prices = data["Close"].squeeze()  # превращаем в Series
        sns.lineplot(x=data.index, y=close_prices, ax=ax, color="blue")
        ax.set_title("Динамика цен", fontsize=14)
        ax.set_xlabel("Дата")
        ax.set_ylabel("Цена (USD)")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # Таблица 
    st.subheader("Данные", divider=True)
    st.dataframe(data.style.format("{:.2f}"))
else:
    st.warning("Нет данных за выбранный период.")
    