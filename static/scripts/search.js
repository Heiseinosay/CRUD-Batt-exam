function find() {
    const text = document.getElementById('search-bar').value
    fetch(`/search?title=${encodeURIComponent(text)}`, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(function (data) {
            console.log(data)
            // Display data on the table
            const tableBody = document.getElementById('rows'); // Reference the tbody element

            // Clear existing rows to avoid duplication
            tableBody.innerHTML = "";

            // Loop through the data and append rows to the table
            for (let i = 0; i < data.length; i++) {
                let tr = document.createElement("tr"); // Create a new table row

                // Create and append each cell for the row
                let td1 = document.createElement("td");
                td1.textContent = data[i][0]; // BookID
                tr.appendChild(td1);

                let td2 = document.createElement("td");
                td2.textContent = data[i][1]; // Title
                tr.appendChild(td2);

                let td3 = document.createElement("td");
                td3.textContent = data[i][2]; // Genre
                tr.appendChild(td3);

                let td4 = document.createElement("td");
                td4.textContent = data[i][3]; // PublicationDate
                tr.appendChild(td4);

                // Append the row to the table body
                tableBody.appendChild(tr);
            }
        })
        .catch(err => console.log(err))
}