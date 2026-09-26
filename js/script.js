// js/script.js

// 🛍️ Product List
const items = [
  { id: 1, name: "Beverages", price: 35, image: "images/Beverages.jpg" },
  { id: 2, name: "Biscuits", price: 10, image: "images/Biscuits.jpg" },
  { id: 3, name: "Chocolates", price: 15, image: "images/Chocolates.jpg" },
  { id: 4, name: "Milk", price: 12, image: "images/Milk.jpg" },
  { id: 5, name: "Oils", price: 150, image: "images/Oils.jpg" },
  { id: 6, name: "Peanuts", price: 120, image: "images/Peanuts.jpg" },
  { id: 7, name: "Rice", price: 45, image: "images/Rice.jpg" },
  { id: 8, name: "Semolina", price: 80, image: "images/Semolina.jpg" },
  { id: 9, name: "Spices-Masalas", price: 20, image: "images/Spices-Masalas.png" },
  { id: 10, name: "Tomatoes", price: 25, image: "images/Tomatoes.jpg" },
  { id: 11, name: "Apples", price: 30, image: "images/Apples.jpg" }
];

// 🎯 DOM References
const productsDiv = document.getElementById("products");
let cart = JSON.parse(localStorage.getItem("cart")) || [];

// 📦 Display Products
function displayProducts(list) {
  productsDiv.innerHTML = "";
  list.forEach(item => {
    const div = document.createElement("div");
    div.className = "product";
    div.innerHTML = `
      <img src="${item.image}" alt="${item.name}" onerror="this.src='images/default.jpg'">
      <h3>${item.name}</h3>
      <p>₹${item.price.toFixed(2)}</p>
      <button onclick="addToCart(${item.id})">Add to Cart</button>
    `;
    productsDiv.append(div);
  });
}

// 🔍 Filter Products
function filterProducts() {
  const q = document.getElementById("search").value.toLowerCase();
  const filtered = items.filter(i => i.name.toLowerCase().includes(q));
  if (filtered.length === 0) {
    productsDiv.innerHTML = "<p>No products found 👀</p>";
  } else {
    displayProducts(filtered);
  }
}

// 💾 Save & Load Cart
function saveCart() {
  localStorage.setItem("cart", JSON.stringify(cart));
  renderCart();
}

// 🛒 Initialize Site
function init() {
  displayProducts(items);
  renderCart();
}

// ➕ Add to Cart
function addToCart(id) {
  const prod = items.find(i => i.id === id);
  const exist = cart.find(c => c.id === id);
  if (exist) {
    exist.qty++;
  } else {
    cart.push({ ...prod, qty: 1 });
  }
  saveCart();
}

// ❌ Remove from Cart
function removeFromCart(id) {
  cart = cart.filter(c => c.id !== id);
  saveCart();
}

// 🔁 Change Quantity
function changeQty(id, delta) {
  const prod = cart.find(c => c.id === id);
  prod.qty += delta;
  if (prod.qty <= 0) {
    removeFromCart(id);
  } else {
    saveCart();
  }
}

// 💳 Render Cart
function renderCart() {
  const container = document.getElementById("cart-items");
  container.innerHTML = "";

  if (cart.length === 0) {
    container.innerHTML = "<p>Your cart is feeling lonely 🛒</p>";
    document.getElementById("cart-total").innerText = "0.00";
    return;
  }

  let total = 0;
  cart.forEach(i => {
    total += i.price * i.qty;
    const p = document.createElement("p");
    p.innerHTML = `
      ${i.name} × ${i.qty}
      <button onclick="changeQty(${i.id}, -1)">−</button>
      <button onclick="changeQty(${i.id}, 1)">+</button>
      <button onclick="removeFromCart(${i.id})">✕</button>
    `;
    container.append(p);
  });

  document.getElementById("cart-total").innerText = total.toFixed(2);
}

// 🚀 Start the app when DOM is ready
document.addEventListener("DOMContentLoaded", init);
