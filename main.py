import backtrader as bt

if __name__ == "__main__":
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000.0)

    print("Starting portfolio value: %.2f" % cerebro.broker.get_value())
    cerebro.run()
    print("final Portfolio value: %.2f" % cerebro.broker.get_value())

    print("final")
