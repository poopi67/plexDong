<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>PLEX PP</title>
</head>
<body>
  <form action="displayValues.php" method="post">
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" required><br>
    <input type="submit" value="Submit">
  </form>
</body>
</html>
