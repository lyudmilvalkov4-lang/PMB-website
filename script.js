const navToggle = document.querySelector(".nav-toggle");
const siteNav = document.querySelector(".site-nav");
const tonsInput = document.querySelector("#tons");
const capacitySelect = document.querySelector("#capacity");
const loadsOutput = document.querySelector("#loads");
const plannerNote = document.querySelector("#planner-note");
const prepareRequestButton = document.querySelector("#prepare-request");
const requestOutput = document.querySelector("#request-output");
const terminalImage = document.querySelector(".terminal-photo img");
const logoImages = document.querySelectorAll(".brand-mark img");
const revealSteps = document.querySelectorAll(".reveal-step");
const processNodes = document.querySelectorAll(".process-node");
const processCount = document.querySelector("#process-count");
const processTitle = document.querySelector("#process-title");
const processText = document.querySelector("#process-text");
const processMeter = document.querySelector(".process-meter span");

const processStepsData = [
  {
    title: "Heat & Transfer",
    text: "Base asphalt is transferred from service storage into the PMB plant through heated pumps and hot-oil jacketed piping."
  },
  {
    title: "Weigh & Feed",
    text: "Bitumen and polymer are weighed and introduced into the mixing system with controlled feeding, load cells, and agitation."
  },
  {
    title: "Mix & Mill",
    text: "Heated mixing tanks and the high-shear mill disperse polymer into the binder for target modification and particle-size control."
  },
  {
    title: "Circulate & Analyze",
    text: "Finished PMB is circulated, stored, and analyzed through certified laboratory testing before shipment documents are issued."
  }
];

function updateLoads() {
  if (!tonsInput || !capacitySelect || !loadsOutput || !plannerNote) return;
  const tons = Math.max(Number(tonsInput.value) || 0, 0);
  const capacity = Number(capacitySelect.value) || 24;
  const loads = Math.max(Math.ceil(tons / capacity), 1);
  loadsOutput.textContent = loads;
  plannerNote.textContent = `Based on ${tons || 0} tons and ${capacity}-ton trucks.`;
}

if (navToggle && siteNav) {
  navToggle.addEventListener("click", () => {
    const isOpen = siteNav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  siteNav.addEventListener("click", (event) => {
    if (event.target.matches("a")) {
      siteNav.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  });
}

if (tonsInput && capacitySelect) {
  tonsInput.addEventListener("input", updateLoads);
  capacitySelect.addEventListener("change", updateLoads);
  updateLoads();
}

if (terminalImage) {
  terminalImage.addEventListener("error", () => {
    terminalImage.style.display = "none";
  });
}

logoImages.forEach((image) => {
  image.addEventListener("error", () => {
    image.style.display = "none";
  });
});

if (prepareRequestButton && requestOutput) {
  prepareRequestButton.addEventListener("click", () => {
    const form = prepareRequestButton.closest("form");
    const [name, company, email] = Array.from(form.querySelectorAll("input")).map((field) => field.value.trim());
    const requestType = form.querySelector("select").value;
    const message = form.querySelector("textarea").value.trim();
    const subject = encodeURIComponent(`Polysan ${requestType}`);
    const body = encodeURIComponent([
      `Name: ${name || "Not provided"}`,
      `Company: ${company || "Not provided"}`,
      `Email: ${email || "Not provided"}`,
      `Request type: ${requestType}`,
      "",
      message || "Please share product, tonnage, timing, project location, and specifications."
    ].join("\n"));

    requestOutput.classList.add("show");
    requestOutput.innerHTML = `Request prepared. <a href="mailto:sales@polysan.com?subject=${subject}&body=${body}">Open email draft</a>`;
  });
}

if (revealSteps.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
      }
    });
  }, { threshold: 0.32 });

  revealSteps.forEach((step) => observer.observe(step));
}

if (processNodes.length && processCount && processTitle && processText && processMeter) {
  processNodes.forEach((node) => {
    node.addEventListener("click", () => {
      const index = Number(node.dataset.step);
      const step = processStepsData[index];
      if (!step) return;

      processNodes.forEach((item) => item.classList.remove("active"));
      node.classList.add("active");
      processCount.textContent = `Step ${index + 1} of ${processStepsData.length}`;
      processTitle.textContent = step.title;
      processText.textContent = step.text;
      processMeter.style.width = `${((index + 1) / processStepsData.length) * 100}%`;
    });
  });
}
