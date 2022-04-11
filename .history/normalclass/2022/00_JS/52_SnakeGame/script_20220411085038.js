document.addEventListener('DOMContentLoaded',() => {
    let canvas = documeny.getElementById('canvas');
    let ctx = canvas.getContext('2d');
    // console.log(canvas.width,canvas.height);

    const column = canvas.width / 20;
    const row = column;

    const blockSize = canvas.width / column;

    console.log (column , row , blockSize);

    

})