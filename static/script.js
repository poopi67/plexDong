window.onload = function() {
  document.getElementById("showBrd").addEventListener("click", function() {
      let x = document.getElementById('ldrBrd');
      let button = document.getElementById("showBrd");
      if (x.style.display === "none") {
          x.style.display = "block";
          button.innerHTML = "Hide Leaderboard";
      } else {
          x.style.display = "none";
          button.innerHTML = "Show Leaderboard";
      }
  });
}