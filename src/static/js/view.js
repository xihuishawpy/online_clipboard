document.addEventListener('DOMContentLoaded', () => {
    const passwordForm = document.getElementById('password-form');
    const passwordInput = document.getElementById('password');
    const submitPasswordButton = document.getElementById('submit-password');
    const contentDisplay = document.getElementById('content-display');
    const contentPre = document.getElementById('content');
    const createdAtSpan = document.getElementById('created-at');
    const burnNotice = document.getElementById('burn-notice');
    const errorMessage = document.getElementById('error-message');

    async function fetchContent(password = '') {
        try {
            const response = await fetch(`/api/paste/${PASTE_ID}?password=${password}`);
            const data = await response.json();

            if (response.ok) {
                contentPre.textContent = data.content;
                createdAtSpan.textContent = `创建时间：${new Date(data.created_at).toLocaleString()}`;
                contentDisplay.classList.remove('hidden');
                passwordForm.classList.add('hidden');
                errorMessage.classList.add('hidden');

                if (data.burn_after_read) {
                    burnNotice.classList.remove('hidden');
                }
            } else {
                if (response.status === 403) {
                    passwordForm.classList.remove('hidden');
                    errorMessage.textContent = '密码错误';
                    errorMessage.classList.remove('hidden');
                } else {
                    errorMessage.textContent = data.error || '内容不存在或已过期';
                    errorMessage.classList.remove('hidden');
                }
            }
        } catch (error) {
            errorMessage.textContent = '网络错误，请稍后重试';
            errorMessage.classList.remove('hidden');
        }
    }

    // 首次加载尝试无密码访问
    fetchContent();

    submitPasswordButton.addEventListener('click', () => {
        fetchContent(passwordInput.value);
    });

    passwordInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            fetchContent(passwordInput.value);
        }
    });
}); 