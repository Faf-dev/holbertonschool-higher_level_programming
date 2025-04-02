function fetchTitle () {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const ul = document.querySelector('#list_movies');
      if (ul) {
        data.results.forEach(movie => {
          const li = document.createElement('li');
          li.textContent = movie.title;
          ul.appendChild(li);
        });
      }
    })
    .catch(error => {
      console.log(error);
    });
}

const listMovies = document.querySelector('#list_movies');
if (listMovies) {
  fetchTitle();
} // Une chaine " " apparait entre la balise </li> et </ul>
