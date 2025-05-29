const API = "http://127.0.0.1:8000";

async function callEndpoint(path, params = {}) {
  const url = new URL(API + path);
  Object.entries(params).forEach(([k,v]) => url.searchParams.set(k,v));
  const res = await fetch(url);
  return res.ok ? res.json() : { error: `${res.status} ${res.statusText}` };
}

function renderWeather(data) {
  if (data.error) return `<p class="result‑card">Error: ${data.error}</p>`;
  return `
    <div class="result‑card">
      <h3>${data.location}</h3>
      <p><strong>${data.temperature}°C</strong> — ${data.description}</p>
      <img src="http://openweathermap.org/img/w/${data.icon}.png" alt="" />
    </div>`;
}

function renderForecast(data) {
  if (data.error) return `<p class="forecast‑card">Error: ${data.error}</p>`;
  let html = `<div class="forecast‑grid">`;
  data.forecasts.forEach(day => {
    html += `
      <div class="forecast‑card">
        <strong>${day.date}</strong><br/>
        ${day.temperature}°C<br/>
        ${day.description}<br/>
        <img src="http://openweathermap.org/img/w/${day.icon}.png" alt="" />
      </div>`;
  });
  return html + `</div>`;
}

function renderHistory(list) {
  if (!list.length) return `<p>No history yet.</p>`;
  return list.map(item => `
    <div class="history‑item">
      [${item.timestamp.split("T")[0]}] ${item.location} (${item.type})<br/>
      ${JSON.stringify(item.data)}
    </div>`).join("");
}

document.addEventListener("DOMContentLoaded", () => {
  const out = document.getElementById("output");
  const hist = document.getElementById("history");

  document.getElementById("btnWeather").onclick = async () => {
    const loc = document.getElementById("locationInput").value.trim();
    out.innerHTML = renderWeather(await callEndpoint("/weather", { location: loc }));
  };

  document.getElementById("btnForecast").onclick = async () => {
    const loc = document.getElementById("locationInput").value.trim();
    out.innerHTML = renderForecast(await callEndpoint("/forecast", { location: loc }));
  };

  document.getElementById("btnHistory").onclick = async () => {
    const data = await callEndpoint("/history");
    hist.innerHTML = renderHistory(data.history);
  };

  document.getElementById("btnClear").onclick = async () => {
    await callEndpoint("/clear");
    hist.innerHTML = `<p>History cleared.</p>`;
  };

  document.getElementById("btnExport").onclick = () => {
    const fmt = document.getElementById("exportFormat").value;
    window.open(`${API}/export?format=${fmt}`, "_blank");
  };
});



