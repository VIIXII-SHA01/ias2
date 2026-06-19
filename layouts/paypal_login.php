<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PayPal Login</title>
    <link rel="stylesheet" href="../css/paypal_login.css">
</head>
<body>
    <div class="page-wrapper">
        <!-- Main Container -->
        <div class="login-page">

            <!-- Login Section -->
            <div class="login-section">
                <form id="loginForm" class="login-form">
                    <!-- Logo -->
                    <div class="paypal-logo">PayPal</div>
                    <!-- Email Input -->
                    <div class="form-field">
                        <input 
                            type="email"
                            id="email"
                            class="input-field"
                            autocomplete="email"
                            required
                        >
                        <label for="email" class="input-label">Email or mobile number</label>
                        <span class="error-message" id="emailError"></span>
                    </div>

                    <!-- Password Input -->
                    <div class="form-field">
                        <input 
                            type="password"
                            id="password"
                            class="input-field"
                            autocomplete="current-password"
                            required
                        >
                        <label for="password" class="input-label">Password</label>
                        <span class="error-message" id="passwordError"></span>
                    </div>

                    <!-- Forgot Password Link -->
                    <a href="#" class="forgot-password">Forgot your password?</a>

                    <!-- Login Button -->
                    <button type="submit" class="btn-login">Log In</button>

                    <!-- Sign Up Section -->
                    <div class="signup-section">
                        <p class="signup-text">Don't have an account? <a href="paypal_signup.php" class="signup-link">Sign Up</a></p>
                    </div>
                </form>
            </div>
        </div>

        <!-- Footer -->
        <footer class="footer">
            <div class="footer-content">
                <a href="#" class="footer-link">Contact Us</a>
                <a href="#" class="footer-link">Privacy</a>
                <a href="#" class="footer-link">Legal</a>
                <a href="#" class="footer-link">Policy Updates</a>
                <a href="#" class="footer-link">Worldwide</a>
            </div>
            <div class="language-selector">
                <button class="language-toggle" id="languageToggle">
                    <span class="flag">🇺🇸</span>
                    <span class="lang-text">English</span>
                    <span class="dropdown-icon">▼</span>
                </button>
                <div class="language-menu" id="languageMenu">
                    <a href="#" class="lang-option">English</a>
                    <a href="#" class="lang-option">Français</a>
                    <a href="#" class="lang-option">Español</a>
                    <a href="#" class="lang-option">中文</a>
                </div>
            </div>
        </footer>
    </div>

    <script src="../javascript/paypal_login.js"></script>
</body>
</html>
