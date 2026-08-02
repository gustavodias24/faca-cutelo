(() => {
    const body = document.body;
    const header = document.querySelector('[data-header]');
    const menuToggle = document.querySelector('[data-menu-toggle]');
    const nav = document.querySelector('[data-nav]');
    const lightbox = document.querySelector('[data-lightbox]');
    const lightboxImage = document.querySelector('[data-lightbox-image]');
    const lightboxClose = document.querySelector('[data-lightbox-close]');

    const updateHeader = () => {
        header?.classList.toggle('scrolled', window.scrollY > 24);
    };

    const closeMenu = () => {
        if (!menuToggle || !nav) return;
        menuToggle.setAttribute('aria-expanded', 'false');
        nav.classList.remove('is-open');
        body.classList.remove('menu-open');
    };

    menuToggle?.addEventListener('click', () => {
        const willOpen = menuToggle.getAttribute('aria-expanded') !== 'true';
        menuToggle.setAttribute('aria-expanded', String(willOpen));
        nav?.classList.toggle('is-open', willOpen);
        body.classList.toggle('menu-open', willOpen);
    });

    nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));

    window.addEventListener('scroll', updateHeader, { passive: true });
    window.addEventListener('resize', () => {
        if (window.innerWidth > 760) closeMenu();
    });
    updateHeader();

    const observer = 'IntersectionObserver' in window
        ? new IntersectionObserver((entries, currentObserver) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                entry.target.classList.add('is-visible');
                currentObserver.unobserve(entry.target);
            });
        }, { threshold: 0.13 })
        : null;

    document.querySelectorAll('.reveal').forEach((element) => {
        if (observer) observer.observe(element);
        else element.classList.add('is-visible');
    });

    const closeLightbox = () => {
        if (!lightbox?.open) return;
        lightbox.close();
        body.classList.remove('lightbox-open');
    };

    document.querySelectorAll('[data-gallery-src]').forEach((button) => {
        button.addEventListener('click', () => {
            if (!lightbox || !lightboxImage) return;
            lightboxImage.src = button.dataset.gallerySrc || '';
            lightboxImage.alt = button.querySelector('img')?.alt || 'Imagem ampliada do produto';
            lightbox.showModal();
            body.classList.add('lightbox-open');
        });
    });

    lightboxClose?.addEventListener('click', closeLightbox);
    lightbox?.addEventListener('click', (event) => {
        if (event.target === lightbox) closeLightbox();
    });
    lightbox?.addEventListener('close', () => body.classList.remove('lightbox-open'));

    document.querySelectorAll('[data-year]').forEach((element) => {
        element.textContent = String(new Date().getFullYear());
    });
})();
