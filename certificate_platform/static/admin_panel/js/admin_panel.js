document.addEventListener('DOMContentLoaded', function() {
    // Neon Hover Effects
    document.querySelectorAll('.btn, .card').forEach(el => {
        el.classList.add('neon-hover');
        el.addEventListener('mouseenter', () => el.classList.add('neon-glow'));
        el.addEventListener('mouseleave', () => el.classList.remove('neon-glow'));
    });

    // Theme Toggle
    const themeToggle = document.createElement('button');
    themeToggle.textContent = 'Toggle Theme';
    themeToggle.className = 'btn btn-primary position-fixed';
    themeToggle.style.top = '10px';
    themeToggle.style.right = '10px';
    document.body.appendChild(themeToggle);
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('light-theme');
        localStorage.setItem('theme', document.body.classList.contains('light-theme') ? 'light' : 'dark');
    });
    if (localStorage.getItem('theme') === 'light') {
        document.body.classList.add('light-theme');
    }

    // Animated Count Up Widgets
    function countUp(element, start, end, duration) {
        let startTime = null;
        function step(timestamp) {
            if (!startTime) startTime = timestamp;
            const progress = Math.min((timestamp - startTime) / duration, 1);
            element.textContent = Math.floor(progress * (end - start) + start);
            if (progress < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
    }
    document.querySelectorAll('.card-text.display-4').forEach(el => {
        const endValue = parseInt(el.textContent);
        el.textContent = '0';
        countUp(el, 0, endValue, 2000);
    });

    // Live Glowing Clock
    const clock = document.createElement('div');
    clock.className = 'position-fixed neon-glow';
    clock.style.bottom = '20px';
    clock.style.left = '20px';
    clock.style.padding = '10px';
    clock.style.background = '#0F52BA';
    clock.style.borderRadius = '8px';
    document.body.appendChild(clock);
    function updateClock() {
        const now = new Date();
        clock.textContent = now.toLocaleTimeString();
    }
    updateClock();
    setInterval(updateClock, 1000);

    // Toast Notifications for Form Submission
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const toast = document.createElement('div');
            toast.className = 'toast align-items-center position-fixed';
            toast.style.bottom = '20px';
            toast.style.right = '20px';
            toast.innerHTML = `
                <div class="d-flex">
                    <div class="toast-body">Admin action successful!</div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
                </div>
            `;
            document.body.appendChild(toast);
            new bootstrap.Toast(toast).show();
            setTimeout(() => toast.remove(), 3000);
        });
    });

    // Interactive Filters for Reports
    const filterForm = document.querySelector('form[method="get"]');
    if (filterForm) {
        filterForm.addEventListener('change', () => {
            filterForm.submit(); // Auto-submit on filter change
        });
    }

    // QR Code Scanning
    const qrInput = document.querySelector('#qr_image');
    const certificateIdInput = document.querySelector('#id_certificate_id');
    const qrPreview = document.querySelector('#qr-preview');
    if (qrInput && certificateIdInput) {
        qrInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const img = new Image();
                    img.src = e.target.result;
                    img.onload = () => {
                        qrPreview.innerHTML = `<img src="${img.src}" alt="QR Code Preview" class="img-thumbnail" style="max-width: 200px;">`;
                        const canvas = document.createElement('canvas');
                        const ctx = canvas.getContext('2d');
                        canvas.width = img.width;
                        canvas.height = img.height;
                        ctx.drawImage(img, 0, 0, img.width, img.height);
                        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
                        const code = jsQR(imageData.data, imageData.width, imageData.height);
                        if (code) {
                            certificateIdInput.value = code.data;
                            certificateIdInput.classList.add('is-valid');
                        } else {
                            certificateIdInput.classList.add('is-invalid');
                            const toast = document.createElement('div');
                            toast.className = 'toast align-items-center position-fixed';
                            toast.style.bottom = '20px';
                            toast.style.right = '20px';
                            toast.innerHTML = `
                                <div class="d-flex">
                                    <div class="toast-body">Invalid QR code!</div>
                                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
                                </div>
                            `;
                            document.body.appendChild(toast);
                            new bootstrap.Toast(toast).show();
                            setTimeout(() => toast.remove(), 3000);
                        }
                    };
                };
                reader.readAsDataURL(file);
            }
        });
    }
});