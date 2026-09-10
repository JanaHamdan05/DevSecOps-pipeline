from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Jana", "role": "intern"},
    {"id": 2, "name": "Admin", "role": "admin"}
]


@app.route("/")
def home():
    return jsonify({
        "message": "Secure DevSecOps Application",
        "status": "running"
    })


@app.route("/users")
def get_users():
    return jsonify(users)


@app.route("/user")
def get_user():
    username = request.args.get("username")

    for user in users:
        if user["name"].lower() == username.lower():
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
