import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    prices=[]
    for quote in quotes:
        _, _, _, price = getDataPoint(quote)
        prices.append(price)

    result=sum(prices)
    """
    Quoted ABC at (bid:120.48, ask:121.2 , price:120.84 )
    Quoted DEF at (bid:117.87, ask:121.68, price:119.775)
    ----------------------------------------------------
                       238.35      242.88        240.615
    """
    self.assertEqual(result, 240.615, "Total Price")



  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    prices_bid=[]
    prices_ask=[]
    for quote in quotes:
      _, bid_price, ask_price, _ = getDataPoint(quote)
      prices_bid.append(bid_price)
      prices_ask.append(ask_price)

    sum_prices_bid=sum(prices_bid)  # 238.35
    sum_prices_ask=sum(prices_ask)  # 240.88

    """         
    Quoted ABC at (bid:120.48, ask:119.2 , price:120.84 ) 
    Quoted DEF at (bid:117.87, ask:121.68, price:119.775)
    ----------------------------------------------------
                       238.35      240.88        240.615
    """


    self.assertGreater(sum_prices_bid, sum_prices_ask, "Bid Price should be greater than Ask Price")


  def test_getDataPoint_Ratio_ABC_over_DEF(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price_a=0
    price_b=0

    for quote in quotes:
        stock, _, _, price = getDataPoint(quote)
        if stock == 'ABC':
          price_a=price
        elif stock == 'DEF':
          price_b=price

    result=getRatio(price_a,price_b)          

    """         
    Quoted ABC at (bid:120.48, ask:119.2 , price:119.84 ) 
    Quoted DEF at (bid:117.87, ask:121.68, price:119.775)
    ----------------------------------------------------
                       238.35      240.88        239.615

    Ratio ABC:DEF =1.000542684199541
    """

    self.assertEqual(round(result,8), round(1.000542684199541,8), "Ratio ABC:DEF")



  def test_getDataPoint_Ratio_None(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price_a=0
    price_b=0

    for quote in quotes:
        stock, _, _, price = getDataPoint(quote)
        if stock == 'ABC':
          price_a=price
        elif stock == 'DEF':
          price_b=price

    result=getRatio(price_a,price_b)          

    """         
    Quoted ABC at (bid:120.48, ask:119.2 , price:119.84 ) 
    Quoted DEF at (bid:117.87, ask:121.68, price:119.775)
    ----------------------------------------------------
                       238.35      240.88        239.615

    Ratio ABC:DEF =1.000542684199541
    """

    self.assertEqual(result ,None, "Ratio ABC:DEF is None")






if __name__ == '__main__':
    unittest.main()
