from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "
        "img-src 'self'; "
        "font-src 'self'; "
        "connect-src 'self'; "
        "frame-ancestors 'none'; "
        "base-uri 'self'; "
        "form-action 'self'"
    )
    response.headers["Permissions-Policy"] = (
        "geolocation=(), microphone=(), camera=()"
    )
    response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
    response.headers["Server"] = ""

    return response

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
    
@app.route("/search")
def search_user():
    username = request.args.get("username")

    return jsonify({
        "username": username,
        "message": "Search executed"
    })
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
