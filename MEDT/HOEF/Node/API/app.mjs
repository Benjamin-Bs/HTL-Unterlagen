import express from 'express';
import swaggerUi from 'swagger-ui-express';
import YAML from 'js-yaml';

const app = express();
const port = 3000;

// SWAGGER-UI ******************************************************************
const swaggerDocument = YAML.load('./swagger.yaml');
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// Test Daten *****************************************************************

let planets = [
    { id: 1, name: 'Kepler 1' },
    { id: 2, name: 'Kepler 2' },
    { id: 3, name: 'Kepler 3' }
];

let facilities = [
    { id: 1, name: 'Facility 1' },
    { id: 2, name: 'Facility 2' },
    { id: 3, name: 'Facility 3' }
];

// GET ************************************************************************

app.get('/planets/:id', (req, res) => {

    const id = parseInt(req.params.id);
    const planet = planets.find(p => p.id == id);

    res.json(planet)
});

app.get('/facilities/:id', (req, res) => {

    const id = parseInt(req.params.id);
    const facility = facilities.find(f => f.id == id);

    res.json(facility);
});

// POST ***********************************************************************

app.post('/planets/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const newPlanet = { id: id, name: `Kepler ${id}` };
    planets.push(newPlanet);
    res.json(newPlanet).send('New planet created');
});

app.post('/facilities/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const newFacility = { id: id, name: `Facility ${id}` };
    facilities.push(newFacility);
    res.json(newPlanet).send('New facility created');
});

// DELETE *********************************************************************

app.delete('/planets/:id', (req, res) => {

    const id = parseInt(req.params.id);
    planets = planets.filter(p => p.id !== id);
    res.send(`Planet with id ${id} deleted`);
});

app.delete('/facilities/:id', (req, res) => {

    const id = parseInt(req.params.id);
    facilities = facilities.filter(f => f.id !== id);
    res.send(`Facility with id ${id} deleted`);
});

// PUT ************************************************************************

app.put('/planets/:id', (req, res) => {
    const id = parseInt(req.params.id);

    const planet = req.body.planet;
    planet.id += 1;

    const index = planets.findIndex(p => p.id === id);
    res.json(planet);
});

app.put('/facilities/:id', (req, res) => {
    const id = parseInt(req.params.id);

    const facility = req.body.facilities;
    facility.id += 1;

    const index = facilities.findIndex(f => f.id === id);
    res.json(facility);
});

// PATCH ***********************************************************************

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});
