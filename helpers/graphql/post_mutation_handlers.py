from graphql import GraphQLError
from posts.models import Post
from users.models import User
from django.core.exceptions import ValidationError
from re import findall


def string_validator(input, title):
	if not findall('[a-zA-Z]', input):
		raise ValueError(f'{title} is empty!')

def mutation_handler(mutation_object, id=None):
	'''
	# Mutation Handler
	 
	mutation_object must contain the input object passed from the mutation function
	for this function to handler the object creation at the database.
	'''
	
	# set the mutation object in a readable variable 
	input = mutation_object
	
	# initiate post object model
	post = Post.objects.get(pk=id) if id else Post()
	
	try:
		post.content = input.content
		post.user = User.objects.get(id=input.user_id)
		post.save()
		
		return post
		
	except Exception as e:
		raise GraphQLError(e)
	

	