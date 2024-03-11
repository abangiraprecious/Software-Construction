<?php

class Authentication {
    // connection to the database connection 
    private $db; 

    public function __construct($db) {
        $this->db = $db; // Storing  the database connection
    }