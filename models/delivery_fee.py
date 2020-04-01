import math

class DeliveryFee:
    def __init__(self, data=[]):
        self.fees = data

    def get_delivery_fee(self, price):
        for fee in self.fees:
            transaction_volume = fee.get('eligible_transaction_volume')
            
            min_price = transaction_volume.get('min_price')
            max_price = transaction_volume.get('max_price') or math.inf 

            if max_price > price >= min_price:
                return fee.get('price')
        return 0