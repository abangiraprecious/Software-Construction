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