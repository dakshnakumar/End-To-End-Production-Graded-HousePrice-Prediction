from abc import ABC,abstractmethod

#step1: implement statergy
class PaymentMethod(ABC):
    @abstractmethod    
    def pay():
        pass

#step2: implement conceret statergy
class CreditcardPayment(PaymentMethod):
    def pay(self,amount):
        return f'paying {amount} using creditcard'
    

class PaypalPayment(PaymentMethod):
    def pay(self,amount):
        return f'paying {amount} using paypal' 
    
class BitcoinPayment(PaymentMethod):
    def pay(self,amount):
        return f'paying {amount} using bitcoin'

# step3: implement context   
class ShoppingCart():
    def __init__(self,payment_method: PaymentMethod):
        self.payment_method = payment_method
    
    def checkout(self,amount):
        return self.payment_method.pay(amount)
        

if __name__ == "__main__":
    
    creditcard = ShoppingCart(CreditcardPayment())
    paypal = ShoppingCart(PaypalPayment())
    bitcoin = ShoppingCart(BitcoinPayment())

    print(creditcard.checkout(100))
    print(paypal.checkout(200))
    print(bitcoin.checkout(400))