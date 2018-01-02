'''
Created on 1 Jan 2018

@author: cmt
'''

import ccxt

print 'Start'
print 'Supported exchanges:'
print(ccxt.exchanges)

hitbtc = ccxt.hitbtc({'verbose': False})
hitbtc_markets = hitbtc.load_markets()

print('HITBTC markets:')
print('hitbtc:\n', hitbtc.id, hitbtc_markets)

print('All sympols')
for symbol in hitbtc.symbols:
    print symbol
    
print('Order book for ', hitbtc.symbols[0])
print(hitbtc.fetch_order_book(hitbtc.symbols[0]))

print 'End'

if __name__ == '__main__':
    pass