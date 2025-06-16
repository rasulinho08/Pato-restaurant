const buttons = document.querySelectorAll('.gallerybuttons button');
const photos = document.querySelectorAll('.galleryphotos > div');

buttons.forEach(button => {
  button.addEventListener('click', () => {
    // Remove active class on buttons
    buttons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');

    const filter = button.getAttribute('data-filter');

    photos.forEach(photo => {
      if (filter === 'all') {
        photo.classList.remove('hidden');
      } else {
        if (photo.classList.contains(filter)) {
          photo.classList.remove('hidden');
        } else {
          photo.classList.add('hidden');
        }
      }
    });
  });
});





