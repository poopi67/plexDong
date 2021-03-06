<?php ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL); ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>PLEX PP</title>
</head>
<body>
  <form action="displayValues.php" method="post">
    <label for="email">Email:</label><br>
    <input type="text" id="email" name="email"><br>
    <input type="submit" value="Submit">
  </form>
</body>
</html>
