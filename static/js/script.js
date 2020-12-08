for (let tupel of document.querySelectorAll('video')) {
    tupel.addEventListener('mouseover', (e) => {
        e.target.play()
    }, false);

    tupel.addEventListener('mouseout', (e) => {
        e.target.pause()
    }, false);
}