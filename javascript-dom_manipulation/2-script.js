function addRedClass () {
  const header = document.querySelector('header');
  if (header) {
    header.classList.add('red');
  }
}

const redHeader = document.querySelector('#red_header');
if (redHeader) {
  redHeader.addEventListener('click', addRedClass);
}
