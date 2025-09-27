// Main JavaScript for Aether Agribot Dashboard

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading animation to buttons on form submission
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
                submitBtn.disabled = true;
                
                // Re-enable after 10 seconds as fallback
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                }, 10000);
            }
        });
    });

    // File upload preview functionality
    function handleFilePreview(fileInput, previewContainer, previewImage) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    previewImage.src = e.target.result;
                    previewContainer.style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Initialize file previews if elements exist
    const fileInputs = {
        'imageFile': { container: 'imagePreview', image: 'previewImg' },
        'leafFile': { container: 'leafPreview', image: 'leafPreviewImg' }
    };

    Object.entries(fileInputs).forEach(([inputId, elements]) => {
        const input = document.getElementById(inputId);
        const container = document.getElementById(elements.container);
        const image = document.getElementById(elements.image);
        
        if (input && container && image) {
            handleFilePreview(input, container, image);
        }
    });

    // Add fade-in animation to cards on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    // Observe all cards and service elements
    document.querySelectorAll('.card, .service-card').forEach(el => {
        observer.observe(el);
    });

    // Navbar active link highlighting
    const currentLocation = location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
        }
    });

    // Add success animation for successful operations
    window.showSuccessAnimation = function(element) {
        element.style.transform = 'scale(1.05)';
        element.style.transition = 'transform 0.3s ease';
        setTimeout(() => {
            element.style.transform = 'scale(1)';
        }, 300);
    };

    // Error handling utility
    window.showError = function(message, container) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'alert alert-danger alert-dismissible fade show';
        errorDiv.innerHTML = `
            <strong>Error!</strong> ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        container.insertBefore(errorDiv, container.firstChild);
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            if (errorDiv.parentNode) {
                errorDiv.remove();
            }
        }, 5000);
    };

    // Success message utility
    window.showSuccess = function(message, container) {
        const successDiv = document.createElement('div');
        successDiv.className = 'alert alert-success alert-dismissible fade show';
        successDiv.innerHTML = `
            <strong>Success!</strong> ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        container.insertBefore(successDiv, container.firstChild);
        
        // Auto-dismiss after 3 seconds
        setTimeout(() => {
            if (successDiv.parentNode) {
                successDiv.remove();
            }
        }, 3000);
    };
});

// Utility function to format confidence percentage
function formatConfidence(confidence) {
    return `${(confidence * 100).toFixed(1)}%`;
}

// Utility function to determine color based on result type
function getResultColor(label, type = 'detection') {
    if (type === 'weed') {
        return label.toLowerCase() === 'weed' ? '#FF9800' : '#4CAF50';
    } else if (type === 'disease') {
        const isHealthy = label.toLowerCase().includes('healthy') || 
                         label.toLowerCase().includes('normal');
        return isHealthy ? '#4CAF50' : '#E65100';
    }
    return '#4CAF50'; // default green
}
