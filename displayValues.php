<?php require_once('lib/DongDB.class.php'); ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <link rel="shortcut icon" type="image/x-icon" href="/assets/dong.png" />
  <title>PlexDong: <?php  echo $_POST['email']; ?></title>
</head>
<body>
  <?php
  $email = htmlspecialchars(strtolower($_POST['email']));
  $db = new DongDB();
  $db->createDong($db, $email);
  ?>
  <body>
    <br />
    
    <button type="button" name="button" id="button" onclick="dispLeader();">View Leaderboard</button>
    <p id="leaderBrd"> </p>
    <script type="text/javascript">
    function dispLeader() {
      let leaderBrd = document.getElementById('leaderBrd');
      leaderBrd.innerHTML = "<?php $db->displayAll($db);?>";
      let button = document.getElementById('button');
      var x = leaderBrd;
      if (x.style.display === "none" || x.style.display === "") {
        x.style.display = "block";
        button.innerHTML = "Hide Leaderboard";
      } else {
        x.style.display = "none";
        button.innerHTML = "View Leaderboard";
      }
    }
    </script>
  </body>
  </html>
