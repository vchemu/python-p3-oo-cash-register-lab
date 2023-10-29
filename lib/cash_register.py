#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.existing_transactions = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(title)
    self.existing_transactions.append({"title": title, "price": price, "quantity": quantity})

  def apply_discount(self):
    if self.discount > 0:
      self.total = int(self.total * ((100 - self.discount) / 100)) #self.discount / 100
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if not self.existing_transactions:
      return "There are no transactions to void."
    self.total -= (self.existing_transactions[-1]["price"] * self.existing_transactions[-1]["quantity"]
    )
    for _ in range(self.existing_transactions[-1]["quantity"]):
      self.items.pop()
    self.existing_transactions.pop()

