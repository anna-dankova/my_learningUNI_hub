// ============================================
// ČASTNI DEL 1: TO-DO LISTA (samo za opravila.php)
// ============================================
document.addEventListener("DOMContentLoaded", function () {
  const addBtn = document.getElementById("addBtn");
  const taskInput = document.getElementById("taskInput");
  const taskList = document.getElementById("taskList");
  const doneCount = document.getElementById("doneCount");
  const openCount = document.getElementById("openCount");

  if (addBtn && taskInput && taskList) {
    addBtn.addEventListener("click", function () {
      const taskText = taskInput.value.trim();

      if (taskText === "") {
        alert("Please enter a task!");
        return;
      }

      const li = document.createElement("li");
      li.className = "list-group-item d-flex align-items-center gap-2";

      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.className = "form-check-input";

      const span = document.createElement("span");
      span.textContent = taskText;
      span.className = "flex-grow-1";

      const deleteBtn = document.createElement("button");
      deleteBtn.textContent = "Delete";
      deleteBtn.className = "btn btn-danger btn-sm";

      checkbox.addEventListener("change", function () {
        if (checkbox.checked) {
          span.style.textDecoration = "line-through";
          span.style.color = "gray";
        } else {
          alert(
            "This task was already completed. It will become active again.",
          );
          span.style.textDecoration = "none";
          span.style.color = "";
        }
        updateCounter();
      });

      deleteBtn.addEventListener("click", function () {
        li.remove();
        updateCounter();
      });

      li.appendChild(checkbox);
      li.appendChild(span);
      li.appendChild(deleteBtn);
      taskList.appendChild(li);

      taskInput.value = "";
      updateCounter();
    });

    taskInput.addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        addBtn.click();
      }
    });
  }

  function updateCounter() {
    if (!taskList) return;
    const allTasks = taskList.querySelectorAll('input[type="checkbox"]');
    let done = 0;
    allTasks.forEach(function (cb) {
      if (cb.checked) done++;
    });
    if (doneCount) doneCount.textContent = done;
    if (openCount) openCount.textContent = allTasks.length - done;
  }
});

// ============================================
// ČASTNI DEL 2: PIŠKOTKI (deluje na VSEH straneh)
// ============================================
function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  document.cookie = `${name}=${value}; expires=${date.toUTCString()}; path=/`;
}

function getCookie(name) {
  const cookies = document.cookie.split(";");
  for (let c of cookies) {
    c = c.trim();
    if (c.startsWith(name + "=")) {
      return c.substring(name.length + 1);
    }
  }
  return null;
}

function showCookieBanner() {
  const banner = document.getElementById("cookie-banner");
  if (banner) banner.classList.remove("hidden");
}

function hideCookieBanner() {
  const banner = document.getElementById("cookie-banner");
  if (banner) banner.classList.add("hidden");
}

function applySettings() {
  let barva = getCookie("barvaOzadja");
  let uporabnik = getCookie("uporabnikStrani");

  if (!barva) barva = "#ffffff";
  if (!uporabnik) uporabnik = "anonimen";

  document.body.style.backgroundColor = barva;

  document
    .querySelectorAll(" footer, table, body")
    .forEach((el) => (el.style.background = barva));

  const displayEl = document.getElementById("prikaz-uporabnika");
  if (displayEl) displayEl.textContent = uporabnik;

  const barvaInput = document.getElementById("barva");
  const uporabnikInput = document.getElementById("uporabnik");
  if (barvaInput) barvaInput.value = barva;
  if (uporabnikInput) uporabnikInput.value = uporabnik;
}

document.addEventListener("DOMContentLoaded", function () {
  const consent = getCookie("cookieConsent");
  if (!consent) {
    showCookieBanner();
  }

  const acceptBtn = document.getElementById("accept-cookies");
  const declineBtn = document.getElementById("decline-cookies");

  if (acceptBtn) {
    acceptBtn.addEventListener("click", function () {
      setCookie("cookieConsent", "accepted", 365);
      hideCookieBanner();
    });
  }

  if (declineBtn) {
    declineBtn.addEventListener("click", function () {
      setCookie("cookieConsent", "declined", 365);
      hideCookieBanner();
    });
  }

  const shraniBtn = document.getElementById("shraniBtn");
  const barvaInput = document.getElementById("barva");
  const uporabnikInput = document.getElementById("uporabnik");

  if (shraniBtn) {
    shraniBtn.addEventListener("click", function () {
      setCookie("barvaOzadja", barvaInput.value, 365);
      setCookie("uporabnikStrani", uporabnikInput.value, 365);
      applySettings();
    });
  }

  applySettings();
});
