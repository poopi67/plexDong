<?php
class DongDB extends SQLite3
{
  private $email;
  function __construct()
  {
    // This is the default location of the tautulli.db file, you may need to make a copy/hardlink as the default permissions of this directory may prevent it
    // from being usable.
    $this->open('/opt/Tautulli/tautulli.db');
  }
  // Handles the displaying of the Dong based on the db and email parameters
  function createDong($db, $email)
  {
    $this->email = $email;
    // Display the total watch count from session_history from the given email and where the paused counter is 0 (to prevent duplicate entries)
    $statement= $db->prepare("SELECT COUNT(*) as count FROM session_history WHERE user = :user AND paused_counter = 0;");
    $statement->bindValue(':user', $email);
    $result = $statement->execute();
    while ($table = $result->fetchArray(SQLITE3_ASSOC)) {
      // If the count of results is greater than 0, proceed. This may be broken, some users are not displaying anything. Will fix if I feel like it in the future.
      if ($table['count'] > 0) {
        $count = $table['count'];
        echo $email . ',' . ' your current play count is: ' . '<b>' . $count . '</b><br />';
        echo "Therefore, your SCHLONG size is: <br />";
        // Gets the total watch amount and divides it by 5, then appends the new amount with the corresponding number of "="'s
        $newCount = round($count / 5);
        echo "8". str_repeat("=", $newCount) . "D";
      } else {
        echo "You entered an email that is not tied to a Plex account.<br />";
      }
    }
  }
}

?>
