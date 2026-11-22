
# Strategy Pattern for Payment Processing

# Payment Strategy
class PaymentStrategy:
    def pay(self, amount):
        pass


# Credit Card Payment
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid Rs.", amount, "using Credit Card.")


# UPI Payment
class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid Rs.", amount, "using UPI.")


# PayPal Payment
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid Rs.", amount, "using PayPal.")


# Payment Processor
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_payment_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
print("Select Payment Method:")
print("1. Credit Card")
print("2. UPI")
print("3. PayPal")

choice = 2
amount = 1500

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = UPIPayment()
elif choice == 3:
    strategy = PayPalPayment()
else:
    print("Invalid choice!")
    strategy = None

if strategy is not None:
    processor = PaymentProcessor(strategy)
    processor.process_payment(amount)
