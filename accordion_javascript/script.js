const accordionItems = document.querySelectorAll('.container')

for (const iterator of accordionItems) {
  iterator.addEventListener('contextmenu', (e) => {
    console.log(e);
    e.target.parentElement.classList.toggle('active');
  });

};
