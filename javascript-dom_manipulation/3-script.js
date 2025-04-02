function changeColor () {
  const header = document.querySelector('header');
  if (header) {
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else if (header.classList.contains('green')) {
      header.classList.remove('green');
      header.classList.add('red');
    } else {
      header.classList.add('red'); // Assignation par défaut si red et green n'est pas présent
    }
  }
}

const toggleHeader = document.querySelector('#toggle_header');
if (toggleHeader) {
  toggleHeader.addEventListener('click', changeColor);
}
