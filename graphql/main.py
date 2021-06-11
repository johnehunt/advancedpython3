from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
from ariadne.constants import PLAYGROUND_HTML

# Holds the resolvers
from model import query, mutation


type_defs = gql(load_schema_from_path("./schema.graphql"))
schema = make_executable_schema(type_defs, query, mutation)

# Initialise Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    """Serve GraphiQL playground"""
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == '__main__':
    app.run(debug=True)
