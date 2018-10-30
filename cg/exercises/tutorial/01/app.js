window.onload = initDemo;

var webGLContext = {};

function initDemo () {

    // Get canvas and WEBGL context
    var canvas = document.getElementById("myCanvas");
    var webGL  = canvas.getContext("webgl");

    checkBrowserSupport(webGL);
    initializeWebGL(webGL);

    var triangleVertices = [

        0.0, 0.5,       0.7, 0.2, 0.2,
        -0.5, -0.5,     0.2, 0.2, 0.7,
        0.5, -0.5,      0.2, 0.7, 0.2

    ];

    // To assign the vertices to the graphics card (currently on CPU),
    // we need to create a buffer and bind the buffer to webGL and bind
    // thevertices to that buffer
    var triangleVertexBufferObject = webGL.createBuffer();
    // Bind the buffer to webGL
    webGL.bindBuffer(webGL.ARRAY_BUFFER, triangleVertexBufferObject);
    // Pass the vertices data. Since Javascript stores all its numbers as
    // 64bit floating point precision we need to pass them as a Float32Array
    // STATIC_DRAW because we are not planning on changing the data after draw
    webGL.bufferData(webGL.ARRAY_BUFFER, new Float32Array(triangleVertices), webGL.STATIC_DRAW);

    // Now we need to tell the vertex shader that the triangle vertices are meant for him
    // So first we will get the location of the vertex shader attribute vertPosition
    var positionAttributeLocation = webGL.getAttribLocation(webGLContext.program, "vertPosition");
    var colorAttributeLocation = webGL.getAttribLocation(webGLContext.program, "vertColor");

    // Now we need to specify the layout of the attribute
    webGL.vertexAttribPointer(
        positionAttributeLocation, // Location
        2, // Number of elements per attribute (vec2),
        webGL.FLOAT, // type of elements
        webGL.FALSE, // normalized
        5 * Float32Array.BYTES_PER_ELEMENT, // Size of an individual vertex (BYTES_PER_ELEMENT holds the number 4)
        0 // Offset from the beginning of a single vertex to this attribute 
    )

    webGL.vertexAttribPointer(
        colorAttributeLocation, // Location
        3, // Number of elements per attribute (vec2),
        webGL.FLOAT, // type of elements
        webGL.FALSE, // normalized
        5 * Float32Array.BYTES_PER_ELEMENT, // Size of an individual vertex (BYTES_PER_ELEMENT holds the number 4)
        2 * Float32Array.BYTES_PER_ELEMENT // Offset from the beginning of a single vertex to this attribute 
    )

    webGL.enableVertexAttribArray(positionAttributeLocation);
    webGL.enableVertexAttribArray(colorAttributeLocation);

    // Draw triangle to screen
    webGL.useProgram(webGLContext.program);
    webGL.drawArrays(
        webGL.TRIANGLES, // triangles
        0, // how many vertices you want to skip
        3  // how many vertices you are passing
    )
    
    console.log("It works!");

}



// --- HELPER FUNCTIONS
function initializeWebGL (webGL) {

    // Set color
    webGL.clearColor(0, 0, 0, 0.03);
    webGL.clear(webGL.COLOR_BUFFER_BIT | webGL.DEPTH_BUFFER_BIT);

    var vertexShader = webGL.createShader(webGL.VERTEX_SHADER);
    var fragmentShader = webGL.createShader(webGL.FRAGMENT_SHADER);

    // Helper function loadAndCompile you will find in the 
    webGLContext.program = loadAndCompileShaders(webGL, "VertexShader.glsl", "FragmentShader.glsl");

}

function checkBrowserSupport (webGLContext) {

    if (!webGLContext) {
        // For IE and other older browsers
        webGL = canvas.getContext("experimental-webgl");

    }

    if (!webGLContext) {
        
        alert("Your browser doesn't support WEBGL");

    }

}