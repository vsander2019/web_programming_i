<<<<<<< HEAD
<html>
<head>
  <title>JQuery Demo Page</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script>
  $(document).ready(function() {
    $.getJSON("http://dev-web-vanessasanders.pythonanywhere.com/static/data.json", function(result) {
        $("#content").append("<ul>");
        $.each(result, function(i, field) {
            $("#content").append("<li>" + field["fruit"] + "</li>");
        });
        $("#content").append("</ul>");
    });
  })
  </script>
</head>
<body>
Hello from the sandbox.
<hr/>
<div id="content"></div>
<hr/>
</body>
=======
<html>
<head>
  <title>JQuery Demo Page</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script>
  $(document).ready(function() {
    $.getJSON("http://dev-web-drdelozier.pythonanywhere.com/static/data.json", function(result) {
        $("#content").append("<ul>");
        $.each(result, function(i, field) {
            $("#content").append("<li>" + field["fruit"] + "</li>");
        });
        $("#content").append("</ul>");
    });
  })
  </script>
</head>
<body>
Hello from the sandbox.
<hr/>
<div id="content"></div>
<hr/>
</body>
>>>>>>> b2693012a90410afe5705293c2236191d9d3b702
</html>