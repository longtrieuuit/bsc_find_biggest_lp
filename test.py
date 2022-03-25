from pancaketrade.network import Network
from decimal import Decimal

if __name__ == "__main__":
    net = Network(
            rpc='https://bsc-dataseed.binance.org/',
            wallet='...',
            min_pool_size_bnb=1,
            price_in_usd = True,
            secrets='....',
        )

    
    address = '0xA0A2eE912CAF7921eaAbC866c6ef6FEc8f7E90A4'
    
    (token_price,base_amount) ,base_token_address,value_lp = net.get_token_price(token_address=address)    
    print(token_price)
    

    LP = base_amount / Decimal(10 ** 18)
    if(base_token_address == "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"):
        bnb_price = net.get_bnb_price()
        LP = LP * bnb_price

    print(LP)
