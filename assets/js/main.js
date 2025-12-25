/* =========================
   LANGUAGE TOGGLE
========================= */
const langToggle = document.getElementById('langToggle');
let isEnglish = false;

langToggle.addEventListener('click', () => {
  isEnglish = !isEnglish;
  document.body.classList.toggle('en-mode', isEnglish);
  langToggle.textContent = isEnglish ? 'VI' : 'EN';
});

/* =========================
   FILTER ALBUM
========================= */
const menuButtons = document.querySelectorAll('.album-menu button');
const galleryItems = document.querySelectorAll('.gallery a');

menuButtons.forEach(button => {
  button.addEventListener('click', () => {
    // active state
    menuButtons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');

    const filter = button.dataset.filter;

    galleryItems.forEach(item => {
      const category = item.dataset.category;

      if (filter === 'all' || category === filter) {
        item.style.display = 'block';
        setTimeout(() => item.classList.add('visible'), 50);
      } else {
        item.classList.remove('visible');
        setTimeout(() => {
          item.style.display = 'none';
        }, 200);
      }
    });
  });
});

/* =========================
   SCROLL FADE-IN
========================= */
const observer = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.15
  }
);

galleryItems.forEach(item => observer.observe(item));

/* =========================
   LIGHTBOX
========================= */
const lightbox = GLightbox({
  touchNavigation: true,
  loop: true,
  preload: true,
  zoomable: false,
  closeButton: true
});

/* =========================
   SMOOTH UX POLISH
========================= */
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    lightbox.close();
  }
});
