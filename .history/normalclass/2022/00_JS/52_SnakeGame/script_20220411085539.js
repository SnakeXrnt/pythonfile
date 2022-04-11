document.addEventListener('DOMContentLoaded',() => {
    let canvas = documeny.getElementById('canvas');
    let ctx = canvas.getContext('2d');
    // console.log(canvas.width,canvas.height);

    const column = canvas.width / 20;
    const row = column;

    const blockSize = canvas.width / column;

    const  border = {
        color : 'Black',
        size : blockSize,
        width : canvas.width,
        height : canvas.height,

        draw : () => {
            ctx.fillStyle = this.color;
            const top = ctx.fillRect(0,0,this.width,this.size);
        }
    }


})