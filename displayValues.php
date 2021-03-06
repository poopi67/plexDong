<?php require_once('lib/ConnectDB.class.php');
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL); ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>YOUR PLEXDONG SIZE</title>
  </head>
  <body>

  </body>
</html>
<?php
$email = htmlspecialchars(strtolower($_POST['email']));
$db = new ConnectDB();
// Display all sqlite tables
    $statement= $db->prepare("SELECT COUNT(*) as count FROM session_history WHERE user = :user AND paused_counter = 0;");
    $statement->bindValue(':user', $email);
    $result = $statement->execute();
    while ($table = $result->fetchArray(SQLITE3_ASSOC)) {
    // If the count of results is greater than 0, proceed. This may be broken, some users are not displaying anything. Will fix if I feel like it in the future.
      if ($table['count'] > 0) {
        $count = $table['count'];
        echo $email . ',' . ' your current play count is: ' . '<b>' . $table['count'] . '</b><br />';
        echo "Therefore, your SCHLONG size is: <br />";
        // Gets the total watch amount and divides it by 5, then appends the new amount with the corresponding number of "="'s
        $newCount = round($count / 5);
        echo "8". str_repeat("=", $newCount) . "D";
    } else {
      echo "You entered an email that is not tied to a Plex account.<br />";
    }
}

?>
