const collButton = document.querySelector('.coll button');
const searcher = document.querySelector('.searcher');
searcher.classList.add('hide'); 
collButton.addEventListener('click', e => {
    searcher.classList.toggle('show'); // Show the searcher when the button is clicked
    collButton.classList.toggle('hide'); // Hide the button
});