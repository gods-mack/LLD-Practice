"""Storage Models and utils"""
from collections import defaultdict

UserDB = {}
RestaurantDB = {}
ReviewDB = {}
RatingDB = defaultdict(list)
OrderHistoryDB = defaultdict(list)
User_sessions = []

# class CurrentUser():
# 	user = None
# 	def __init__(self):
# 		return self.user

# 	@classmethod
# 	def create_session(self, user_obj):
# 		self.user = user_obj


# def login(phone):
# 	if phone in UserDB:
# 		import pdb; pdb.set_trace()	
# 		#CURRENT_USER = UserDB[phone]
# 		CurrentUser().create_session(user_obj)

# 		return "OK"
# 	return "error"


