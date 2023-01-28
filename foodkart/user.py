"""
User model
"""
from datetime import datetime
from utils import UserDB, OrderHistoryDB
class User():
    def __init__(self, name, phone, sex, pincode):
        self.name = name
        self.phone = phone
        self.sex = sex
        self.pincode = pincode

    def save_user(self):
        phone = self.phone
        UserDB[phone] = self

    def update_order_history(self, rest_name, quantity):
        OrderHistoryDB[self.phone].append({
          "rest_name":rest_name,
          "quantity":quantity,
          "ordered_on":str(datetime.now())
        })

    def get_past_orders(self):
        orders = OrderHistoryDB[self.phone]
        return orders
