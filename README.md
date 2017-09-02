# IQfeed API example
IQfeed is a financial data providor, I used the data for futures trading (NQ), my trading platform was in MATLAB so i used python only for fetching the data from IQfeed and sent it to matlab using TCP.
In this repo I give the code sample for connecting to IQfeed requesting a feed and parsing it.
IQfeed api may be updated, I used it in 2016, the expiry of the future should also be updated before running.

The code connects to IQfeed parse data of bid, ask, last, bidsize, asksize, buys and sells.

