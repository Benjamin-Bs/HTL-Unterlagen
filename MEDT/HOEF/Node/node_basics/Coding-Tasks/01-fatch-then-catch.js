
async function logData() {
    fetch('https://randomuser.me/api/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const { results } = data;
            const { name } = results[0]
            console.log(`The User name: ${name.title} ${name.first} ${name.last}`)
        })
        .catch(error => {
            console.log('Error: ' + error);
        });
}

logData();

