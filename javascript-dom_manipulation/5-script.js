function updateHeaderText() {
  const header = document.querySelector('header');
  if (header) {
    header.textContent = 'New Header!!!';
  }
}

const updateHeader = document.querySelector('#update_header');
if (updateHeader) {
  updateHeader.addEventListener('click', updateHeaderText);
}
