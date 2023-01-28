
"""
Restaurant Model
"""
import time
from datetime import datetime
from utils import *
class Restaurant():

	def __init__(self, name, pincode_reachs, food_item, food_price, quantity, stars=0):
		self.name =  name
		self.pincode_reachs = pincode_reachs
		self.food_item =food_item
		self.food_price = food_price
		self.quantity = quantity
		self.stars = stars  # rating stars

	def save(self):
		RestaurantDB[self.name] = self

	def serializer(self):
		return {
			"name": self.name,
			"pincode_reachs": self.pincode_reachs,
			"food_item": self.food_item,
			"food_price": self.food_price,
			"quantity": self.quantity,
			"stars": self.stars
		}

