const navEl = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (navEl && window.pageYOffset >= 50) {
        navEl.classList.add('navbar-scrolled');
    } else if (navEl && window.pageYOffset < 50) {
        navEl.classList.remove('navbar-scrolled');
    }
})