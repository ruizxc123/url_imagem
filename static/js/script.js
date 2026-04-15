function copiarUrl() {
    const urlElement = document.getElementById('imageUrl');
    const btnElement = document.getElementById('copyBtn');
    const url = urlElement.href;
    
    // API moderna de Clipboard
    navigator.clipboard.writeText(url).then(() => {
        // Feedback visual amigável
        const textoOriginal = btnElement.innerText;
        btnElement.innerText = 'Copiado!';
        btnElement.classList.add('success');
        
        // Volta ao normal após 2 segundos
        setTimeout(() => {
            btnElement.innerText = textoOriginal;
            btnElement.classList.remove('success');
        }, 2000);
        
    }).catch(err => {
        console.error('Falha ao copiar: ', err);
        alert('Não foi possível copiar a URL. Selecione o link e copie manualmente.');
    });
}