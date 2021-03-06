<?php require_once('lib/DongDB.class.php');
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
$db = new DongDB();
$db->createDong($db, $email);
?>
