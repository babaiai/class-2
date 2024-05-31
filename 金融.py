import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# 从本地文件读取股票数据
df = pd.read_csv('C:\\Users\\vicky\\Desktop\\學校\\333\\6560.csv')

# 计算移动平均线（MA）
df['MA_20'] = df['close'].rolling(window=20).mean()

# 计算相对强弱指标（RSI）
def calculate_rsi(df, period=14):
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

df['RSI'] = calculate_rsi(df)

# 数据可视化
fig = go.Figure()

# 添加股票价格线
fig.add_trace(go.Scatter(x=df['date'], y=df['close'], mode='lines', name='close Price'))

# 添加移动平均线
fig.add_trace(go.Scatter(x=df['date'], y=df['MA_20'], mode='lines', name='20-Day MA'))

# 添加RSI指标
fig.add_trace(go.Scatter(x=df['date'], y=df['RSI'], mode='lines', name='RSI'))

# 更新图表布局
fig.update_layout(title='股票数据与技术指标可视化',
                   xaxis_title='日期',
                   yaxis_title='价格/RSI',
                   template='plotly_dark')

# 显示图表
st.plotly_chart(fig)
