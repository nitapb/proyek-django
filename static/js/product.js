// === PRODUCT.JS ===
// Utility: ambil CSRF token dari cookie
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// --- STATE ---
let deleteId = null;

// === MEMUAT PRODUK ===
async function loadProducts() {
  const container = document.querySelector("#product-list");
  if (!container) return;

  container.innerHTML = `
    <div class="text-center text-pink-600 animate-pulse mt-8">Memuat produk...</div>
  `;

  try {
    const response = await fetch("/api/json/"); // endpoint dari urls.py
    if (!response.ok) throw new Error("Gagal fetch produk.");

    const products = await response.json();

    // Render produk ke halaman
    if (products.length === 0) {
      container.innerHTML = `
        <div class="text-center text-gray-500 mt-8">
          Belum ada produk 😢
        </div>`;
      return;
    }

    container.innerHTML = products.map(p => `
      <article class="bg-white rounded-lg border border-pink-200 hover:shadow-lg transition duration-300 overflow-hidden">
        <div class="aspect-[4/3] relative overflow-hidden">
          ${p.thumbnail
            ? `<img src="${p.thumbnail}" alt="${p.name}" class="w-full h-full object-cover">`
            : `<div class="w-full h-full bg-pink-100"></div>`}
        </div>
        <div class="p-5">
          <h3 class="text-lg font-semibold text-gray-800 mb-2 line-clamp-1">${p.name}</h3>
          <p class="text-pink-600 font-bold mb-2">Rp${p.price}</p>
          <p class="text-sm text-gray-500 mb-4">Kategori: ${p.category_display}</p>

          <div class="flex items-center justify-between pt-3 border-t border-gray-100">
            <a href="/products/${p.id}/" class="text-pink-600 hover:text-pink-700 font-medium text-sm transition">Detail</a>
            ${p.user_username === CURRENT_USER ? `
              <div class="flex space-x-2">
                <a href="/products/${p.id}/edit/" class="text-yellow-600 hover:text-yellow-700 text-sm transition">Edit</a>
                <button class="text-red-600 hover:text-red-700 text-sm transition delete-btn" data-id="${p.id}">Delete</button>
              </div>` : ""}
          </div>
        </div>
      </article>
    `).join("");

  } catch (err) {
    console.error(err);
    container.innerHTML = `
      <div class="text-center text-red-500 bg-pink-50 border border-pink-200 rounded-lg p-4 mt-8">
        Terjadi kesalahan saat memuat produk. Coba tekan tombol Refresh.
      </div>`;
  }
}

// === REFRESH PRODUK TANPA RELOAD ===
async function refreshProducts() {
  await loadProducts();
}

// === DELETE PRODUK (MODAL) ===
document.addEventListener("click", function (e) {
  if (e.target.classList.contains("delete-btn")) {
    deleteId = e.target.dataset.id;
    document.getElementById("delete-modal").classList.remove("hidden");
    document.getElementById("delete-modal").classList.add("flex");
  }
});

document.getElementById("cancel-delete").addEventListener("click", () => {
  document.getElementById("delete-modal").classList.add("hidden");
});

document.getElementById("confirm-delete").addEventListener("click", async () => {
  if (!deleteId) return;

  try {
    const response = await fetch(`/delete-product-ajax/${deleteId}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
    });

    const data = await response.json();
    if (data.status === "success") {
      showToast("Berhasil 💖", data.message, "success");
      await refreshProducts();
    } else {
      showToast("Gagal 💔", data.message, "error");
    }
  } catch (error) {
    showToast("Error 😢", "Terjadi kesalahan saat menghapus produk.", "error");
  }

  document.getElementById("delete-modal").classList.add("hidden");
  deleteId = null;
});

// === AUTO LOAD SAAT HALAMAN SIAP ===
document.addEventListener("DOMContentLoaded", loadProducts);