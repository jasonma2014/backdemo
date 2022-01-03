import datetime
import os.path
import sys

import backtrader as bt


if __name__ == "__main__":
    cerebro = bt.Cerebro()

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, "./datas/orcl-1995-2014.txt")

    # Create a data feed
    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        # Do not pass values before this date
        fromdate=datetime.datetime(2000, 1, 1),
        # Do not pass values after this date
        todate=datetime.datetime(2000, 12, 31),
        reverse=False)

    # Add data to cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    print("Starting portfolio value: %.2f" % cerebro.broker.get_value())
    cerebro.run()
    print("final Portfolio value: %.2f" % cerebro.broker.get_value())

