<?php require_once('lib/DongDB.class.php'); ?>
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
$db = new DongDB();
$db->createDong($db, $email);
?>
