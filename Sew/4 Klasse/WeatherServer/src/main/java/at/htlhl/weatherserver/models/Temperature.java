package at.htlhl.weatherserver.models;

import java.time.LocalDateTime;

public class Temperature {

    private float temperature;
    private LocalDateTime measureTime;


    public Temperature(LocalDateTime measureTime, float temperature){
        this.measureTime = measureTime;
        this.temperature = temperature;
    }

    public Temperature(){

    }

    public float getTemperature() {
        return temperature;
    }

    public void setTemperature(float temperature) {
        this.temperature = temperature;
    }

    public LocalDateTime getMeasureTime() {
        return measureTime;
    }

    public void setMeasureTime(LocalDateTime measureTime) {
        this.measureTime = measureTime;
    }
}
