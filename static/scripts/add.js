function add() {
    let title = document.getElementById('input-title');
    let genre = document.getElementById('input-genre');
    let date = document.getElementById('input-date')

    fetch('/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ // Convert data to JSON format
            'title': title.value,
            'genre': genre.value,
            'date': date.value
        })
    })
        .then(response => response.json())
        .then(function (data) {
            console.log(data);
            alert("Success!")
            title.value = ""
            genre.value = ""
            date.value = ""
        }).catch(err => {
            console.log(err)
        })
}