class StockSpan:
    def __init__(self, price: int, prev=None, span: int = 1):
        self.price = price
        self.prev = prev
        self.span = span


class StockSpanner:
    def __init__(self, head: StockSpan = None):
        self.head = head


    def next(self, price: int) -> int:
        print(f"Today's price: {price}")
        newSpan = StockSpan(price)
        current = self.head

        # Update the stack.
        if self.head == None:
            self.head = newSpan
        # Remaining cases must check all the span's before hand (and combine them if necessary) to see if their prices will align. So that means combining elements
        elif price >= self.head.price:
            self.head.span += 1
            self.head.price = price
        else:
            newSpan.prev = self.head
            self.head = newSpan
        
        return self.head.span

    
    # Record another day within the stock span. Resets if new price is less than the head
    def _next(self, price: int) -> int:
        print(f"Today's price: {price}")
        newNode = StockSpan(price)

        # Add a new node to the (empty) stack.
        if self.head != None:
            newNode.prev = self.head
        self.head = newNode

        max_span = 0
        current = self.head
        # Find the longest consecutive span.
        while current != None:
            print("Analysing new span")

            # Find the length of the span being occupied by the <current> variable
            print(f"\n Comparing today's price to {current.price}")
            span = 0

            while (current != None) and (current.price <= price):
                print("Add one to the current span length")
                span += 1
                current = current.prev

            max_span = max(span, max_span)
            print(f"New max_span: {max_span}")

            if current != None:
                current = current.prev

        self.span = max_span
        print("\n")
        return self.span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


"""
Basially run nested while loops. 
One to record the largest span so far, and the span currently being measured. 
You need to analyse consecutive days.

To improve solution, maybe you can track the current span's price.
If the current span's price is less than the new price, then we need to recount. 
Otherwise, we can just add the new element to the stack and then return an incremented span.

Okay, even more insight has been gained into this poorly explained questions. 
A span MUST include today and consecutive days before hand. Makes it easie to complete. 
But it also makes it slightly stranger to optimise. 
"""
