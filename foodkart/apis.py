from restaurant import Restaurant
from user import User
from utils import *

def login(phone):
	if phone in UserDB:
		User_sessions.append(UserDB[phone])
		return "OK"
	return "error"


def register_user(self, name, phone, sex, pincode):
	u = User(name, phone, sex, pincode)
	u.save_user()
	return "OK"


def register_rest( name, pincode_reachs, food_item, food_price, quantity, stars=0):
	try:
		rest_obj = Restaurant(name, pincode_reachs, food_item, food_price, quantity, stars)
		rest_obj.save()
	except Exception as ex:
		return str(ex)
	return "OK"


def show_restaurant( filter):
	restaurants = RestaurantDB.values()
	reverse = False if filter == "price" else True
	key = lambda x: x.food_price if filter == "price" else x.stars
	sorted_restaurants = sorted(restaurants, key=key, reverse=reverse)
	sorted_restaurants = [rest.serializer() for rest in sorted_restaurants]
	return sorted_restaurants


def update_quantity(rest_name, new_quantity):
	rest = RestaurantDB.get(rest_name)
	if rest:
		rest.quantity += new_quantity
		rest.save()
	else:
		return "Restaurant Doesn't Exist"
	return "OK"


def create_review(rest_name, rating, msg=""):
	restaurant = RestaurantDB.get(rest_name)
	if not restaurant:
		return "Restaurant not found"

	ReviewDB[rest_name] = {"stars": rating, "comment": msg}

	RatingDB[rest_name].append(float(rating))
	total_rating = sum(RatingDB[rest_name]) / len(RatingDB[rest_name])
	restaurant.stars = total_rating
	restaurant.save()
	return "OK"


def place_order(rest_name, quantity):
    restaurant = RestaurantDB.get(rest_name)
    if not restaurant:
        return "Restaurant Doesn't Exist"

    logged_in_user = User_sessions[-1]
    if logged_in_user.pincode not in restaurant.pincode_reachs:
        return "Couldn't Deliver at your pincode"

    if quantity > restaurant.quantity:
        return "Not enough quantity"

    restaurant.quantity -= quantity
    restaurant.save()
    logged_in_user.update_order_history(rest_name, quantity)
    return "Order Placed Successfully"
