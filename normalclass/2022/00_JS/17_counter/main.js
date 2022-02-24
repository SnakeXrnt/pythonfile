let counter = 0;

let count = () => {
    counter++;
    
    $("counter").text(counter);
    if (counter % 10 === 0){
        alert(`counternya sudah ${counter}`);
    }
}