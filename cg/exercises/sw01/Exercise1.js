//
// Computer Graphics
//
// WebGL Exercises
//

// Register function to call after document has loaded
window.onload = startup;

// the gl object is saved globally
var gl;

// we keep all local parameters for the program in a single object
// Schritt 2: Abfragen des Index dieses Attributs im JavaScript Program
var ctx = {

    shaderProgram: -1,
    aVertexPositionId: -1

};

// we keep all the parameters for drawing a specific object together
var rectangleObject = {

    buffer: -1

};

/**
 * Startup function to be called when the body is loaded
 */
function startup() {

    "use strict";
    var canvas = document.getElementById("myCanvas");

    gl = createGLContext(canvas);

    initGL();

    draw();

}

/**
 * InitGL should contain the functionality that needs to be executed only once
 */
function initGL() {
    
    "use strict";

    // Add custom Shaders
    ctx.shaderProgram = loadAndCompileShaders(gl, "VertexShader.glsl", "FragmentShader.glsl");
    setUpAttributesAndUniforms();
    setUpBuffers();
    gl.clearColor(0.3688,0.2312,0.0000,0.3725);
    
    // add more necessary commands here

}

/**
 * Setup all the attribute and uniform variables
 * Schritt 2: Abfragen des Index dieses Attributs im JavaScript Program
 */
function setUpAttributesAndUniforms(){
    "use strict";

    // finds the index of the variable in the program
    ctx.aVertexPositionId = gl.getAttribLocation(ctx.shaderProgram, "aVertexPosition");
}

/**
 * Setup the buffers to use. If more objects are needed this should be split in a file per object.
 */
function setUpBuffers(){
    "use strict";

    var vertices = [
        0,0,
        1,0,
        0,1,
        1,1
    ];

    rectangleObject.buffer = gl.createBuffer();

    gl.bindBuffer(

        gl.ARRAY_BUFFER,
        rectangleObject.buffer

    );

    gl.bufferData(

        gl.ARRAY_BUFFER ,
        new Float32Array(vertices),
        gl.STATIC_DRAW

    );
}

/**
 * Draw the scene.
 */
function draw() {

    "use strict";
    console.log("Drawing");

    // Schritt 5: Verbinden des Buffers mit dem Attribut Index
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.bindBuffer(gl.ARRAY_BUFFER , rectangleObject.buffer);
    gl.vertexAttribPointer(ctx.aVertexPositionId, 2, gl.FLOAT, false, 0, 0);
    gl.enableVertexAttribArray(ctx.aVertexPositionId);

    // Schritt 6: Zeichnen des Arrays
    gl.drawArrays(gl.LINE_LOOP, 0, 4);

}