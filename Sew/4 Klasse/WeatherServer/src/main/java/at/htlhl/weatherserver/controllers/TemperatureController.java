package at.htlhl.weatherserver.controllers;

import at.htlhl.weatherserver.models.Temperature;
import at.htlhl.weatherserver.repositories.TemperatureRepository;
import io.swagger.v3.oas.annotations.Operation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.sql.SQLException;

@RestController
@RequestMapping("/weatherserver/temperature")
public class TemperatureController {

    private TemperatureRepository temperatureRepository;

    @PostMapping(value="", consumes = "application/json",produces="application/json")
    @ResponseStatus(HttpStatus.CREATED)
    @Operation(summary = "add a new temperature entry")
    public Temperature addTemperature (@RequestBody Temperature temperature) throws SQLException {
        return temperatureRepository.insert(temperature);
    }

    @GetMapping(value = "",
                produces = "application/json")
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "get latest temperature")
    public Temperature findLatest() throws SQLException {
        return temperatureRepository.findLatestTemperature();
    }

    @Autowired
    public void setTemperatureRepository(TemperatureRepository temperatureRepository){
        this.temperatureRepository = temperatureRepository;
    }




}
