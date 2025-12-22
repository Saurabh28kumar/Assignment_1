from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from models import db, User
from crypto_utils import encrypt_data, decrypt_data
from config import Config

auth_bp = Blueprint("auth", __name__)

# ---------------- REGISTER ----------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    encrypted_aadhaar = encrypt_data(
        data["aadhaar"],
        Config.ENCRYPTION_KEY
    )

    user = User(
        username=data["username"],
        password_hash=generate_password_hash(data["password"]),
        aadhaar_encrypted=encrypted_aadhaar
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


# ---------------- LOGIN ----------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password_hash, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    # JWT requires subject (identity) to be a STRING
    access_token = create_access_token(identity=str(user.id))

    return jsonify({"access_token": access_token}), 200


# ---------------- PROFILE ----------------
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    # Convert identity back to INTEGER
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)

    decrypted_aadhaar = decrypt_data(
        user.aadhaar_encrypted,
        Config.ENCRYPTION_KEY
    )

    return jsonify({
        "username": user.username,
        "aadhaar": decrypted_aadhaar
    }), 200
