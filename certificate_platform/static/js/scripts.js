document.addEventListener('DOMContentLoaded', function() {
    // Add yellow glow to interactive elements
    document.querySelectorAll('.navbar-brand, .nav-link, .btn, .card').forEach(el => {
        el.classList.add('yellow-glow');
    });

    // Theme toggle (white/yellow to dark mode)
    const toggleButton = document.createElement('button');
    toggleButton.textContent = 'Toggle Theme';
    toggleButton.className = 'btn btn-secondary position-fixed';
    toggleButton.style.bottom = '20px';
    toggleButton.style.left = '20px';
    document.body.appendChild(toggleButton);
    toggleButton.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('theme', document.body.classList.contains('dark-mode') ? 'dark' : 'white');
    });
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode');
    }

    // Show toasts for alerts
    document.querySelectorAll('.alert').forEach(alert => {
        const toast = document.createElement('div');
        toast.className = `toast align-items-center ${alert.classList.contains('alert-success') ? 'bg-success' : 'bg-danger'} text-white`;
        toast.style.bottom = '20px';
        toast.style.right = '20px';
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">${alert.textContent}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;
        document.body.appendChild(toast);
        new bootstrap.Toast(toast).show();
        setTimeout(() => toast.remove(), 3000);
        alert.remove();
    });
});