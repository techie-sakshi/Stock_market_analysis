# Stock Market Analysis using Python 📊

This project presents an end-to-end analysis of stock price data using Python libraries like `pandas`, `matplotlib`, `seaborn`, and `mplfinance`. It includes daily return calculations, moving averages, volatility, candlestick visualization, and trend analysis.

---

## 📁 Dataset
- File: `infy_stock.csv`
- Columns: `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`
- Data Type: Historical stock price data

---

## 🛠️ Tools & Libraries
- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- mplfinance

---

## 📌 Project Tasks & Highlights

### 1. Load and Inspect the Data
- Loaded CSV using pandas
- Displayed first 10 rows
- Checked for missing/null values and handled them

### 2. Data Visualization
- Line plot of closing price over time
- Candlestick chart using `mplfinance`

### 3. Statistical Analysis
- Calculated daily return percentage:
  \> `((Close - Open) / Open) * 100`
- Computed mean, median, and standard deviation of daily returns
- Calculated standard deviation of closing prices

### 4. Moving Averages
- Calculated 50-day and 200-day moving averages
- Visualized crossover trends with closing prices

### 5. Volatility Analysis
- Plotted 30-day rolling standard deviation of closing prices

### 6. Trend Analysis (Bullish/Bearish)
- Detected bullish/bearish trends using 50-day vs 200-day moving average crossover
- Marked trend shifts visually on plot

---

## 📈 Sample Visuals (Add These to Your Repo)
- `closing_price_plot.png`
- `candlestick_chart.png`
- `volatility_plot.png`
- `moving_average_crossover.png`

---

## 🔍 Key Insights
- Detected multiple bullish and bearish phases across the dataset
- Volatility spikes aligned with major market events
- Long-term trends could be predicted with moving averages

---

## 🚀 How to Run
1. Clone this repo
2. Install dependencies using `pip install -r requirements.txt`
3. Run the notebook: `stock_analysis.ipynb`

---

## 📎 File Structure
