class StockNode:
    def __init__(self, price: int, next = None):
        self.price = price
        self.next = next

class StockSpanner:
    

    def __init__(self, head: StockNode = None, tail: StockNode = None, span: int = 0):
        self.head = head
        self.tail = tail
        self.span = span
    
    # Record another day within the stock span. Resets if new price is less than the head
    def next(self, price: int) -> int:
        self.span = 0
        current = self.head
        newNode = StockNode(price)
        if self.head == None:
            self.head = newNode
        
        while current != None:
            if current.price <= price:
                self.span += 1
        
        self.span = new_span
        return self.span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)



'''Bakersly, stack the data until 
    def __init__(self):
        #collection - holds the daily stock prices
        #need to go over entire dataset most likely
        #optimise by checking yesterday's span and today's price
        # if span resets, then we can just clear data and continue
'''