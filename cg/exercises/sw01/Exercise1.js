//
// Computer Graphics
//
// WebGL Exercises
//

// Register function to call after document has loaded
window.onload = startup;

// GL object saved globally
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

    // -- 1. Create context from canvas
    gl = createGLContext(canvas);

    // -- 2. Initialize the GL object (global)
    initGL();

    // -- 3. Draw objects
    draw();

}

/**
 * InitGL should contain the functionality that needs to be executed only once
 */
function initGL() {
    
    "use strict";

    // -- 1. Add shaders (load / compile)
    ctx.shaderProgram = loadAndCompileShaders(gl, "VertexShader.glsl", "FragmentShader.glsl");

    // -- 2. Assign attribute-index to context
    setUpAttributesAndUniforms();

    // -- 3. Setup buffers
    setUpBuffers();

    // -- 4. Set color ??
    gl.clearColor(0.4688,0.1512,0.0000,0.2725);

}

/**
 * Setup all the attribute and uniform variables
 * Schritt 2: Abfragen des Index dieses Attributs im JavaScript Program
 */
function setUpAttributesAndUniforms(){

    "use strict";

    // Finds index of the variable in the program
    ctx.aVertexPositionId = gl.getAttribLocation(ctx.shaderProgram, "aVertexPosition");

}

/**
 * Setup the buffers to use. If more objects are needed this should be split in a file per object.
 */
function setUpBuffers(){

    "use strict";

    // Vertex data (positions)
    var vertices = [
        -0.5, -0.5,
        -0.5, 0.5,
        0.5, -0.5,
        0.5, 0.5,
        1.0,1.0
    ];

    // Create WebGL buffer
    rectangleObject.buffer = gl.createBuffer();

    // Bind the WebGL buffer to WebGL global context
    gl.bindBuffer(

        gl.ARRAY_BUFFER,
        rectangleObject.buffer

    );

    // Put data into buffer
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
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);


}