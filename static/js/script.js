for (let tupel of document.querySelectorAll('video')) {
    tupel.addEventListener('mouseover', (e) => {
        e.target.play()
        e.target.muted = true;
    }, false);

    tupel.addEventListener('mouseout', (e) => {
        e.target.pause()
    }, false);
}



function channeldropdown() {
    document.getElementById("channeldropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.channel_img')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}