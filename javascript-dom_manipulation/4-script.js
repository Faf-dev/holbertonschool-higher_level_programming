function addLi () {
  const ul = document.querySelector('ul.my_list');
  if (ul) {
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
  }
}

const addItem = document.querySelector('#add_item');
if (addItem) {
  addItem.addEventListener('click', addLi); 
}
