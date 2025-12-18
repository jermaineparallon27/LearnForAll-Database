function filterList(inputId, listId) {
    var input = document.getElementById(inputId).value.toLowerCase();
    var items = document.getElementById(listId).getElementsByTagName('li');

    for (var i = 0; i < items.length; i++) {
        if (items[i].innerText.toLowerCase().includes(input)) {
            items[i].style.display = '';
        } else {
            items[i].style.display = 'none';
        }
    }
}