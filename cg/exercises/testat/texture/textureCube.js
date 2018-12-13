/*
    Define a wire frame cube with methods for drawing it.

    * @param gl the webgl context
    * @param color the color of the cube
    * @returns object with draw method
    * @constructor
 */

function TextureFrameCube(gl) {

    function defineVertices(gl) {
        var vertices = [
            // back
            -0.5,-0.5,-0.5, //v0
            0.5,-0.5,-0.5,  //v1
            -0.5,0.5,-0.5,  //v2
            0.5,0.5,-0.5,   //v3

            // left
            -0.5,-0.5,-0.5, //v4
            -0.5,0.5,-0.5,  //v5
            -0.5,-0.5,0.5,  //v6
            -0.5,0.5,0.5,   //v7

            // front
            -0.5,-0.5,0.5,  //v8
            -0.5,0.5,0.5,   //v9
            0.5,-0.5,0.5,   //v10
            0.5,0.5,0.5,    //v11

            // right
            0.5,-0.5,-0.5,  //v12
            0.5,0.5,-0.5,   //v13
            0.5,-0.5,0.5,   //v14
            0.5,0.5,0.5,    //v15

            // top
            0.5,0.5,-0.5,   //v16
            -0.5,0.5,-0.5,  //v17
            0.5,0.5,0.5,    //v18
            -0.5,0.5,0.5,   //v19

            // bottom
            -0.5,-0.5,-0.5, //v20
            0.5,-0.5,-0.5,  //v21
            -0.5,-0.5,0.5,  //v22
            0.5,-0.5,0.5    //v23


        ];

        var buffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);

        return buffer;
    }

    function defineTexture(gl) {

        var texture = [
            1,0,
            0,0,
            1,1,
            0,1,

            0,0,
            0,1,
            1,0,
            1,1,

            0,0,
            0,1,
            1,0,
            1,1,

            0,0,
            0,1,
            1,0,
            1,1,

            0,0,
            0,1,
            1,0,
            1,1,

            0,0,
            0,1,
            1,0,
            1,1

        ];

        var buffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(texture), gl.STATIC_DRAW);

        return buffer;
    }

    function defineEdges(gl) {
        // Verbindung zwischen den Vertices
        var vertexIndices = [
            //back
            0,1,2,
            1,2,3,

            //left
            4,5,6,
            5,6,7,

            //front
            8,9,10,
            9,10,11,

            //right
            12,13,14,
            13,14,15,

            // top
            16,17,18,
            17,18,19,

            //bottom
            20,21,22,
            21,22,23
        ];

        var buffer = gl.createBuffer();
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(vertexIndices), gl.STATIC_DRAW);

        return buffer;

    }




    return {

        bufferVertices: defineVertices(gl),
        bufferTexture: defineTexture(gl),
        bufferEdges: defineEdges(gl),
        draw: function(gl, aVertexPositionId, aVertexTextureCoordId, textureObj) {

            gl.bindBuffer(gl.ARRAY_BUFFER, this.bufferVertices);
            gl.vertexAttribPointer(aVertexPositionId, 3, gl.FLOAT, false, 0, 0);
            gl.enableVertexAttribArray(aVertexPositionId);

            gl.bindBuffer(gl.ARRAY_BUFFER, this.bufferTexture);
            gl.vertexAttribPointer(aVertexTextureCoordId, 2, gl.FLOAT, false, 0, 0);
            gl.enableVertexAttribArray(aVertexTextureCoordId);

            gl.bindTexture(gl.TEXTURE_2D, textureObj);
            gl.activeTexture(gl.TEXTURE0);

            gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.bufferEdges);
            gl.drawElements(gl.TRIANGLES, 36 ,gl.UNSIGNED_SHORT, 0);

        }

    }
}