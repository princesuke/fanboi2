<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
    <link rel="stylesheet" href="${request.tagged_static_path('fanboi2:static/stylesheets/app.css')}">
    <link rel="shortcut icon" href="${request.tagged_static_path('fanboi2:static/favicon.ico')}">
    <title>Fanboi Channel</title>
</head>
<body id="${request.route_name}">
    <header id="header">
        <div class="container">
            <h1 class="brand"><a href="/">Fanboi Channel</a></h1>
        </div>
    </header>

    ${self.body()}

    <footer id="footer">
        <div class="container">
            All contents are responsibilty of its posters.<br>
            Fanboi2 is an open-source project. <a href="http://github.com/pxfs/fanboi2">Fork me</a>.
        </div>
    </footer>
</body>
</html>