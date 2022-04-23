document.addEventListener('DOMContentLoaded', () => {

    let canvas = document.getElementById("canvas");
    let ctx = canvas.getContext("2d");

    //console.log(canvas.width, canvas.height)

    const blockSize = 20;
    const column = canvas.width / 20;
    let score = 0
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

    let scoreText = {
        font : "20px Arial",
        color : "white",
        align : "left",
        baseline : "top",
        size : blockSize,

        draw : function() {
                const x = 0;
                const y = 0;
                ctx.font = this.font;
                ctx.fillStyle = this.color;
                ctx.textAlign = this.align;
                ctx.textBaseline = this.baseline;
                ctx.fillText("   Score : " + score, x, y);
        }
    }

    const gameOverText = {
        font : "30px Arial",
        color : "black",
        align : "left",
        baseline : "middle",
        size : blockSize,

        draw : function() {
            clearInterval(mainloop);
                const x = 0;
                const y = 0;
                ctx.font = this.font;
                ctx.fillStyle = this.color;
                ctx.textAlign = this.align;
                ctx.textBaseline = this.baseline;
                ctx.fillText("Game Over", x, y);
        }
    }

    class Block {
        constructor(row , column ){
            this.row = row;
            this.column = column;
            this.size = blockSize;
            
        }

        circle(x, y, radius, color,isFilled) {
            ctx.strokeStyle = color;
            ctx.fillStyle = color;
            ctx.beginPath();
            ctx.arc(x , y , radius , 0 , 2 * Math.PI);
            ctx.stroke();
            if(isFilled) {
                ctx.fill();
            }
        }

        drawSquare(color) {
            let x = this.column * blockSize;
            let y = this.row * blockSize;
            this.color = color;
            ctx.fillStyle = this.color;
            ctx.fillRect(x, y, this.size, this.size);

        }

        drawCircle(color) {
            let x = this.column * this.size;
            let y = this.row * this.size;
            this.color = color;

            this.circle(x, y, this.size/2, this.color,true);
        }
    }

    class Apple {

        constructor(){
            this.block = new Block(0,0);
            this.move();
        }

        draw(){
            this.block.drawCircle("red");
        }

        move(){
            let randomRow = Math.floor(Math.random() * (row-2));
            let randomColumn = Math.floor(Math.random() * (column-2));
            this.block.row = randomRow;
            this.block.column = randomColumn;
        }
    }

    class Snake {
        
        constructor(){
            this.segments = [
                new Block(7,5),
                new Block(6,5),
                new Block(5,5),
            ]
            this.direction = "right";
            this.nextDirection = "right";

        }

        draw() {
            this.segments.forEach((segment) => {
                segment.drawSquare("green");
            });
        }

        setDirection(newDirection) {
            if (this.direction === "up" && newDirection === "down") {
                return;
            }
            if (this.direction === "down" && newDirection === "up") {
                return;
            }
            if (this.direction === "left" && newDirection === "right") {
                return;
            }
            if (this.direction === "right" && newDirection === "left") {
                return;
            }   
            console.log(newDirection);
            this.nextDirection = newDirection;
        }

        move(){
            let head = this.segments[0];
            let newHead;

            this.direction = this.nextDirection;

            if(this.direction === "right") newHead = new Block(head.row, head.column + 1);
            else if(this.direction === "left") newHead = new Block(head.row, head.column - 1);
            else if(this.direction === "up") newHead = new Block(head.row - 1, head.column);
            else if(this.direction === "down") newHead = new Block(head.row + 1, head.column);

            this.segments.unshift(newHead);
            this.segments.pop()
        }

        CheckCollision(head){
            const leftCollision = (head.column === 0);
            const rightCollision = (head.column === column - 1);
            const topCollision = (head.row === 0);
            const bottomCollision = (head.row === row - 1);
            const wallCollision = (leftCollision || rightCollision || topCollision || bottomCollision);
        }
    }

    let snake = new Snake()
    let apple = new Apple()

    let mainloop = setInterval(() => {
        ctx.clearRect(0,0,canvas.width ,canvas.height);
        border.draw();
        scoreText.draw();
        snake.draw();
        snake.move();
        apple.draw();
    }, 200)

    document.addEventListener('keydown', (event) => {
        switch (event.code) {
            case "KeyW":
                snake.setDirection("up");
                break;
            case "KeyA":
                snake.setDirection("left");
                break;
            case "KeyS":
                snake.setDirection("down");
                break;
            case "KeyD":
                snake.setDirection("right");
                break;


            default:
                console.log(undefined)
        }
    })
    // let block = new Block(4,5);
    // block.drawSquare("red");


})