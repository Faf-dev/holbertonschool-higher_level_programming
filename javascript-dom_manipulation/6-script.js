function fetchCharName () {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      character.textContent = data.name;
    })
    .catch(error => {
      console.log(error);
    });
}

const character = document.querySelector('#character');
if (character) {
  fetchCharName();
}
