<?php

class Authentication {
    private $db; 

    public function __construct($db) {
        $this->db = $db; 
    }

    public function register($username, $password, $email) {

        if (!$this->isValidPassword($password)) {
            return "Password does not meet complexity requirements";
        } 

        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        try {
            $stmt = $this->db->prepare("INSERT INTO users (username, password, email) VALUES (?, ?, ?)");
            $stmt->bind_param("sss", $username, $hashedPassword, $email);
            $stmt->execute();

            return "User registered successfully";

        } catch (Exception $e) {
            return "Registration failed: " . $e->getMessage(); 
        }
    }

    private function isValidPassword($password) {
        return preg_match('/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/', $password);
    }

}
?>