<?php header("Content-Type: application/json");
$host = 'localhost';
$user = 'root';
$pwd = 'somepass';
$db = 'motd';
$conn = new mysqli($host, $user, $pwd, $db);

if($conn) {
	$sql = "SELECT * FROM motd ORDER BY RAND() LIMIT 1";
        $result = $conn->query($sql);
        $row = $result->fetch_assoc();
} else if(!$conn) {
        echo 'connection failed';
}

echo json_encode($row['messages']);

?>