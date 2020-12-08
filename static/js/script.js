for (let tupel of document.querySelectorAll('video')) {
    tupel.addEventListener('mouseover', (e) => {
        e.target.play()
        e.target.muted = true;
    }, false);

    tupel.addEventListener('mouseout', (e) => {
        e.target.pause()
    }, false);
}