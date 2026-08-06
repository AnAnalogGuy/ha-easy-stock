1| DOMAIN = "easy_stock"
2| 
3| CONF_SYMBOL = "symbol"
4| CONF_NAME = "name"
5| CONF_SCAN_INTERVAL = "scan_interval"
6| 
7| DEFAULT_SCAN_INTERVAL = 900  # 15 minutes
8| 
9| YAHOO_CHART_URL = (
10|     "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
11|-    "?range=1y&interval=1d&includePrePost=false"
11|+    "?range=1y&interval=1d&includePrePost=true"
12| )
13| 
14| YAHOO_CHART_URL_MINI = (
15|     "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
16|-    "?range=5d&interval=1d&includePrePost=false"
16|+    "?range=5d&interval=1d&includePrePost=true"
17| )
