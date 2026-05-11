document.addEventListener('DOMContentLoaded', () => {
    // 1. URL'den model parametresini al
    const urlParams = new URLSearchParams(window.location.search);
    const modelType = urlParams.get('model') || 'emlak'; // default emlak
    
    // 2. UI Elementlerini Seç
    const modelInfo = document.getElementById('model-info');
    const modelName = document.getElementById('model-name');
    const modelDesc = document.getElementById('model-desc');
    const modelIcon = document.getElementById('model-icon');
    const glow = document.getElementById('dynamic-glow');
    const sendBtn = document.getElementById('send-btn');
    
    // 3. Modele göre temayı ve metinleri ayarla
    if (modelType === 'hotel') {
        document.body.classList.add('theme-hotel');
        modelName.innerText = "HotelMind AI";
        modelDesc.innerText = "Otel Asistanı";
        modelIcon.innerHTML = '<i class="fa-solid fa-hotel"></i>';
        glow.style.background = 'var(--hotel-color)';
    } else {
        document.body.classList.add('theme-emlak');
        modelName.innerText = "Emlak AI";
        modelDesc.innerText = "Emlak Asistanı";
        modelIcon.innerHTML = '<i class="fa-solid fa-building"></i>';
        glow.style.background = 'var(--emlak-color)';
    }

    // 4. Chat Mantığı
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    
    // Basit bir User ID oluştur
    let userId = localStorage.getItem('nexus_user_id');
    if(!userId) {
        userId = 'user_' + Math.random().toString(36).substr(2, 9);
        localStorage.setItem('nexus_user_id', userId);
    }

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = userInput.value.trim();
        if (!message) return;
        
        // Kullanıcı mesajını ekle
        appendMessage('user', message);
        userInput.value = '';
        
        // Yükleniyor animasyonu
        const loadingId = appendLoading();
        
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    user_id: userId,
                    message: message,
                    model_type: modelType
                })
            });
            
            const data = await response.json();
            
            // Yükleniyoru kaldır ve cevabı yazdır
            document.getElementById(loadingId).remove();
            appendMessage('assistant', data.response);
            
        } catch (error) {
            console.error("Hata:", error);
            document.getElementById(loadingId).remove();
            appendMessage('assistant', "Bir hata oluştu. Lütfen tekrar deneyin.");
        }
    });

    function appendMessage(role, text) {
        const div = document.createElement('div');
        div.className = `message ${role}`;
        
        let iconHtml = role === 'user' ? '<i class="fa-solid fa-user"></i>' : (modelType === 'hotel' ? '<i class="fa-solid fa-hotel"></i>' : '<i class="fa-solid fa-building"></i>');
        
        // Marked.js ile markdown'ı HTML'e çevir
        const formattedText = role === 'assistant' ? marked.parse(text) : text;
        
        div.innerHTML = `
            <div class="avatar">${iconHtml}</div>
            <div class="bubble">${formattedText}</div>
        `;
        
        chatMessages.appendChild(div);
        scrollToBottom();
    }
    
    function appendLoading() {
        const id = 'loading-' + Date.now();
        const div = document.createElement('div');
        div.className = `message assistant loading-msg`;
        div.id = id;
        
        let iconHtml = modelType === 'hotel' ? '<i class="fa-solid fa-hotel"></i>' : '<i class="fa-solid fa-building"></i>';
        
        div.innerHTML = `
            <div class="avatar">${iconHtml}</div>
            <div class="bubble">
                <div class="typing-indicator">
                    <span></span><span></span><span></span>
                </div>
            </div>
        `;
        
        chatMessages.appendChild(div);
        scrollToBottom();
        return id;
    }
    
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    document.getElementById('clear-chat').addEventListener('click', () => {
        if(confirm('Sohbet geçmişini temizlemek istiyor musunuz?')) {
            chatMessages.innerHTML = `
                <div class="message assistant">
                    <div class="avatar"><i class="fa-solid fa-robot"></i></div>
                    <div class="bubble">Sohbet temizlendi. Size nasıl yardımcı olabilirim?</div>
                </div>
            `;
        }
    });
});
