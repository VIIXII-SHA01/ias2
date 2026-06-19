// PayPal Login Page - JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');
    const loginButton = document.querySelector('.btn-login');
    const languageToggle = document.getElementById('languageToggle');
    const languageMenu = document.getElementById('languageMenu');

    // Language Selector
    if (languageToggle && languageMenu) {
        languageToggle.addEventListener('click', function(e) {
            e.preventDefault();
            languageMenu.classList.toggle('active');
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!languageToggle.contains(e.target) && !languageMenu.contains(e.target)) {
                languageMenu.classList.remove('active');
            }
        });

        // Language option clicks
        const langOptions = document.querySelectorAll('.lang-option');
        langOptions.forEach(option => {
            option.addEventListener('click', function(e) {
                e.preventDefault();
                const lang = this.textContent.trim();
                languageToggle.querySelector('.lang-text').textContent = lang;
                languageMenu.classList.remove('active');
            });
        });
    }

    // Real-time validation
    emailInput.addEventListener('blur', validateEmail);
    emailInput.addEventListener('input', function() {
        if (emailError.classList.contains('show')) {
            validateEmail();
        }
    });

    passwordInput.addEventListener('blur', validatePassword);
    passwordInput.addEventListener('input', function() {
        if (passwordError.classList.contains('show')) {
            validatePassword();
        }
    });

    // Form Submission
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // Clear previous errors
        clearErrors();

        // Validate both fields
        const emailValid = validateEmail();
        const passwordValid = validatePassword();

        if (emailValid && passwordValid) {
            submitLogin();
        }
    });

    // Email Validation
    function validateEmail() {
        const email = emailInput.value.trim();

        if (!email) {
            showError(emailError, 'Email or mobile number is required');
            emailInput.classList.add('error');
            return false;
        }

        // Email format validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        // Phone format validation (basic)
        const phoneRegex = /^[\d\s\-\+\(\)]{10,}$/;

        if (!emailRegex.test(email) && !phoneRegex.test(email)) {
            showError(emailError, 'Please enter a valid email or mobile number');
            emailInput.classList.add('error');
            return false;
        }

        clearError(emailError);
        emailInput.classList.remove('error');
        return true;
    }

    // Password Validation
    function validatePassword() {
        const password = passwordInput.value;

        if (!password) {
            showError(passwordError, 'Password is required');
            passwordInput.classList.add('error');
            return false;
        }

        if (password.length < 6) {
            showError(passwordError, 'Password must be at least 6 characters');
            passwordInput.classList.add('error');
            return false;
        }

        clearError(passwordError);
        passwordInput.classList.remove('error');
        return true;
    }

    // Show Error
    function showError(element, message) {
        element.textContent = message;
        element.classList.add('show');
    }

    // Clear Error
    function clearError(element) {
        element.textContent = '';
        element.classList.remove('show');
    }

    // Clear All Errors
    function clearErrors() {
        clearError(emailError);
        clearError(passwordError);
        emailInput.classList.remove('error');
        passwordInput.classList.remove('error');
    }

    // Submit Login
    async function submitLogin() {
        loginButton.disabled = true;
        loginButton.classList.add('loading');

        try {
            const email = emailInput.value.trim();
            const password = passwordInput.value;

            // Simulate API call (replace with actual endpoint)
            const response = await fetch('#', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email: email,
                    password: password
                })
            }).catch(() => {
                // Demo mode - simulate successful login
                return {
                    ok: true,
                    json: () => Promise.resolve({ success: true })
                };
            });

            if (response.ok) {
                const data = await response.json();

                if (data.success) {
                    // Success - redirect to dashboard
                    showSuccess('Login successful! Redirecting...');
                    setTimeout(() => {
                        // window.location.href = '/dashboard';
                        console.log('Logging in as:', email);
                    }, 1500);
                } else {
                    showError(emailError, data.message || 'Login failed');
                }
            }
        } catch (error) {
            console.error('Login error:', error);
            showError(emailError, 'An error occurred. Please try again.');
        } finally {
            loginButton.disabled = false;
            loginButton.classList.remove('loading');
        }
    }

    // Show Success Message
    function showSuccess(message) {
        const successDiv = document.createElement('div');
        successDiv.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #27ae60;
            color: white;
            padding: 15px 20px;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
            z-index: 10000;
            animation: slideIn 0.3s ease-out;
        `;
        successDiv.textContent = message;
        document.body.appendChild(successDiv);

        setTimeout(() => {
            successDiv.remove();
        }, 3000);
    }

    // Keyboard Navigation
    emailInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            passwordInput.focus();
        }
    });

    passwordInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            loginForm.dispatchEvent(new Event('submit'));
        }
    });

    // Focus management
    emailInput.addEventListener('focus', function() {
        this.classList.remove('error');
    });

    passwordInput.addEventListener('focus', function() {
        this.classList.remove('error');
    });

    // Add CSS for animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .input-field.error {
            border-color: #e74c3c !important;
            background-color: #fef5f5 !important;
        }

        .input-field.error:focus {
            box-shadow: 0 0 0 3px rgba(231, 76, 60, 0.1) !important;
        }
    `;
    document.head.appendChild(style);
});

    // Language Selector Toggle
    if (languageBtn) {
        languageBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            languageMenu.classList.toggle('active');
        });

        // Close menu when clicking outside
        document.addEventListener('click', function() {
            languageMenu.classList.remove('active');
        });

        // Language option clicks
        const languageOptions = document.querySelectorAll('.language-option');
        languageOptions.forEach(option => {
            option.addEventListener('click', function(e) {
                e.preventDefault();
                const lang = this.textContent;
                languageBtn.querySelector('.language-text').textContent = lang;
                languageMenu.classList.remove('active');
            });
        });
    }

    // Email Input Validation
    emailInput.addEventListener('blur', function() {
        validateEmail();
    });

    emailInput.addEventListener('input', function() {
        if (emailError.textContent) {
            emailError.textContent = '';
        }
    });

    // Password Input Validation
    passwordInput.addEventListener('blur', function() {
        validatePassword();
    });

    passwordInput.addEventListener('input', function() {
        if (passwordError.textContent) {
            passwordError.textContent = '';
        }
    });

    // Form Submission
    loginForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Reset error messages
        emailError.textContent = '';
        passwordError.textContent = '';

        // Validate inputs
        if (!validateEmail() || !validatePassword()) {
            return;
        }

        // Disable button and show loading
        loginBtn.disabled = true;
        loadingSpinner.classList.add('active');

        try {
            // Simulate API call
            const email = emailInput.value.trim();
            const password = passwordInput.value;

            // Send login request
            const response = await loginUser(email, password);

            if (response.success) {
                // Show success message and redirect
                showSuccessMessage('Login successful! Redirecting...');
                
                // Simulate redirect after 1.5 seconds
                setTimeout(() => {
                    // window.location.href = '/dashboard'; // Uncomment for actual redirect
                    console.log('Redirect to dashboard');
                }, 1500);
            } else {
                // Show error message
                showErrorMessage(response.message || 'Login failed. Please try again.');
            }
        } catch (error) {
            console.error('Login error:', error);
            showErrorMessage('An error occurred. Please try again later.');
        } finally {
            // Re-enable button and hide loading
            loginBtn.disabled = false;
            loadingSpinner.classList.remove('active');
        }
    });

    // Email Validation Function
    function validateEmail() {
        const email = emailInput.value.trim();
        
        if (!email) {
            emailError.textContent = 'Please enter your email or phone number.';
            emailInput.classList.add('invalid');
            return false;
        }

        // Check if it's a valid email or phone number
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const phoneRegex = /^[\d\s\-\+\(\)]{10,}$/;

        if (!emailRegex.test(email) && !phoneRegex.test(email)) {
            emailError.textContent = 'Please enter a valid email address or phone number.';
            emailInput.classList.add('invalid');
            return false;
        }

        emailInput.classList.remove('invalid');
        return true;
    }

    // Password Validation Function
    function validatePassword() {
        const password = passwordInput.value;
        
        if (!password) {
            passwordError.textContent = 'Please enter your password.';
            passwordInput.classList.add('invalid');
            return false;
        }

        if (password.length < 6) {
            passwordError.textContent = 'Password must be at least 6 characters.';
            passwordInput.classList.add('invalid');
            return false;
        }

        passwordInput.classList.remove('invalid');
        return true;
    }

    // Show Success Message
    function showSuccessMessage(message) {
        const successDiv = document.createElement('div');
        successDiv.className = 'success-message';
        successDiv.textContent = message;
        successDiv.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #27ae60;
            color: white;
            padding: 15px 20px;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
            z-index: 1001;
            animation: slideInRight 0.3s ease-out;
        `;
        document.body.appendChild(successDiv);

        setTimeout(() => {
            successDiv.remove();
        }, 3000);
    }

    // Show Error Message
    function showErrorMessage(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-notification';
        errorDiv.textContent = message;
        errorDiv.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #e74c3c;
            color: white;
            padding: 15px 20px;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
            z-index: 1001;
            animation: slideInRight 0.3s ease-out;
        `;
        document.body.appendChild(errorDiv);

        setTimeout(() => {
            errorDiv.remove();
        }, 4000);
    }

    // Mock API Call (Replace with actual API call)
    async function loginUser(email, password) {
        return new Promise((resolve) => {
            // Simulate API response delay
            setTimeout(() => {
                // Mock validation - In a real app, this would be server-side
                if (email && password) {
                    resolve({
                        success: true,
                        message: 'Login successful',
                        data: {
                            email: email
                        }
                    });
                } else {
                    resolve({
                        success: false,
                        message: 'Invalid credentials'
                    });
                }
            }, 1500); // Simulate network delay
        });
    }

    // Clear error on focus
    emailInput.addEventListener('focus', function() {
        this.classList.remove('invalid');
    });

    passwordInput.addEventListener('focus', function() {
        this.classList.remove('invalid');
    });

    // Prevent autofill security issues
    emailInput.addEventListener('change', function() {
        validateEmail();
    });

    passwordInput.addEventListener('change', function() {
        validatePassword();
    });

    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + Enter to submit
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            loginForm.dispatchEvent(new Event('submit'));
        }
    });
});

// Add CSS animation styles dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    .form-input.invalid {
        border-color: #e74c3c !important;
        background-color: #fadbd8 !important;
    }

    @media (prefers-color-scheme: dark) {
        .form-input.invalid {
            background-color: #5a2c2c !important;
        }
    }
`;
document.head.appendChild(style);