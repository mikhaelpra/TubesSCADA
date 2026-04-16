// [STUDENT]
// Minggu 1:
// - Ambil data point dari backend dan tampilkan ke layar
//
// Minggu 2:
// - Hubungkan tombol OPEN/CLOSE ke endpoint command
//
// Minggu 3:
// - Ambil dan tampilkan alarm serta SOE
//
// Minggu 5:
// - Tambahkan trend sederhana jika historian sudah siap
//
// Minggu 6:
// - Pastikan state GUI konsisten saat demo
/*async function init() {
  const pointsEl = document.getElementById("points");
  pointsEl.innerHTML = "Implementasi mahasiswa diperlukan.";
}
init();
*/




async function loadPoints() {
  try {
    const res = await fetch("/points");
    const data = await res.json();

    const container = document.getElementById("points");

    let html = "";

    for (const key in data) {
      html += `
        <div class="point">
          <strong>${key}</strong>: ${data[key].value}
        </div>
      `;
    }

    container.innerHTML = html;

  } catch (err) {
    console.error("Error ambil data:", err);
  }
}

// refresh tiap 1 detik
setInterval(loadPoints, 1000);