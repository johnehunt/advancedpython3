# Now import the Ariadne elements
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
# import PLAYGROUND_HTML, this is a useful tool for writing,
# testing and learning about our GraphQL API.
# It provides a web application front end to allow you to
# run graphQL queries against your sever.
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify

# Holds the resolvers
from model import query, mutation

# Setups up the schema with type definitions for
# GraphQL to process. gql validates the schema and
# schema is then make executable
type_defs = gql(load_schema_from_path("./schema.graphql"))
schema = make_executable_schema(type_defs, query, mutation)

# Initialise Flask
app = Flask(__name__)


# Set up path mapping for simple hello world response
# Useful for testing
@app.route('/')
def hello_world():
	return 'Hello, World!'


# Sets up the URL for the GraphiQL playground application
# Used with GET HTTP request Method
@app.route("/graphql", methods=["GET"])
def graphql_playground():
	"""Serve GraphiQL playground"""
	return PLAYGROUND_HTML, 200


# GraphQL (single) end point. It will be used
# for all GraphQL queries and mutations
# By convention is is also /graphql but it
# uses the POST HTTP Request method.
@app.route("/graphql", methods=["POST"])
def graphql_server():
	# Get the JSON request submitted via POST
	data = request.get_json()

	# Pass request data along with schema and
	# original request to graphql_sync to work out
	# which resolver function to call
	success, result = graphql_sync(
			schema,
			data,
			context_value=request,
			debug=app.debug
	)

	# If all ok return result and status code
	status_code = 200 if success else 400
	return jsonify(result), status_code


if __name__ == '__main__':
	app.run(debug=True)
