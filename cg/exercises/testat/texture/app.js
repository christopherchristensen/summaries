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
var ctx = {
    shaderProgram: -1,
    uColorId: -1,
    aColorPositionId: -1,
    aVertexPositionId: -1,
    uModelMat: -1,
    uViewMat: -1,
    aVertexTextureCoordId: -1,
    uProjectionMat: -1
};

// keep texture parameters in an object so we can mix textures and objects
var lennaTxt = {
    textureObj: {}
};

// we keep all the parameters for drawing a specific object together
var object = {
    vertexBuffer: -1,
    edgeBuffer: -1
};

/**
 * Startup function to be called when the body is loaded
 */
function startup() {

    "use strict";
    var canvas = document.getElementById("myCanvas");
    gl = createGLContext(canvas);
    initGL();
    loadTexture();

}


/**
 * InitGL should contain the functionality that needs to be executed only once
 */
function initGL() {

    "use strict";
    ctx.shaderProgram = loadAndCompileShaders(gl, 'VertexShader.glsl', 'FragmentShader.glsl');
    setUpAttributesAndUniforms();
    setUpBuffers();
    gl.clearColor(1, 1, 1, 1);

}

/**
 * Setup all the attribute and uniform variables
 */
function setUpAttributesAndUniforms() {

    "use strict";
    ctx.aVertexPositionId = gl.getAttribLocation(ctx.shaderProgram, "aVertexPosition");
    ctx.aColorPositionId = gl.getAttribLocation(ctx.shaderProgram, "aVertexColor");
    ctx.aVertexTextureCoordId = gl.getAttribLocation(ctx.shaderProgram, "aVertexTextureCoord");
    ctx.uColorId = gl.getUniformLocation(ctx.shaderProgram, "uColor");
    ctx.uModelMat = gl.getUniformLocation(ctx.shaderProgram, "modelMat");
    ctx.uViewMat = gl.getUniformLocation(ctx.shaderProgram, "viewMat");
    ctx.uProjectionMat = gl.getUniformLocation(ctx.shaderProgram, "projectionMat");

}

/**
 * Setup the buffers to use. If more objects are needed this should be split in a file per object.
 */
function setUpBuffers() {
    "use strict";
}

/**
 * Draw the scene.
 */
function draw() {
    "use strict";

    console.log("Drawing");
    gl.clear(gl.COLOR_BUFFER_BIT);

    var modelMatrix = mat4.create();
    var viewMatrix = mat4.create();
    var projectionMatrix = mat4.create();

    mat4.identity(modelMatrix);
    mat4.lookAt(viewMatrix, [-4, 3, -2], [0, 0, 0], [0, 1, 10]); // view perspective
    mat4.perspective(projectionMatrix, glMatrix.toRadian(45), gl.drawingBufferWidth / gl.drawingBufferHeight, 0.2, 1000.0);

    gl.uniformMatrix4fv(ctx.uModelMat, false, modelMatrix);
    gl.uniformMatrix4fv(ctx.uViewMat, false, viewMatrix);
    gl.uniformMatrix4fv(ctx.uProjectionMat, false, projectionMatrix);

    // definition
    var textureFrameCube = new TextureFrameCube(gl);

    var angle = 0;
    var identityMatrix = mat4.create();
    mat4.identity(identityMatrix);

    var loop = function() {

        angle = performance.now() / 1000 / 8 * 2 * Math.PI; // also triggers speed of rotation
        mat4.rotate(modelMatrix, identityMatrix, angle, [0, 1, 0.5]);
        gl.uniformMatrix4fv(ctx.uModelMat, false, modelMatrix);

        gl.clearColor(1, 1, 1, 1);
        gl.enable(gl.DEPTH_TEST);
        gl.clear(gl.DEPTH_BUFFER_BIT | gl.COLOR_BUFFER_BIT);

        // in draw
        textureFrameCube.draw(gl, ctx.aVertexPositionId, ctx.aVertexTextureCoordId, lennaTxt.textureObj);

        requestAnimationFrame(loop);

    };

    requestAnimationFrame(loop);

}

/**
 * Initialize a texture from an image
 * @param image the loaded image
 * @param textureObject WebGL Texture Object */
function initTexture(image, textureObject) {

    console.log("init Texture");

    // create a new texture
    gl.bindTexture(gl.TEXTURE_2D, textureObject);

    // set parameters for the texture
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_NEAREST);

    gl.generateMipmap(gl.TEXTURE_2D);

    // turn texture off again
    gl.bindTexture(gl.TEXTURE_2D, null);

}
/**
 * Load an image as a texture
 */
function loadTexture() {

    console.log("loading Texture");

    var image = new Image();

    // create a texture object
    lennaTxt.textureObj = gl.createTexture();

    image.onload = function () {

        initTexture(image, lennaTxt.textureObj);

        // make sure there is a redraw after the loading of the texture
        draw();

    };

    image.src = "lena512.png";

}