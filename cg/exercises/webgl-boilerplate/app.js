//
// Computer Graphics
//
// WebGL Exercises
//

// Register function to call after document has loaded
window.onload = startup;

// the gl object is saved globally
let gl;

// we keep all local parameters for the program in a single object
const ctx = {
    shaderProgram: -1
};

/**
 * Startup function to be called when the body is loaded
 */
function startup() {

    "use strict";

    let canvas = document.getElementById("myCanvas");

    gl = createGLContext(canvas);
    initGL();
    draw();

}

/**
 * InitGL should contain the functionality that needs to be executed only once
 */
function initGL() {

    "use strict";
    
    ctx.shaderProgram = loadAndCompileShaders(gl, 'VertexShader.glsl', 'FragmentShader.glsl');
    setUpAttributesAndUniforms();
    setUpBuffers();
    gl.clearColor(0.3,0,0,0.5);
    
    // add more necessary commands here
}

/**
 * Setup all the attribute and uniform variables
 */
function setUpAttributesAndUniforms(){
    "use strict";
}

/**
 * Setup the buffers to use. If more objects are needed this should be split in a file per object.
 */
function setUpBuffers(){
    "use strict";
}

/**
 * Draw the scene.
 */
function draw() {
    "use strict";
    console.log("Drawing");
    gl.clear(gl.COLOR_BUFFER_BIT);
    // add drawing routines here
}