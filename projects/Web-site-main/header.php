<?php include 'menu.php'; ?>
<!DOCTYPE html>
<html lang="sl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seminarska naloga</title>
    <link rel="stylesheet" href="lib/bootstrap-5.3.8-dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="css/stil.css?v=3">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #797979 !important;">

    <div class="container">
        <a class="navbar-brand" href="index.php">Moja stran</a>
        <span id="prikaz-uporabnika"></span>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <?php foreach ($links as $name => $url): ?>
                    <li class="nav-item">
                        <a class="nav-link <?php echo (basename($_SERVER['PHP_SELF']) == $url) ? 'active' : ''; ?>"
                            href="<?php echo $url; ?>">
                            <?php echo $name; ?>
                        </a>
                    </li>
                <?php endforeach; ?>
            </ul>
        </div>
    </div>
</nav>

