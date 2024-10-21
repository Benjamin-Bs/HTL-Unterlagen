"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.drawScene = drawScene;
var gl_matrix_1 = require("gl-matrix");
function drawScene(gl, programInfo, buffers, squareRotation) {
    gl.clearColor(0.0, 0.0, 0.0, 1.0); // Clear to black, fully opaque
    gl.clearDepth(1.0); // Clear everything // Wenn Elemente hintereinander sind, schaut die grafikkarte welches objekt näher zur kamera ist
    gl.enable(gl.DEPTH_TEST); // Enable depth testing
    gl.depthFunc(gl.LEQUAL); // Near things obscure far things
    // Clear the canvas before we start drawing on it.
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
    // Create a perspective matrix, a special matrix that is
    // used to simulate the distortion of perspective in a camera.
    // Our field of view is 45 degrees, with a width/height
    // ratio that matches the display size of the canvas
    // and we only want to see objects between 0.1 units
    // and 100 units away from the camera.
    var fieldOfView = (45 * Math.PI) / 180; // in radians
    var aspect = gl.canvas.clientWidth / gl.canvas.clientHeight;
    var zNear = 0.1;
    var zFar = 100.0;
    var projectionMatrix = gl_matrix_1.mat4.create();
    // note: glmatrix.js always has the first argument
    // as the destination to receive the result.
    gl_matrix_1.mat4.perspective(projectionMatrix, fieldOfView, aspect, zNear, zFar);
    // Set the drawing position to the "identity" point, which is
    // the center of the scene.
    var modelViewMatrix = gl_matrix_1.mat4.create();
    // Now move the drawing position a bit to where we want to
    // start drawing the square.
    gl_matrix_1.mat4.translate(modelViewMatrix, // destination matrix
    modelViewMatrix, // matrix to translate
    [-0.0, 0.0, -6.0]); // amount to translate
    gl_matrix_1.mat4.rotate(modelViewMatrix, // destination matrix
    modelViewMatrix, // matrix to rotate
    squareRotation, // amount to rotate in radians
    [0, 0, 1]); // axis to rotate around      
    // Tell WebGL how to pull out the positions from the position
    // buffer into the vertexPosition attribute.
    setPositionAttribute(gl, buffers, programInfo);
    setColorAttribute(gl, buffers, programInfo);
    // Tell WebGL to use our program when drawing
    gl.useProgram(programInfo.program);
    // Set the shader uniforms
    gl.uniformMatrix4fv(programInfo.uniformLocations.projectionMatrix, false, projectionMatrix);
    gl.uniformMatrix4fv(programInfo.uniformLocations.modelViewMatrix, false, modelViewMatrix);
    {
        var offset = 0;
        var vertexCount = 4;
        gl.drawArrays(gl.TRIANGLE_STRIP, offset, vertexCount);
    }
}
// Tell WebGL how to pull out the colors from the color buffer
// into the vertexColor attribute.
function setColorAttribute(gl, buffers, programInfo) {
    var numComponents = 4;
    var type = gl.FLOAT;
    var normalize = false;
    var stride = 0;
    var offset = 0;
    gl.bindBuffer(gl.ARRAY_BUFFER, buffers.color);
    gl.vertexAttribPointer(programInfo.attribLocations.vertexColor, numComponents, type, normalize, stride, offset);
    gl.enableVertexAttribArray(programInfo.attribLocations.vertexColor);
}
// Tell WebGL how to pull out the positions from the position
// buffer into the vertexPosition attribute.
function setPositionAttribute(gl, buffers, programInfo) {
    var numComponents = 2; // pull out 2 values per iteration
    var type = gl.FLOAT; // the data in the buffer is 32bit floats
    var normalize = false; // don't normalize
    var stride = 0; // how many bytes to get from one set of values to the next
    // 0 = use type and numComponents above
    var offset = 0; // how many bytes inside the buffer to start from
    gl.bindBuffer(gl.ARRAY_BUFFER, buffers.position);
    gl.vertexAttribPointer(programInfo.attribLocations.vertexPosition, // String mit dem Variablen Namen
    numComponents, type, normalize, stride, offset);
    gl.enableVertexAttribArray(programInfo.attribLocations.vertexPosition);
}
