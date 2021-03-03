<?php include 'lib/ConnectDB.class.php'; ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>YOUR PEENER SIZE</title>
  </head>
  <body>

  </body>
</html>
<?php
$email = htmlspecialchars($_POST['email']);
$db = new ConnectDB();
// Display all sqlite tables
    $statement= $db->prepare("SELECT COUNT(*) as count FROM session_history WHERE user = :user AND paused_counter = 0;");
    $statement->bindValue(':user', $email);
    $result = $statement->execute();
    // $data = $result->fetchAll();
    while ($table = $result->fetchArray(SQLITE3_ASSOC)) {
        $count = $table['count'];
        echo $email . ',' . ' your current play count is: ' . '<b>' . $table['count'] . '</b><br />';
    }
    echo "Therefore, your SCHLONG size is: <br />";
    $newCount = round($count / 5);
    echo "8". str_repeat("=", $newCount) . "D";

// "SELECT COUNT(*) as count FROM session_history WHERE user_id = 20078290 AND paused_counter = 0;"

?>
