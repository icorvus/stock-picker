

def stock_picker(stock_prices):
    local_max = 0
    # First value is best day to buy, second is best day to sell
    best_days = [0, 0] 
    for buy in range(len(stock_prices)):
        for sell in range(buy + 1, len(stock_prices)):
            if stock_prices[sell] - stock_prices[buy] >= local_max:
                local_max = stock_prices[sell] - stock_prices[buy]
                best_days = [buy, sell]
    return best_days


def main():
    print(stock_picker([17,3,6,9,15,8,6,1,10]))
    print(stock_picker([17,3,6,9,15,8,6,10,1]))
    print(stock_picker([17,3,6,9,15,8,6,10,12]))

if __name__ == "__main__":
    main()