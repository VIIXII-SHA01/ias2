document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input[type="email"], input[type="password"]');
    
    inputs.forEach(input => {
        const label = input.nextElementSibling;
        
        // Check on load if input has value
        if (input.value) {
            label.style.top = '-12px';
            label.style.fontSize = '12px';
            label.style.color = '#0260ca';
        }
        
        // On focus
        input.addEventListener('focus', function() {
            label.style.top = '-12px';
            label.style.fontSize = '12px';
            label.style.color = '#0260ca';
        });
        
        // On blur
        input.addEventListener('blur', function() {
            if (!input.value) {
                label.style.top = '16px';
                label.style.fontSize = '16px';
                label.style.color = '#767676';
            }
        });
        
        // On input (as user types)
        input.addEventListener('input', function() {
            if (input.value) {
                label.style.top = '-12px';
                label.style.fontSize = '12px';
                label.style.color = '#0260ca';
            } else {
                label.style.top = '16px';
                label.style.fontSize = '16px';
                label.style.color = '#767676';
            }
        });
    });
    
    // Fetch and populate country flags
    const countryDropdown = document.getElementById('country-flag');
    const languageLabel = document.querySelector('.language-label');
    const savedCountry = localStorage.getItem('selectedCountry') || '';
    
    fetch('https://restcountries.com/v3.1/all?fields=name,cca2,flags,idd')
        .then(response => response.json())
        .then(data => {
            // Sort countries by name
            data.sort((a, b) => a.name.common.localeCompare(b.name.common));
            
            // Populate dropdown
            data.forEach(country => {
                const option = document.createElement('option');
                option.value = country.cca2;
                option.textContent = `${country.flags.png} ${country.name.common}`;
                option.dataset.flag = country.flags.png;
                option.dataset.name = country.name.common;
                countryDropdown.appendChild(option);
            });
            
            // Set saved country if exists
            if (savedCountry) {
                countryDropdown.value = savedCountry;
                const selectedOption = countryDropdown.selectedOptions[0];
                if (selectedOption) {
                    languageLabel.textContent = selectedOption.dataset.name;
                    countryDropdown.textContent = selectedOption.dataset.flag;
                }
            }
        })
        .catch(error => console.error('Error fetching countries:', error));
    
    countryDropdown.addEventListener('change', function() {
        if (this.value) {
            const selectedOption = this.selectedOptions[0];
            const countryName = selectedOption.dataset.name;
            const countryFlag = selectedOption.dataset.flag;
            
            localStorage.setItem('selectedCountry', this.value);
            languageLabel.textContent = countryName;
            countryDropdown.textContent = countryFlag;
        }
    });
});
