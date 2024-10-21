"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var drawScene_js_1 = require("./drawScene.js");
var initBuffers_js_1 = require("./initBuffers.js");
//
// start here
//
// attribute -> verändert sich immer 
// uniform -> bleibt gleich (fixer wert)
// Vertex shader program
// Vertex shader program
var vsSource = "\n    attribute vec4 aVertexPosition;\n    attribute vec4 aVertexColor;\n\n    uniform mat4 uModelViewMatrix;\n    uniform mat4 uProjectionMatrix;\n\n    varying lowp vec4 vColor;\n\n    void main(void) {\n      gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;\n      vColor = aVertexColor;\n    }\n  ";
var fsSource = "\n  varying lowp vec4 vColor;\n\n  void main(void) {\n    gl_FragColor = vColor;\n  }\n";
//
// Initialize a shader program, so WebGL knows how to draw our data
//
function initShaderProgram(gl, vsSource, fsSource) {
    var vertexShader = loadShader(gl, gl.VERTEX_SHADER, vsSource);
    var fragmentShader = loadShader(gl, gl.FRAGMENT_SHADER, fsSource);
    // Create the shader program
    var shaderProgram = gl.createProgram();
    gl.attachShader(shaderProgram, vertexShader); // ich hänge einen shader zu diesem Program dazu
    gl.attachShader(shaderProgram, fragmentShader);
    gl.linkProgram(shaderProgram);
    // If creating the shader program failed, alert
    if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
        alert("Unable to initialize the shader program: ".concat(gl.getProgramInfoLog(shaderProgram)));
        return null;
    }
    return shaderProgram;
}
//
// creates a shader of the given type, uploads the source and
// compiles it.
//
function loadShader(gl, type, source) {
    var shader = gl.createShader(type);
    // Send the source to the shader object
    gl.shaderSource(shader, source); //Shader code in ein Objekt packen
    // Compile the shader program
    gl.compileShader(shader);
    // See if it compiled successfully
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        alert("An error occurred compiling the shaders: ".concat(gl.getShaderInfoLog(shader)));
        gl.deleteShader(shader);
        return null;
    }
    return shader;
}
function main() {
    var canvas = document.querySelector("#glcanvas"); // * Das 'as' ist wie ein Typecast
    // Initialize the GL context
    var gl = canvas.getContext("webgl");
    // Only continue if WebGL is available and working
    if (gl === null) {
        alert("Unable to initialize WebGL. Your browser or machine may not support it.");
        return;
    }
    // Initialize a shader program; this is where all the lighting
    // for the vertices and so forth is established.
    var shaderProgram = initShaderProgram(gl, vsSource, fsSource);
    // Collect all the info needed to use the shader program.
    // Look up which attribute our shader program is using
    // for aVertexPosition and look up uniform locations.
    var programInfo = {
        program: shaderProgram,
        attribLocations: {
            vertexPosition: gl.getAttribLocation(shaderProgram, "aVertexPosition"),
            vertexColor: gl.getAttribLocation(shaderProgram, "aVertexColor")
        },
        uniformLocations: {
            projectionMatrix: gl.getUniformLocation(shaderProgram, "uProjectionMatrix"),
            modelViewMatrix: gl.getUniformLocation(shaderProgram, "uModelViewMatrix"),
        },
    };
    var buffers = (0, initBuffers_js_1.initBuffers)(gl);
    requestAnimationFrame(render);
    // Draw the scene repeatedly
    function render(now) {
        // console.log(deltaTime);
        now *= 0.001; // convert to seconds
        deltaTime = now - then;
        then = now;
        (0, drawScene_js_1.drawScene)(gl, programInfo, buffers, squareRotation);
        squareRotation += deltaTime;
        requestAnimationFrame(render);
    }
}
var squareRotation = 0;
var deltaTime = 0;
var then = 0;
main();
