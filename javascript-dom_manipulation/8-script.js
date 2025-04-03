function fetchValue () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const hi = document.querySelector('#hello');
      hi.textContent = data.hello;
    })
    .catch(error => {
      console.log(error);
    });
}
document.addEventListener('DOMContentLoaded', fetchValue);
