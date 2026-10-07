<?php include 'header.php'; ?>

<main class="flex-grow-1">
<section class="container mt-5">
    
    <?php
    $errors = [];
    $success = '';
    
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $name = trim($_POST['name'] ?? '');
        $email = trim($_POST['email'] ?? '');
        $phone = trim($_POST['phone'] ?? '');
        $message = trim($_POST['message'] ?? '');
        
        
        if (empty($name)) $errors[] = 'Name required';
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = 'Invalid email';
        if (empty($phone)) $errors[] = 'Phone number rquired';
        if (strlen($message) < 10) $errors[] = 'Message is too short';
        
        if (empty($errors)) {
            $success = 'Your message has been sent! Hvala!';
            $name = $email = $phone = $message = ''; 
        }
    }
    ?>

    <div class="card page-card glass-effect" style="min-height: 70vh;">
        <div class="page-header">
            <h1 class="mb-0">Contact with me</h1>
        </div>
        
        <div class="card-body p-5">
            
            <?php if ($success): ?>
                <div class="alert alert-success text-center mb-4" role="alert">
                    <?= htmlspecialchars($success) ?>
                </div>
            <?php endif; ?>
            
            <?php if ($errors): ?>
                <div class="alert alert-danger">
                    <ul class="mb-0">
                        <?php foreach ($errors as $error): ?>
                            <li><?= htmlspecialchars($error) ?></li>
                        <?php endforeach; ?>
                    </ul>
                </div>
            <?php endif; ?>
            
            <form method="POST" novalidate>
                <div class="mb-4">
                    <label for="name" class="form-label fw-bold mb-2">Name and surname</label>
                    <input type="text" class="form-control" id="name" name="name" 
                    value="<?= htmlspecialchars($_POST['name'] ?? '') ?>" required>
                </div>
                
                <div class="mb-4">
                    <label for="email" class="form-label fw-bold mb-2">E-mail</label>
                    <input type="email" class="form-control" id="email" name="email" 
                        value="<?= htmlspecialchars($_POST['email'] ?? '') ?>" required>
                </div>
                
                <div class="mb-4">
                    <label for="phone" class="form-label fw-bold mb-2">Phone</label>
                    <input type="tel" class="form-control" id="phone" name="phone" 
                        value="<?= htmlspecialchars($_POST['phone'] ?? '') ?>" required>
                </div>
                
                <div class="mb-4">
                    <label for="message" class="form-label fw-bold mb-2">Message</label>
                    <textarea class="form-control" id="message" name="message" rows="6" 
                            required><?= htmlspecialchars($_POST['message'] ?? '') ?></textarea>
                </div>
                
                <div class="text-center">
                    <button type="submit" class="btn btn-primary btn-lg px-5">Send</button>
                </div>
            </form>
            
        </div>
    </div>

</section>
</main>

<?php include 'footer.php'; ?>
