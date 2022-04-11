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
    border.draw();
    
})