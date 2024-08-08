<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = htmlspecialchars($_POST['name']);
    $message = htmlspecialchars($_POST['message']);

    // 데이터베이스에 연결합니다 (MySQL 예제)
    $conn = new mysqli('localhost', 'username', 'password', 'guestbook');

    if ($conn->connect_error) {
        die("연결 실패: " . $conn->connect_error);
    }

    $sql = "INSERT INTO entries (name, message) VALUES ('$name', '$message')";
    if ($conn->query($sql) === TRUE) {
        echo "새 기록이 성공적으로 추가되었습니다.";
    } else {
        echo "오류: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
    header("Location: index.html");
    exit();
}
?>
