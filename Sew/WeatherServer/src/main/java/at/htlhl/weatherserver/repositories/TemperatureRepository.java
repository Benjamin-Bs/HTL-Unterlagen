package at.htlhl.weatherserver.repositories;

import at.htlhl.weatherserver.models.Temperature;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.time.LocalDateTime;

@Repository
public class TemperatureRepository {

    // Constants **************************************************************
    private static final Logger LOGGER = (Logger) LoggerFactory.getLogger(TemperatureRepository.class);
    private static final String INSERT_TEMPERATURE_SQL = "INSERT INTO TEMPERATURE (measuretime, temperature) VALUES (?, ?)";

    private static final String SELECT_LATEST_TEMPERATURE_SQL =
            """
            SELECT      measuretime, temperature 
            FROM        temperature
            ORDER BY    measuretime DESC
            LIMIT       1
            """;

    // Fields *****************************************************************

    @Autowired
    private JdbcTemplate jdbcTemplate;

    // Database CrUT operations (CRUT = Create Read Update delete) ************

    public Temperature insert(Temperature temperature) throws SQLException {
        if(temperature.getMeasureTime()==null){
            LocalDateTime measureTime = LocalDateTime.now();
            temperature.setMeasureTime(measureTime);
            LOGGER.info("measure time added(" + measureTime + ")");
        }

        PreparedStatement ps = jdbcTemplate.getDataSource().getConnection().prepareStatement(INSERT_TEMPERATURE_SQL);
        ps.setTimestamp(1, Timestamp.valueOf(temperature.getMeasureTime()));
        ps.setFloat(2,temperature.getTemperature());
        int linesInTableChanged = ps.executeUpdate();
        LOGGER.info("Lines inserted: " + linesInTableChanged);
        return temperature;

    }

    public Temperature findLatestTemperature() throws SQLException{

        ResultSet rs = jdbcTemplate.getDataSource().getConnection().createStatement().executeQuery(SELECT_LATEST_TEMPERATURE_SQL);

        if(rs.next()){
            Temperature temperature = new Temperature();
            temperature.setMeasureTime(rs.getTimestamp("measuretime").toLocalDateTime());
            temperature.setTemperature(rs.getFloat("temperature"));
            return temperature;
        }else {
            throw new SQLException("could not fatch data from database");
        }

    }

}
