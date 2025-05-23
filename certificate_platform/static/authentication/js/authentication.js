document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.btn, .card').forEach(el => {
        el.classList.add('neon-glow');
    });
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', (e) => {
            const toast = document.createElement('div');
            toast.className = 'toast align-items-center position-fixed';
            toast.style.bottom = '20px';
            toast.style.right = '20px';
            toast.innerHTML = `
                <div class="d-flex">
                    <div class="toast-body">Action successful!</div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
                </div>
            `;
            document.body.appendChild(toast);
            new bootstrap.Toast(toast).show();
            setTimeout(() => toast.remove(), 3000);
        });
    }
});