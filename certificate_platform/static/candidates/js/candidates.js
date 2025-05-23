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

    // Toast Notifications for Form Submission
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', (e) => {
            const toast = document.createElement('div');
            toast.className = 'toast align-items-center position-fixed';
            toast.style.bottom = '20px';
            toast.style.right = '20px';
            toast.innerHTML = `
                <div class="d-flex">
                    <div class="toast-body">Candidate action successful!</div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
                </div>
            `;
            document.body.appendChild(toast);
            new bootstrap.Toast(toast).show();
            setTimeout(() => toast.remove(), 3000);
        });
    }

    // File Upload Preview
    const fileInput = document.querySelector('input[type="file"]');
    if (fileInput) {
        fileInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const preview = document.createElement('div');
                    preview.innerHTML = `<p>Selected file: ${file.name}</p>`;
                    fileInput.parentElement.appendChild(preview);
                };
                reader.readAsDataURL(file);
            }
        });
    }
});