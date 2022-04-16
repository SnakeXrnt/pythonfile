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

        drawCircle(color) {
            let x = this.column * blockSize;
            let y = this.row * blockSize;
            this.color = color;
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(x + blockSize / 2, y + blockSize / 2, blockSize / 2, 0, Math.PI * 2, true);
            ctx.fill();
        }
    }

    class Snake {
        
        constructor(){
            this.segments = [
                new Block(7,5),
                new Block(6,5),
                new Block(5,5),
            ]
        }

        draw() {
            this.segments.forEach((segment) => {
                segment.drawSquare("green");
            });
        }
    }

    border.draw();
    let snake = new Snake();
    snake.draw();
    // let block = new Block(4,5);
    // block.drawSquare("red");


})