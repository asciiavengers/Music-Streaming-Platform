document.addEventListener('DOMContentLoaded', function() {
    const songItems = document.querySelectorAll('song-item');
    const audioPlayer = document.getElementById('audio-player');

    songItems.forEach(item => {
        item.addEventListener('click', function() {
            const songSrc = this.getAttribute('data-src');
            audioPlayer.src = songSrc;
            audioPlayer.play();
        });
    });
});