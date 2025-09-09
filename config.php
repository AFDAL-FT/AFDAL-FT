<?php
// auth.php - File untuk menangani autentikasi
include 'config.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['login'])) {
        $email = sanitize_input($_POST['inputEmailAddress']);
        $password = sanitize_input($_POST['inputPassword']);
        
        // Query untuk memeriksa user
        $stmt = $conn->prepare("SELECT id, password, name FROM users WHERE email = ?");
        $stmt->execute([$email]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);
        
        if ($user && password_verify($password, $user['password'])) {
            // Login berhasil
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['user_name'] = $user['name'];
            redirect('index.html');
        } else {
            // Login gagal
            $error = "Email atau password salah!";
        }
    }
}
?>