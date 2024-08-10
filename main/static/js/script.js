// Desabilitar rolagem em desktop
if (window.innerWidth >= 768) {
    document.body.style.overflow = 'hidden';
} else {
    document.body.style.overflow = 'auto'; // Permitir rolagem em dispositivos móveis
}

function toggleScroll() {
    if (window.innerWidth >= 768) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }
}

// Executa ao carregar a página
toggleScroll();

// Executa ao redimensionar a janela
window.addEventListener('resize', toggleScroll);