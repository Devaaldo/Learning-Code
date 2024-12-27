// Inisialisasi peta dengan Leaflet
var map = L.map("map").setView([-6.1751, 106.865], 13); // Contoh koordinat (Jakarta)

// Tambahkan tile peta dari OpenStreetMap
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 18,
}).addTo(map);

// Contoh marker untuk area tertentu
var marker = L.marker([-6.1751, 106.865])
  .addTo(map)
  .bindPopup("Klik untuk melihat data penduduk.");

// Event listener untuk klik pada marker
marker.on("click", function () {
  // Panggil API Flask untuk mendapatkan data penduduk berdasarkan ID area
  fetch("/api/data_penduduk?id=1")
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        marker.bindPopup("Data tidak ditemukan").openPopup();
      } else {
        // Tampilkan data penduduk di popup
        marker
          .bindPopup(
            `Nama: ${data.nama}<br>Jumlah Penduduk: ${data.jumlah_penduduk}`
          )
          .openPopup();
      }
    })
    .catch((error) => console.error("Error:", error));
});
