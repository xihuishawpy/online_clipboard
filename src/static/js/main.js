document.addEventListener('DOMContentLoaded', () => {
    const contentTextarea = document.getElementById('content');
    const passwordInput = document.getElementById('password');
    const expireTimeSelect = document.getElementById('expireTime');
    const burnAfterReadCheckbox = document.getElementById('burnAfterRead');
    const submitButton = document.getElementById('submit');
    const resultDiv = document.getElementById('result');
    const shareUrlInput = document.getElementById('shareUrl');
    const copyUrlButton = document.getElementById('copyUrl');

    submitButton.addEventListener('click', async () => {
        const content = contentTextarea.value.trim();
        if (!content) {
            alert('请输入内容');
            return;
        }

        const data = {
            content,
            password: passwordInput.value,
            expireTime: expireTimeSelect.value,
            burnAfterRead: burnAfterReadCheckbox.checked
        };

        try {
            const response = await fetch('/api/paste', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            
            if (response.ok) {
                const url = `${window.location.origin}${result.url}`;
                shareUrlInput.value = url;
                resultDiv.classList.remove('hidden');
            } else {
                alert(result.error || '创建失败');
            }
        } catch (error) {
            alert('网络错误，请稍后重试');
        }
    });

    copyUrlButton.addEventListener('click', () => {
        shareUrlInput.select();
        document.execCommand('copy');
        copyUrlButton.textContent = '已复制';
        setTimeout(() => {
            copyUrlButton.textContent = '复制';
        }, 2000);
    });
}); 