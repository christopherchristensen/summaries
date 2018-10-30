window.onload = initDemo;

var webGLContext = {};

function initDemo () {

    // Get canvas and WEBGL context
    var canvas = document.getElementById("myCanvas");
    var webGL  = canvas.getContext("webgl");

    checkBrowserSupport(webGL);
    initializeWebGL(webGL);

    var boxVertices = [
        // Top
		-1.0, 1.0, -1.0,   0.2, 0.0, 0.1,
		-1.0, 1.0, 1.0,    0.2, 0.0, 0.1,
		1.0, 1.0, 1.0,     0.2, 0.0, 0.1,
		1.0, 1.0, -1.0,    0.2, 0.0, 0.1,

		// Left
		-1.0, 1.0, 1.0,    0.1, 0.2, 0.0,
		-1.0, -1.0, 1.0,   0.1, 0.2, 0.0,
		-1.0, -1.0, -1.0,  0.1, 0.2, 0.0,
		-1.0, 1.0, -1.0,   0.1, 0.2, 0.0,

		// Right
		1.0, 1.0, 1.0,    0.0, 0.1, 0.2,
		1.0, -1.0, 1.0,   0.0, 0.1, 0.2,
		1.0, -1.0, -1.0,  0.0, 0.1, 0.2,
		1.0, 1.0, -1.0,   0.0, 0.1, 0.2,

		// Front
		1.0, 1.0, 1.0,    0.1, 0.1, 0.1,
		1.0, -1.0, 1.0,   0.1, 0.1, 0.1,
		-1.0, -1.0, 1.0,  0.1, 0.1, 0.1,
		-1.0, 1.0, 1.0,   0.1, 0.1, 0.1,

		// Back
		1.0, 1.0, -1.0,    0.3, 0.0, 0.0,
		1.0, -1.0, -1.0,   0.3, 0.0, 0.0,
		-1.0, -1.0, -1.0,  0.3, 0.0, 0.0,
		-1.0, 1.0, -1.0,   0.3, 0.0, 0.0,

		// Bottom
		-1.0, -1.0, -1.0,  0.3, 0.0, 0.2,
		-1.0, -1.0, 1.0,   0.3, 0.0, 0.2,
		1.0, -1.0, 1.0,    0.3, 0.0, 0.2,
		1.0, -1.0, -1.0,   0.3, 0.0, 0.2,
    ];

    var boxIndices =
	[
		// Top
		0, 1, 2,
		0, 2, 3,

		// Left
		5, 4, 6,
		6, 4, 7,

		// Right
		8, 9, 10,
		8, 10, 11,

		// Front
		13, 12, 14,
		15, 14, 12,

		// Back
		16, 17, 18,
		16, 18, 19,

		// Bottom
		21, 20, 22,
		22, 20, 23
	];

    var boxVertexBufferObject = webGL.createBuffer();
    webGL.bindBuffer(webGL.ARRAY_BUFFER, boxVertexBufferObject);
    webGL.bufferData(webGL.ARRAY_BUFFER, new Float32Array(boxVertices), webGL.STATIC_DRAW);

    var boxIndexBufferObject = webGL.createBuffer();
    webGL.bindBuffer(webGL.ELEMENT_ARRAY_BUFFER, boxIndexBufferObject);
    webGL.bufferData(webGL.ELEMENT_ARRAY_BUFFER, new Uint16Array(boxIndices), webGL.STATIC_DRAW);

    // Now we need to tell the vertex shader that the triangle vertices are meant for him
    // So first we will get the location of the vertex shader attribute vertPosition
    var positionAttributeLocation = webGL.getAttribLocation(webGLContext.program, "vertPosition");
    var colorAttributeLocation = webGL.getAttribLocation(webGLContext.program, "vertColor");

    // Now we need to specify the layout of the attribute
    webGL.vertexAttribPointer(
        positionAttributeLocation, // Location
        3, // Number of elements per attribute (vec2),
        webGL.FLOAT, // type of elements
        webGL.FALSE, // normalized
        6 * Float32Array.BYTES_PER_ELEMENT, // Size of an individual vertex (BYTES_PER_ELEMENT holds the number 4)
        0 // Offset from the beginning of a single vertex to this attribute 
    )

    webGL.vertexAttribPointer(
        colorAttributeLocation, // Location
        3, // Number of elements per attribute (vec2),
        webGL.FLOAT, // type of elements
        webGL.FALSE, // normalized
        6 * Float32Array.BYTES_PER_ELEMENT, // Size of an individual vertex (BYTES_PER_ELEMENT holds the number 4)
        3 * Float32Array.BYTES_PER_ELEMENT // Offset from the beginning of a single vertex to this attribute 
    )

    webGL.enableVertexAttribArray(positionAttributeLocation);
    webGL.enableVertexAttribArray(colorAttributeLocation);

    // To get the uniform values from the vertex shader we need to get their location
    var matWorldUniformLocation = webGL.getUniformLocation(webGLContext.program, "mWorld");
    var matViewUniformLocation = webGL.getUniformLocation(webGLContext.program, "mView");
    var matProjUniformLocation = webGL.getUniformLocation(webGLContext.program, "mProj");

    // Create the matrices
    var worldMatrix = new Float32Array(16);
    var viewMatrix = new Float32Array(16);
    var projMatrix = new Float32Array(16);
    var xRotationMatrix = new Float32Array(16);
    var yRotationMatrix = new Float32Array(16);

    // Make the matrices identity matrices
    mat4.identity(worldMatrix);
    mat4.lookAt(viewMatrix, [0, 2, -8], [0, 0, 0], [0, 1, 0]);
    mat4.perspective(projMatrix, glMatrix.toRadian(45), canvas.width / canvas.height, 0.1, 1000.0);

    // Now we will send these matrices to our shader
    webGL.uniformMatrix4fv(matWorldUniformLocation, webGL.FALSE, worldMatrix);
    webGL.uniformMatrix4fv(matViewUniformLocation, webGL.FALSE, viewMatrix);
    webGL.uniformMatrix4fv(matProjUniformLocation, webGL.FALSE, projMatrix);

    webGL.enable(webGL.DEPTH_TEST);
    webGL.enable(webGL.CULL_FACE);
    webGL.cullFace(webGL.BACK);
    webGL.frontFace(webGL.CCW);

    // Draw triangle to screen
    webGL.useProgram(webGLContext.program);
    

    // Now the loop will constantly rotate the triangle
    var identityMatrix = new Float32Array(16);
    mat4.identity(identityMatrix);
    var angle = 0;
    var loop = function () {
        
        angle = performance.now() / 1000 / 6 * 2 * Math.PI;
        mat4.rotate(xRotationMatrix, identityMatrix, angle, [0, 1, 0]);
        mat4.rotate(yRotationMatrix, identityMatrix, angle / 4, [1, 0, 0]);
        mat4.mul(worldMatrix, xRotationMatrix, yRotationMatrix);
        webGL.uniformMatrix4fv(matWorldUniformLocation, webGL.FALSE, worldMatrix);

        webGL.clearColor(0.0, 0.0, 0.0, 0.1);
        webGL.clear(webGL.COLOR_BUFFER_BIT | webGL.DEPTH_BUFFER_BIT);

        webGL.drawElements(
            webGL.TRIANGLES, // triangles
            boxIndices.length, 
            webGL.UNSIGNED_SHORT,
            0 
        )

        requestAnimationFrame(loop);

    }
    requestAnimationFrame(loop);
    
    console.log("It works!");

}



// --- HELPER FUNCTIONS
function initializeWebGL (webGL) {

    // Set color
    webGL.clearColor(0.0, 0.0, 0.0, 0.02);
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