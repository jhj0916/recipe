<?php
// 데이터베이스에 연결합니다 (MySQL 예제)
$conn = new mysqli('localhost', 'username', 'password', 'guestbook');

// 연결 상태를 확인합니다.
if ($conn->connect_error) {
    die("연결 실패: " . $conn->connect_error);
}

// SQL 쿼리를 작성합니다.
$sql = "SELECT name, message, created_at FROM entries ORDER BY created_at DESC";

// 쿼리를 실행합니다.
$result = $conn->query($sql);

// 쿼리 실행 결과를 확인합니다.
if ($result === FALSE) {
    die("쿼리 실행 실패: " . $conn->error);
}

// 결과가 있는지 확인합니다.
if ($result->num_rows > 0) {
    // 결과를 반복하여 출력합니다.
    while($row = $result->fetch_assoc()) {
        echo "<div class='entry'>";
        echo "<h3>" . htmlspecialchars($row['name']) . "</h3>";
        echo "<p>" . htmlspecialchars($row['message']) . "</p>";
        echo "<small>" . htmlspecialchars($row['created_at']) . "</small>";
        echo "</div>";
    }
} else {
    echo "방명록이 비어 있습니다.";
}

// 연결을 종료합니다.
$conn->close();
?>
