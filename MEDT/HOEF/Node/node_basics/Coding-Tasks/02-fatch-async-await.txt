async function logData() {
    try {
        const response = await fetch('https://randomuser.me/api/');

        const data = await response.json();

        const { results } = data;
        const { name } = results[0]

        console.log(`The name:  ${name.title} ${name.first} ${name.last}`);
    } catch (error) {
        console.log(error)
    }
}