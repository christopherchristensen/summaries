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

    aVertexPositionId: -1,
    aColorPositionId: -1,
    aNormalVertexId: -1,
    aVertexTexturCoordId: -1,
    uEnableTextureId: -1,
    uEnableLightingId: -1,
    uLightPositionId: -1,
    uLightColorId: -1,
    uSamplerId: -1,
    uModelViewMatrixId: -1,
    uProjectionMatrixId: -1,
    uNormalMatrixId: -1
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
    ctx.shaderProgram = loadAndCompileShaders(gl, 'VertexShader.glsl', 'FragmentShader.glsl');
    setUpAttributesAndUniforms();
    setUpBuffers();
    gl.clearColor(0.8, 0.8, 0.8, 1);

}

/**
 * Setup all the attribute and uniform variables
 */
function setUpAttributesAndUniforms() {

    "use strict";

    ctx.aVertexPositionId = gl.getAttribLocation(ctx.shaderProgram, "aVertexPosition");
    ctx.aColorPositionId = gl.getAttribLocation(ctx.shaderProgram, "aVertexColor");
    ctx.aNormalVertexId = gl.getAttribLocation(ctx.shaderProgram, "aVertexNormal");
    ctx.aVertexTexturCoordId = gl.getAttribLocation(ctx.shaderProgram, "aVertexTextureCoord");

    ctx.uEnableTextureId = gl.getUniformLocation(ctx.shaderProgram, "uEnableTexture");
    ctx.uEnableLightingId = gl.getUniformLocation(ctx.shaderProgram, "uEnableLighting");
    ctx.uLightPositionId = gl.getUniformLocation(ctx.shaderProgram, "uLightPosition");
    ctx.uLightColorId = gl.getUniformLocation(ctx.shaderProgram, "uLightColor");
    ctx.uSamplerId = gl.getUniformLocation(ctx.shaderProgram, "uSampler");
    ctx.uViewMatrixId = gl.getUniformLocation(ctx.shaderProgram, "uViewMatrix");
    ctx.uModelMatrixId = gl.getUniformLocation(ctx.shaderProgram, "uModelMatrix");
    ctx.uProjectionMatrixId = gl.getUniformLocation(ctx.shaderProgram, "uProjectionMatrix");
    ctx.uNormalMatrixId = gl.getUniformLocation(ctx.shaderProgram, "uNormalMatrix");

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

    gl.uniform1i(ctx.uEnableLightingId, true);
    gl.uniform1i(ctx.uEnableTextureId, false);
    gl.uniform3fv(ctx.uLightPositionId, [-7, 7, 7]);
    gl.uniform3fv(ctx.uLightColorId, [0.6, 0.6, 0.6]);

    gl.clear(gl.COLOR_BUFFER_BIT);

    var modelMatrix = mat4.create();
    var viewMatrix = mat4.create();
    var projectionMatrix = mat4.create();
    mat4.identity(modelMatrix);
    mat4.lookAt(viewMatrix, [-5, 5, -5], [0, 1, 0], [0, 2, 0]);
    mat4.perspective(projectionMatrix, glMatrix.toRadian(45), gl.drawingBufferWidth / gl.drawingBufferHeight, 0.2, 1000.0);

    gl.uniformMatrix4fv(ctx.uViewMatrixId, false, viewMatrix);
    gl.uniformMatrix4fv(ctx.uModelMatrixId, false, modelMatrix);
    gl.uniformMatrix4fv(ctx.uProjectionMatrixId, false, projectionMatrix);

    var normalMatrix = mat3.create();
    var modelViewMatrix = mat4.create();

    mat4.multiply(modelViewMatrix, viewMatrix, modelMatrix);
    mat3.normalFromMat4(normalMatrix, modelViewMatrix);
    gl.uniformMatrix3fv(ctx.uNormalMatrixId, false, normalMatrix);

    // definition
    var wiredCube = new WireFrameCube(gl);
    var solidSphere = new SolidSphere(gl, 10, 10);

    var angle = 0;
    var identityMatrix = mat4.create();

    mat4.identity(identityMatrix);

    var loop = function () {
        angle = performance.now() / 1000 / 10 * 2 * Math.PI;

        gl.clearColor(0.8, 0.8, 0.8, 1);
        gl.enable(gl.DEPTH_TEST);
        gl.clear(gl.DEPTH_BUFFER_BIT | gl.COLOR_BUFFER_BIT);

        // draw cube
        mat4.translate(modelMatrix,identityMatrix, [0, 0, 1]);
        mat4.rotate(modelMatrix, modelMatrix, angle, [0.5, 1, 0]);
        gl.uniformMatrix4fv(ctx.uModelMatrixId, false, modelMatrix);

        mat4.multiply(modelViewMatrix, viewMatrix, modelMatrix);
        mat3.normalFromMat4(normalMatrix, modelViewMatrix);
        gl.uniformMatrix3fv(ctx.uNormalMatrixId,false,normalMatrix);
        wiredCube.draw(gl, ctx.aVertexPositionId, ctx.aColorPositionId, ctx.aNormalVertexId);

        // draw sphere
        mat4.translate(modelMatrix,identityMatrix, [3, 0, 1]);
        mat4.rotate(modelMatrix, modelMatrix, angle, [0, 1, 0]);
        gl.uniformMatrix4fv(ctx.uModelMatrixId, false, modelMatrix);

        mat4.multiply(modelViewMatrix, viewMatrix, modelMatrix);
        mat3.normalFromMat4(normalMatrix, modelViewMatrix);
        gl.uniformMatrix3fv(ctx.uNormalMatrixId,false,normalMatrix);
        solidSphere.draw(gl, ctx.aVertexPositionId, ctx.aColorPositionId, ctx.aNormalVertexId, [0.7, 0.8, 0.7]);

        requestAnimationFrame(loop);

    };

    requestAnimationFrame(loop);

}