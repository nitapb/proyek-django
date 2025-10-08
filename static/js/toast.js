function showToast(title, message, type = 'pink', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Hapus semua class warna dulu
    toastComponent.classList.remove(
        'bg-pink-100', 'border-pink-300', 'text-pink-800',
        'bg-green-100', 'border-green-400', 'text-green-800',
        'bg-red-100', 'border-red-400', 'text-red-800',
        'bg-gray-100', 'border-gray-300', 'text-gray-800'
    );

    // Warna sesuai tipe
    if (type === 'success') {
        toastComponent.classList.add('bg-green-100', 'border-green-400', 'text-green-800');
        toastComponent.style.border = '1px solid #86efac';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-100', 'border-red-400', 'text-red-800');
        toastComponent.style.border = '1px solid #fca5a5';
    } else if (type === 'pink') {
        toastComponent.classList.add('bg-pink-100', 'border-pink-300', 'text-pink-800');
        toastComponent.style.border = '1px solid #f9a8d4';
    } else {
        toastComponent.classList.add('bg-gray-100', 'border-gray-300', 'text-gray-800');
        toastComponent.style.border = '1px solid #d1d5db';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Animasi muncul
    toastComponent.classList.remove('opacity-0', 'translate-y-10');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    // Hilang setelah durasi tertentu
    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-10');
    }, duration);
}