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
    aVertexPositionId: -1,
    uColorId: -1,
    texture2DId: -1

};

// we keep all the parameters for drawing a specific object together
var rectangleObject = {

    buffer: -1

};

// Keep texture parameters in an object so we can mix textures and objects
var lennaTxt = {

    textureObject: {}

}

// create the texture coordinates for the object
var textureCoord = [ 
    -0.25, -0.25,
    -0.25, 0.25,
    0.25, -0.25,
    0.25, 0.25
];

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
* Initialize a texture from an image
* @param image the loaded image
* @param textureObject WebGL Texture Object */
function initTexture (image, textureObject) {

    // Create a new texture
    gl.bindTexture(gl.TEXTURE_2D, textureObject);

    // Set parameters for the texture
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL , true);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image); 
    gl.texParameteri(gl.TEXTURE_2D , gl.TEXTURE_MAG_FILTER , gl.LINEAR); 
    gl.texParameteri(gl.TEXTURE_2D , gl.TEXTURE_MIN_FILTER , gl.LINEAR_MIPMAP_NEAREST); 
    gl.generateMipmap(gl.TEXTURE_2D);

    // Turn texture off again ??
    gl.bindTexture(gl.TEXTURE_2D, null);

}

/**
 * Setup all the attribute and uniform variables
 * Schritt 2: Abfragen des Index dieses Attributs im JavaScript Program
 */
function setUpAttributesAndUniforms(){

    "use strict";

    // Finds index of the variable in the program
    ctx.aVertexPositionId = gl.getAttribLocation(ctx.shaderProgram, "aVertexPosition");
    //ctx.uColorId = gl.getUniformLocation(ctx.shaderProgram, "uColor");
    ctx.texture2DId = gl.getUniformLocation(ctx.shaderProgram, "texture2D");

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
        0.5, 0.5
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

    // Texture Buffers
    rectangleObject.textureBuffer = gl.createBuffer(); 

    gl.bindBuffer(

        gl.ARRAY_BUFFER , 
        rectangleObject.textureBuffer

    ); 

    gl.bufferData(

        gl.ARRAY_BUFFER , 
        new Float32Array(textureCoord), 
        gl.STATIC_DRAW

    );

}


/**
 * Load an image as a texture 
 */
function loadTexture () {
    
    var image = new Image();
    // Create a texture object 
    lennaTxt.textureObj = gl.createTexture(); 
    image.onload = function() {

        initTexture(image, lennaTxt.textureObj);

        // Make sure there is a redraw after the loading of the texture
        draw(); 

    };

    // setting the src will trigger onload
    image.src = "lena512.png";

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

    gl.activeTexture(gl.TEXTURE0); 
    gl.bindTexture(gl.TEXTURE_2D , lennaTxt.textureObj); 
    gl.uniform1i(ctx.uSampler2DId , 0);

    // Schritt 6: Zeichnen des Arrays
    gl.uniform4f(ctx.texture2DId, 1, 0.5, 0.0, 1.0);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);


}