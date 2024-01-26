package at.htlhl.weatherserver.controllers;

import io.swagger.v3.oas.annotations.Operation;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("weatherserver/greetings")
public class GreetingController {

    // Constantes *************************************************************

    private static final String HELLO_RESPONE = """
                {
                "type":"greeting",
                "value":"Hello ${NAME}!"
                }
                """;


    // Webservices ************************************************************

    @GetMapping(value = "/hello", produces = "application/json")
    @Operation(summary = "say hello to the given name")
    @ResponseStatus(HttpStatus.OK)
    public String sayHello(@RequestParam(defaultValue = "World") String name){

        return HELLO_RESPONE.replace("${NAME}",name);

    }

    /**
     * Alternative implementation of sayHello
     * @return
     */

    @GetMapping(value = "/hello/{name}" , produces = ("application/json"))
    @Operation(summary = "say hello to name")
    @ResponseStatus(HttpStatus.OK)
    public String sayHelloAlternative(@PathVariable String name){
        return HELLO_RESPONE.replace("${NAME}",name);
    }


}
