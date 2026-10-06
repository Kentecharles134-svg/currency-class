class Currency:
    USD_TO_CREDITS = 100

    def __init__(self, amount=0, currency_type="credits"):
        self.amount = float(amount)
        self.currency_type = currency_type.lower()

    def __str__(self):
        return f"{self.amount:.2f} {self.currency_type}"

    def __mul__(self, value):
        return Currency(self.amount * value, self.currency_type)

    def __truediv__(self, value):
        return Currency(self.amount / value, self.currency_type)

    def __iadd__(self, value):
        if isinstance(value, Currency):
            self.amount += value.amount
        else:
            self.amount += value
        return self

    def __isub__(self, value):
        if isinstance(value, Currency):
            self.amount -= value.amount
        else:
            self.amount -= value
        return self

    def __le__(self, other):
        if isinstance(other, Currency):
            return self.amount <= other.amount
        return self.amount <= other

    def __ge__(self, other):
        if isinstance(other, Currency):
            return self.amount >= other.amount
        return self.amount >= other

    def __int__(self):
        return int(self.amount)

    def __float__(self):
        return float(self.amount)

    def convert(self):
        if self.currency_type == "usd":
            converted_amount = self.amount * self.USD_TO_CREDITS
            return Currency(converted_amount, "credits")

        elif self.currency_type == "credits":
            converted_amount = self.amount / self.USD_TO_CREDITS
            return Currency(converted_amount, "usd")

        else:
            raise ValueError("Currency type must be 'usd' or 'credits'.")

    def can_afford(self, cost):
        if isinstance(cost, Currency):
            return self.amount >= cost.amount
        return self.amount >= cost


if __name__ == "__main__":
    wallet = Currency(500, "credits")

    print("Starting wallet:", wallet)

    wallet += 200
    print("After adding 200 credits:", wallet)

    wallet -= 100
    print("After spending 100 credits:", wallet)

    doubled = wallet * 2
    print("Wallet multiplied by 2:", doubled)

    divided = wallet / 2
    print("Wallet divided by 2:", divided)

    print("Wallet as integer:", int(wallet))
    print("Wallet as float:", float(wallet))

    usd_value = wallet.convert()
    print("Converted to USD:", usd_value)

    print("Can afford 300 credits:", wallet.can_afford(300))
    print("Wallet >= 500:", wallet >= 500)
    print("Wallet <= 1000:", wallet <= 1000)
