# Amazon-Stock-Price-Forecasting-Using-LSTM-and-GAN
Time Series Forecasting with LSTM and GAN to predict Amazon Stock Prices

## Data

Amazon Stock Price data from 01/01/2010 to 04/04/2023

![AMZN](https://github.com/fola789/Amazon-Stock-Price-Forecasting-Using-LSTM-and-GAN/blob/master/amzndata.png)

### Key Data
- Exponential Moving Average (EMA): EMA is a type of moving average that gives greater weight to more recent prices. It is calculated by taking a certain percentage of the latest closing price and adding it to the previous EMA. This results in a smoother line compared to a simple moving average, and it is commonly used to identify trends in stock prices.
- Moving Average Convergence Divergence (MACD): MACD is a trend-following momentum indicator that shows the relationship between two moving averages of the 'Close' price. It is calculated by subtracting the 26-period Exponential Moving Average (EMA) from the 12-period EMA. The signal line, which is a 9-period EMA of the MACD line, is then plotted on top of the MACD line. Traders use MACD to identify changes in momentum, direction, and the strength of the trend.
- Relative Strength Index (RSI): RSI is a technical indicator that measures the strength of a security by comparing its average gains and losses over a certain period of time. It ranges from 0 to 100, and readings above 70 are considered overbought, while readings below 30 are considered oversold. RSI is commonly used to identify potential trend reversals and to generate buy and sell signals.
- Average True Range (ATR): ATR is a technical indicator that measures volatility by taking into account the range of the 'High' and 'Low' prices over a certain period of time. It is calculated by finding the average true range of each day, which is the maximum of the following: the distance between the high and the low, the absolute value of the difference between the high and the previous close, and the absolute value of the difference between the low and the previous close. Traders use ATR to identify potential price breakouts and to set stop-loss levels.
- Bollinger Bands: Bollinger Bands are a technical indicator that consist of a simple moving average (typically 20 periods) and two standard deviations above and below the moving average. The upper and lower bands represent the upper and lower price levels that a stock is expected to trade within. When the price moves above the upper band, it is considered overbought, and when the price moves below the lower band, it is considered oversold. Bollinger Bands are commonly used to identify potential trend reversals and to generate buy and sell signals.
- Relative Strength Value (RSV) is a technical indicator used to measure the strength of a security's price relative to its previous trading periods. The RSV is calculated based on the closing price of a security over a specified period of time. It is expressed as a percentage and represents the ratio of the security's closing price to the highest high of the specified period. An RSV value of 100 indicates that the closing price is at the highest high of the specified period, while an RSV value of 0 indicates that the closing price is at the lowest low of the specified period. A high RSV value indicates that the security is trending upwards, while a low RSV value indicates that the security is trending downwards. Traders often use the RSV as an indicator of whether a security is overbought or oversold. An RSV value above 70 is generally considered overbought, while an RSV value below 30 is generally considered oversold. When the RSV value reaches these levels, traders may look for a reversal in the security's price trend.

![Technical Indicators](https://github.com/fola789/Amazon-Stock-Price-Forecasting-Using-LSTM-and-GAN/blob/master/technicalIndicators.png)

### Fourier Transform
The Fourier transform is a mathematical tool used to decompose a time series signal into its frequency components. In the context of stock prices, it can be used to identify cycles or periodic patterns in the data.

By decomposing the signal into its frequency components, we can identify dominant frequencies or cycles that are present in the data. These cycles or frequencies can then be used to make predictions about future stock prices.

For example, if we identify a dominant frequency of 30 days in the data, we might expect to see a similar pattern in the future. We could then use this information to make predictions about the direction of future stock prices.

![Fourier Transform](https://github.com/fola789/Amazon-Stock-Price-Forecasting-Using-LSTM-and-GAN/blob/master/fourierTransform.png)