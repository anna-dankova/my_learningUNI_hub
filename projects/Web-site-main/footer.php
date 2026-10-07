<footer class="bg-dark text-white mt-5 py-4">
    <div class="container">
        <ul class="list-inline text-end mb-0">
            <?php foreach ($links as $name => $url): ?>
                <li class="list-inline-item">
                    <a href="<?php echo $url; ?>">
                        <?php echo $name; ?>
                    </a>
                </li>
            <?php endforeach; ?>
        </ul>
    </div>
</footer>

<script src="lib/bootstrap-5.3.8-dist/js/bootstrap.bundle.min.js"></script>
<script src="js/skripta.js"></script>
</body>
</html>
