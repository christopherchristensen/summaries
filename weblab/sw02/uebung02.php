<?php  session_start();
$host = 'localhost';
$user = 'root';
$pwd = 'somepass';
$db = 'motd';
$conn = new mysqli($host, $user, $pwd, $db);

if($conn) {
	if(!isset($_SESSION['visitor'])) {
                $_SESSION['visitor'] = 1;
        } else {
                $temp = $_SESSION['visitor'];
                $_SESSION['visitor'] = ($temp+1);
                }
        $id = $_SESSION['visitor'];
        $sql = "SELECT * FROM motd WHERE id=$id";
        $result = $conn->query($sql);
        $row = $result->fetch_assoc();
        echo $row['messages'];
} else if(!$conn) {
        echo 'connection failed';
}



?>