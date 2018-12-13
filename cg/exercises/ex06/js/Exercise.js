//
// DI Computer Graphics
//
// WebGL Exercises
//

// Turn Texture Mapping on and off
// Add Transformation
// Add 3D functionality
// Add shading

// Register function to call after document has loaded
window.onload = startup;

// the gl object is saved globally
var gl;

// all parameters associated with the shader program
var ctx = {

    shaderProgram: -1,

    aVertexPositionId: -1,
    aVertexColorId: -1,
    aVertexTextureCoordId: -1,
    aVertexNormalId: -1, // TODO: -2

    uModelViewMatrixId: -1,
    uProjectionMatrixId: -1,
    uNormalMatrixId: -1,
    uTextureMatrixId: -1,
    uSamplerId: -1,
    uEnableTextureId: -1,
    uLightPositionId: -1,
    uLightColorId: -1,
    uEnableLightingId: -1

};

// loaded textures
var textures = { // TODO: colorCube, sphere, textureCube
    textureObject0: {}
};

// parameters that define the scene
var scene = {
    eyePosition: [-1, 4, -4],
    lookAtPosition: [0, 0, 0],
    upVector: [0, 1, 0],
    nearPlane: 0.1,
    farPlane: 30.0,
    fov: 40,
    lightPosition: [-20, 20, 0],
    lightColor: [0.5, 1, 1],
    rotateObjects: true,
    angle: 0,
    angularSpeed: 0.1 * 2 * Math.PI / 360.0
};

// defined object
var drawingObjects = {
    wiredCube: -1,
    solidCube: -1,
    solidSphere: -1
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
    window.requestAnimationFrame (drawAnimated);
}

/**
 * InitGL should contain the functionality that needs to be executed only once
 */
function initGL() {
    "use strict";
    ctx.shaderProgram = loadAndCompileShaders(gl, 'shaders/VertexShader.glsl', 'shaders/FragmentShaderLighting.glsl');
    setUpAttributesAndUniforms();
    defineObjects();

    gl.enable(gl.DEPTH_TEST);
    gl.clearColor(0.8, 0.8, 0.8, 1);
}

/**
 * Initialize a texture from an image
 * @param image the loaded image
 * @param textureObject WebGL Texture Object
 */
function initTexture(image, textureObject) {
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
    var image = new Image();
    // create a texture object
    textures.textureObject0 = gl.createTexture();
    image.onload = function() {
        console.log("Image loaded");
        initTexture(image, textures.textureObject0);
    };
    // setting the src will trigger onload
    image.src = "/img/lena512.png";
}

function defineObjects() {
    drawingObjects.wiredCube = new WireFrameCube(gl, [1.0, 1.0, 0.0]);
    drawingObjects.solidCube = new SolidCube(gl,
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 1.0, 0.0],
        [0.0, 1.0, 1.0],
        [1.0, 0.0, 1.0]);
    drawingObjects.solidSphere = new SolidSphere(gl, 40, 40);
}

/**
 * Setup all the attribute and uniform variables
 */
function setUpAttributesAndUniforms(){
    "use strict";
    ctx.aVertexPositionId = gl.getAttribLocation(ctx.shaderProgram, "aVertexPosition");
    ctx.aVertexColorId = gl.getAttribLocation(ctx.shaderProgram, "aVertexColor");
    ctx.aVertexTextureCoordId = gl.getAttribLocation(ctx.shaderProgram, "aVertexTextureCoord");
    ctx.aVertexNormalId = gl.getAttribLocation(ctx.shaderProgram, "aVertexNormal");

    ctx.uModelViewMatrixId = gl.getUniformLocation(ctx.shaderProgram, "uModelViewMatrix");
    ctx.uProjectionMatrixId = gl.getUniformLocation(ctx.shaderProgram, "uProjectionMatrix");
    ctx.uNormalMatrixId = gl.getUniformLocation(ctx.shaderProgram, "uNormalMatrix");
    ctx.uTextureMatrixId = gl.getUniformLocation(ctx.shaderProgram, "uTextureMatrix");

    ctx.uSamplerId = gl.getUniformLocation(ctx.shaderProgram, "uSampler");
    ctx.uEnableTextureId = gl.getUniformLocation(ctx.shaderProgram, "uEnableTexture");

    ctx.uLightPositionId = gl.getUniformLocation(ctx.shaderProgram, "uLightPosition");
    ctx.uLightColorId = gl.getUniformLocation(ctx.shaderProgram, "uLightColor");
    ctx.uEnableLightingId = gl.getUniformLocation(ctx.shaderProgram, "uEnableLighting");
}

/**
 * Draw the scene.
 */
function draw() {
    "use strict";
    var modelViewMatrix = mat4.create();
    var viewMatrix = mat4.create();
    var projectionMatrix = mat4.create();
    var textureMatrix = mat3.create();
    var normalMatrix = mat3.create();

    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    // set the matrices from the scene
    mat4.lookAt(viewMatrix, scene.eyePosition, scene.lookAtPosition, scene.upVector);

    gl.enable(gl.DEPTH_TEST);
    gl.uniform1i(ctx.uEnableLightingId, 1);
    gl.uniform1i(ctx.uEnableTextureId, 0);

    gl.uniform3fv(ctx.uLightColorId, [0.8, 0.5, 0.8]);
    gl.uniform3fv(ctx.uLightPositionId, [10, 10, 10]);

    mat4.perspective(projectionMatrix,
        glMatrix.toRadian(40),
        gl.drawingBufferWidth / gl.drawingBufferHeight,
        scene.nearPlane, scene.farPlane);
    //mat4.ortho(projectionMatrix, -2.0, 2.0, -2.0, 2.0, scene.nearPlane, scene.farPlane);


    // enable the texture mapping
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, textures.textureObject0);
    gl.uniform1i(ctx.uSamplerId, 0);
    gl.uniformMatrix3fv(ctx.uTextureMatrixId, false, textureMatrix);

    // tell the fragment shader to use the texture
    gl.uniform1i(ctx.uEnableTextureId, 1);

    gl.uniformMatrix3fv(ctx.uTextureMatrixId, false, textureMatrix);


    // set the light
    gl.uniform1i(ctx.uEnableLightingId, 1);
    gl.uniform3fv(ctx.uLightPositionId, scene.lightPosition);
    gl.uniform3fv(ctx.uLightColorId, scene.lightColor);

    // same projection matrix for all drawings, so it can be specified here
    gl.uniformMatrix4fv(ctx.uProjectionMatrixId, false, projectionMatrix);

    // translate and rotate objects
    mat4.translate(modelViewMatrix, viewMatrix, [1.0, 0, 0]);
    mat4.rotate(modelViewMatrix, modelViewMatrix, scene.angle, [0, 1, 0]);
    gl.uniformMatrix4fv(ctx.uModelViewMatrixId, false, modelViewMatrix);
    mat3.normalFromMat4(normalMatrix, modelViewMatrix);
    gl.uniformMatrix3fv(ctx.uNormalMatrixId, false, normalMatrix);
    //drawingObjects.wiredCube.draw(gl, ctx.aVertexPositionId, ctx.aVertexColorId);
    drawingObjects.solidCube.draw(gl, ctx.aVertexPositionId, ctx.aVertexColorId, ctx.aVertexNormalId);


    // translate and rotate objects
    mat4.translate(modelViewMatrix, viewMatrix, [-1.0, 0, 0]);
    mat4.rotate(modelViewMatrix, modelViewMatrix, scene.angle, [0, 1, 0]);
    gl.uniformMatrix4fv(ctx.uModelViewMatrixId, false, modelViewMatrix);
    mat3.normalFromMat4(normalMatrix, modelViewMatrix);
    gl.uniformMatrix3fv(ctx.uNormalMatrixId, false, normalMatrix);
    drawingObjects.solidCube.draw(gl, ctx.aVertexPositionId, ctx.aVertexColorId, ctx.aVertexNormalId);

    // draw sphere
    mat4.translate(modelViewMatrix, viewMatrix, [0.0, 0.0, -1.0]);
    mat4.rotate(modelViewMatrix, modelViewMatrix, scene.angle, [0, 1, 0]);
    mat4.scale(modelViewMatrix, modelViewMatrix, [0.5, 0.5, 0.5]);
    gl.uniformMatrix4fv(ctx.uModelViewMatrixId, false, modelViewMatrix);
    mat3.normalFromMat4(normalMatrix, modelViewMatrix);
    gl.uniformMatrix3fv(ctx.uNormalMatrixId, false, normalMatrix);
    drawingObjects.solidSphere.drawWithColor(gl, ctx.aVertexPositionId, ctx.aVertexColorId, ctx.aVertexNormalId, [1, 0, 0]);
}

var first = true;
var lastTimeStamp = 0;


function drawAnimated ( timeStamp ) {
    var timeElapsed = 0;
    if (first) {
        lastTimeStamp = timeStamp;
        first = false;
    } else {
        timeElapsed = timeStamp - lastTimeStamp;
        lastTimeStamp = timeStamp;
    }
    // calculate time since last call
    // move or change objects
    scene.angle += timeElapsed * scene.angularSpeed;
    if (scene.angle > 2.0*Math.PI) {
        scene.angle -= 2.0*Math.PI;
    }
    draw ();
    // request the next frame
    window.requestAnimationFrame (drawAnimated);
}