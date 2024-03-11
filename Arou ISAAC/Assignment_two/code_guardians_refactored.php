<?php

class Authentication {
    // connection to the database connection 
    private $db; 

    public function __construct($db) {
        $this->db = $db; // Storing  the database connection
    }

    public function register($username, $password, $email) {
        // Input validation & sanitization 
        if (!$this->isValidPassword($password)) {
            return "Password does not meet complexity requirements";
        } 
        // Hashing the password for secure storage
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        try {
            $stmt = $this->db->prepare("INSERT INTO users (username, password, email) VALUES (?, ?, ?)");
            $stmt->bind_param("sss", $username, $hashedPassword, $email);
            $stmt->execute();

            return "User registered successfully";

        } catch (Exception $e) {
            // Handling database errors gracefully
            return "Registration failed: " . $e->getMessage(); 
        }
    }

    // another method for login
    public function login($username, $password) {
        try {
            // Fetching user details from the database
            $stmt = $this->db->prepare("SELECT id, password FROM users WHERE username = ?");
            $stmt->bind_param("s", $username);
            $stmt->execute();
            $result = $stmt->get_result();