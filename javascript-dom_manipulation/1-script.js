function updateColor() {
  const header = document.querySelector("header");
  if (header) {
  header.style.color = "#FF0000";
  }
}

const redHeader = document.querySelector("#red_header");
if (redHeader) {
  redHeader.addEventListener("click", updateColor);
}
