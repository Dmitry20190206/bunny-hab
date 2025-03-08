document.addEventListener('DOMContentLoaded', function() {
    // Обработка формы анализа кода
    const codeForm = document.getElementById('codeForm');
    if (codeForm) {
        codeForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const code = document.getElementById('code').value;
            const resultsDiv = document.getElementById('analysisResults');
            
            try {
                const response = await fetch('/code-analysis', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: `code=${encodeURIComponent(code)}`
                });
                
                const data = await response.json();
                
                let html = '';
                
                // Отображение проблем
                if (data.issues.length > 0) {
                    html += '<div class="alert alert-warning"><h6>Найденные проблемы:</h6><ul>';
                    data.issues.forEach(issue => {
                        html += `<li>${issue}</li>`;
                    });
                    html += '</ul></div>';
                } else {
                    html += '<div class="alert alert-success">Проблем не обнаружено</div>';
                }
                
                // Отображение предложений
                if (data.suggestions.length > 0) {
                    html += '<div class="alert alert-info"><h6>Предложения по улучшению:</h6><ul>';
                    data.suggestions.forEach(suggestion => {
                        html += `<li>${suggestion}</li>`;
                    });
                    html += '</ul></div>';
                }
                
                resultsDiv.innerHTML = html;
            } catch (error) {
                resultsDiv.innerHTML = `
                    <div class="alert alert-danger">
                        Произошла ошибка при анализе кода: ${error.message}
                    </div>
                `;
            }
        });
    }
    
    // Обработка чата
    const chatForm = document.getElementById('chatForm');
    if (chatForm) {
        chatForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const messageInput = document.getElementById('messageInput');
            const message = messageInput.value;
            const chatMessages = document.getElementById('chatMessages');
            
            // Добавляем сообщение пользователя
            chatMessages.innerHTML += `
                <div class="chat-message user">
                    <strong>Вы:</strong> ${message}
                </div>
            `;
            
            try {
                const response = await fetch('/chat/message', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message })
                });
                
                const data = await response.json();
                
                // Добавляем ответ ассистента
                chatMessages.innerHTML += `
                    <div class="chat-message assistant">
                        <strong>Ассистент:</strong> ${data.response}
                    </div>
                `;
                
                // Очищаем поле ввода
                messageInput.value = '';
                
                // Прокручиваем чат вниз
                chatMessages.scrollTop = chatMessages.scrollHeight;
            } catch (error) {
                chatMessages.innerHTML += `
                    <div class="alert alert-danger">
                        Произошла ошибка: ${error.message}
                    </div>
                `;
            }
        });
    }
}); 