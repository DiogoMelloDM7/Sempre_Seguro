function excluirItem(itemId) {
        if (confirm("Tem certeza que deseja excluir este produto?")) {
            const csrftoken = getCookie('csrftoken');
            fetch(`/excluiritem/${itemId}/`, {
                method: "DELETE",
                headers: {
                    "X-CSRFToken": csrftoken,
                },
            })
            .then((response) => {
                if (response.ok) {
                    location.reload(); // Atualiza a página após excluir o item
                } else {
                    alert("Ocorreu um erro ao excluir o produto.");
                }
            })
            .catch((error) => {
                console.error("Erro na solicitação AJAX:", error);
            });
        }
    }

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se o cookie começa com o nome do token CSRF
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function excluirRelatorio(relatorioId) {
    if (confirm("Tem certeza que deseja excluir este relatório?")) {
        const csrftoken = getCookie('csrftoken');
        fetch(`/excluir-relatorio/${relatorioId}/`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": csrftoken,

            },
        })
        .then((response) => {
            if (response.ok) {
                 window.location.href = '/relatorios/' // Atualiza a página após excluir o item
            } else {
                alert("Ocorreu um erro ao excluir o relatório.");
            }
        })
        .catch((error) => {
            console.error("Erro na solicitação AJAX:", error);
        });
    }
}

function excluirContaFutura(contaId) {
    if (confirm("Tem certeza que deseja excluir esta conta?")) {
        const csrftoken = getCookie('csrftoken');
        fetch(`/delete_contas_avencer/${contaId}/`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": csrftoken,

            },
        })
        .then((response) => {
            if (response.ok) {
                 location.reload();
            } else {
                alert("Ocorreu um erro ao excluir a conta.");
            }
        })
        .catch((error) => {
            console.error("Erro na solicitação AJAX:", error);
        });
    }
}




