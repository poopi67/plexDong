<?php
// Handles the connection to the SQLite3 database and displaying the Dong size based on the user's email input
class DongDB extends SQLite3
{
  private $email;
  // Handles the connection to the database
  function __construct()
  {
    // This is the default location of the tautulli.db file, you may need to make a copy/hardlink as the default permissions of this directory may prevent it
    // from being usable.
    $this->open('tautulliEX.db');
  }
  // Handles the displaying of the Dong based on the db and email parameters
  function createDong($db, $email)
  {
    // Display the total watch count from session_history from the given email and where the paused counter is 0 (to prevent duplicate entries)
    $statement= $db->prepare("SELECT COUNT(*) as count FROM session_history WHERE user = :user;");
    $statement->bindValue(':user', $email);
    $result = $statement->execute();
    while ($table = $result->fetchArray(SQLITE3_ASSOC)) {
      // If the posted email is set and the count of results is greater than 0, proceed. This may be broken, some users are not displaying anything. Will fix if I feel like it in the future.
      $count = $table['count'];
      if (isset($email) && $count > 0) {
        echo $email . ',' . ' your current play count is: ' . '<b>' . $count . '</b><br />';
        echo "Therefore, your SCHLONG size is: <br />";
        // Gets the total watch amount and divides it by 5 then displays the, uh, shaft using the newCount number with "="'s
        $newCount = round($count / 5);
        echo "8". str_repeat("=", $newCount) . "D";
      } else {
        echo "You entered an email that is not tied to a Plex account. Redirecting you back to the previous page.<br />";
        header("refresh:5;url=/index.html");
      }
    }
  }

  function displayAll($db)
  {
    $stmt = $db->prepare("SELECT user, COUNT(*) as count FROM session_history GROUP BY user ORDER BY count DESC;");
    $result = $stmt->execute();
    echo "<ol>";
    while ($table = $result->fetchArray(SQLITE3_ASSOC)) {
      $user = $table['user'];
      $count = $table['count'];
      $newCount = round($count / 5);
      echo "<li>" . $user . " with <b>" . $count . "</b> plays " . "</li><br />" . "8" . str_repeat("=", $newCount) . "D";
    }
    echo "</ol>";
  }
}
