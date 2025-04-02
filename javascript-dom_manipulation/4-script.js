function addLi () {
  const ul = document.querySelector('ul.my_list');
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
}

const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', addLi);
