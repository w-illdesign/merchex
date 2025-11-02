document.addEventListener('DOMContentLoaded', () => {

    function createRipple(e) {
        const target = e.currentTarget;

        // Créer le ripple
        const ripple = document.createElement('span');
        ripple.className = 'ripple';

        // Taille du ripple = plus grand côté de l'élément
        const rect = target.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        ripple.style.width = ripple.style.height = size + 'px';

        // Position centrée sur le clic
        ripple.style.left = (e.clientX - rect.left - size / 2) + 'px';
        ripple.style.top = (e.clientY - rect.top - size / 2) + 'px';

        // Ajouter le ripple à l'élément
        target.appendChild(ripple);

        // Supprimer après animation
        ripple.addEventListener('animationend', () => ripple.remove());
    }

    // Fonction pour attacher le ripple aux éléments existants et futurs
    function attachRipples(root = document) {
        const elements = root.querySelectorAll('a, button');
        elements.forEach(el => {
            if (!el.hasAttribute('data-ripple')) {
                el.setAttribute('data-ripple', 'true');
                el.addEventListener('click', createRipple);
            }
        });
    }

    // Attacher aux éléments existants
    attachRipples();

    // Observer le DOM pour les éléments ajoutés dynamiquement
    const observer = new MutationObserver(mutations => {
        mutations.forEach(m => {
            m.addedNodes.forEach(node => {
                if (node.nodeType === 1) attachRipples(node);
            });
        });
    });

    observer.observe(document.body, { childList: true, subtree: true });

});