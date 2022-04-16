document.addEventListener('DOMContentLoaded', () => {

    let canvas = document.getElementById("canvas");
    let ctx = canvas.getContext("2d");

    //console.log(canvas.width, canvas.height)

    const blockSize = 20;
    const column = canvas.width / 20;
    const row = column;

    const border = {

        color : "black",
        size : blockSize,
        width : canvas.width,
        height : canvas.height,

        draw : function() {

            ctx.fillStyle = this.color;
            const top = ctx.fillRect(0, 0, this.width, this.size);
            const right = ctx.fillRect(this.width-this.size, 0, this.size, this.height);
            const bottom = ctx.fillRect(0, this.height-this.size, this.width, this.size);
            const left = ctx.fillRect(0, 0, this.size, this.height);
        }

    }

    class Block {
        constructor(row , column ){
            this.row = row;
            this.column = column;
            this.size = blockSize;
            
        }

        drawSquare(color) {
            let x = this.column * blockSize;
            let y = this.row * blockSize;
            this.color = color;
            ctx.fillStyle = this.color;
            ctx.fillRect(x, y, this.size, this.size);

        }
    }

    class Snake {
        
        constructor(){
            this.body = [];
            this.body.push(new Block(0,0));
            this.body.push(new Block(0,1));
            this.body.push(new Block(0,2));
            this.body.push(new Block(0,3));
            this.body.push(new Block(0,4));
            this.body.push(new Block(0,5));
            this.body.push(new Block(0,6));
            this.body.push(new Block(0,7));
            this.body.push(new Block(0,8));
            this.body.push(new Block(0,9));
            this.body.push(new Block(0,10));
            this.body.push(new Block(0,11));
            this.body.push(new Block(0,12));
            this.body.push(new Block(0,13));
            this.body.push(new Block(0,14));
            this.body.push(new Block(0,15));
            this.body.push(new Block(0,16));
            this.body.push(new Block(0,17));
            this.body.push(new Block(0,18));
            this.body.push(new Block(0,19));
            this.body.push(new Block(0,20));
            this.body.push(new Block(0,21));
            this.body.push(new Block(0,22));
            this.body.push(new Block(0,23));
            this.body.push(new Block(0,24));
            this.body.push(new Block(0,25));
            this.body.push(new Block(0,26));
            this.body.push(new Block(0,27));
            this.body.push(new Block(0,28));
            this.body.push(new Block(0,29));
            this.body.push(new Block(0,30));
            this.body.push(new Block(0,31));
            this.body.push(new Block(0,
        }
    }

    border.draw();
    let block = new Block(4,5);
    block.drawSquare("red");


})