# Assignment 1: Secure User Profile & Access Control System

# Project Overview
This project implements a secure system to manage user identity and profile data, incorporating encryption for sensitive fields.



# Technology Stack
Backend: Python, Flask, Flask-JWT-Extended
Database: SQLite (persisted)
Frontend: React (Vite)
Security: JWT Authentication, AES Encryption
Version Control: Git & GitHub


# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py


# frontend
cd frontend
npm install
npm run dev


# API Documentation

Method ,  Endpoint   , Description 
post   ,  /register  , register a new user
post   ,  /login     , authenicate user and return  JWT 
get    ,  /profile   , fetch user profile 

# Database Schema
User Table

id – Integer (Primary Key)
username – String
password_hash – String
aadhaar_encrypted – Text (AES encrypted)


# AI-Assisted Tasks

AI tools (ChatGPT) were used during development to:

Design and implement the Flask backend with JWT authentication.
Add password hashing and AES-based Aadhaar encryption/decryption.
Create REST APIs for registration, login, and profile retrieval.
Assist in building the React frontend (login, registration, dashboard).
Debug backend–frontend integration issues and improve UI styling.

# Effectiveness Score

Score: 4 / 5

Justification:
AI tools helped speed up development and reduce boilerplate code, especially for backend security and frontend integration. Some debugging and UI refinements still required manual effort.