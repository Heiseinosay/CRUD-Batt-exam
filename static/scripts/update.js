let bookID = document.getElementById("bookID")
let title = document.getElementById('input-title')
let genre = document.getElementById('input-genre')
let date = document.getElementById('input-date')
let updateable = false // filter for valid bookID only

function searchByID() {

    fetch(`/searchByID?bookID=${encodeURIComponent(bookID.value)}`, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(data => {
            console.log(data[0])
            title.value = data[0][1]
            genre.value = data[0][2]
            // Convert the date to YYYY-MM-DD format
            let originalDate = new Date(data[0][3]);
            let formattedDate = originalDate.toISOString().split('T')[0]; // Extract YYYY-MM-DD

            date.value = formattedDate;
            updateable = true
        })
        .catch(err => {
            updateable = false
            console.error("Error searching:", err)
        })
}

function update() {
    if (updateable == true) {
        fetch("/update", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ // Convert data to JSON format
                'bookID': bookID.value,
                'title': title.value,
                'genre': genre.value,
                'date': date.value
            })
        })
            .then(response => response.json())
            .then(data => {
                alert("Successfully updated!")
                bookID.value = ""
                title.value = ""
                genre.value = ""
                date.value = ""
            })
            .catch(err => {
                console.log(err)
            })
    } else {
        alert("Please input a valid bookID")
    }
}