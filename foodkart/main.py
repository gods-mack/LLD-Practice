"""
FoodKart - food order service lLD (e.g Swiggy, Zomato)
"""
from utils import User_sessions
from apis import *
import json

"""
- Restaurant
  - name
  - address/pincode
  - pincodeItServe[]
  - menu{}

- User
  - phoneNumber
  - pincode/address
  - name
  - sex


- UserOrderHistory


- Review
  - rest_id
  - stars
  - comment_msg
"""

def main():
	u = User("manish", "7056008581", "M", "WF")
	u.save_user()
	u1 = User("LkhRaj", "12345", "M", "BF")
	u1.save_user()

	if login("7056008581") == "OK":
		print ("Logged in Successfully by -> {}\n".format((User_sessions[-1].name)))

	if login("12345") == "OK":
		print ("Logged in Successfully by -> {}\n".format((User_sessions[-1].name)))

	register_rest("BTF", ["HSR", "MRT", "BF"], "biryani", 280, 10, 3.8)
	register_rest("Meghna", ["HSR", "BF"], "biryani", 210, 10, 4)
	register_rest("Pind-Bloochi", ["HSR", "MRT", "BF"], "Daaru", 1200, 6, 2.9)
	register_rest("Mainland-China", ["MRT", "BF", "WF"], "Pronz", 450, 8, 3.7)
	register_rest("EatFit", ["HSR", "WF", "BF"], "thali", 249, 14, 2.7)
	
	print (place_order("BTF", 2))
	print (place_order("BTF", 3))
	create_review("EatFit", 4, "Good food")
	
	print (json.dumps(u1.get_past_orders(), indent=2))

	res = show_restaurant("price")
	# show as json response in order to make it more readable
	print (json.dumps(res, indent=2))


if __name__ == "__main__":
	main()
