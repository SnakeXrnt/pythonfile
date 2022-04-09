function setup() {
    createCanvas(400,400);
    console.log('Okey');
    noStroke();
    frameRate(24);


}

function draw() {
    background(121);
    fill(255,0,0,160);
    eclipse (200,200,100,200);

    fill(0,255,0,160);
    eclipse (200,200,100,100);
    console.log("Ok MainlOOP");
}