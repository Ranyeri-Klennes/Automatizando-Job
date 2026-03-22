# Desktop Automation Bot ☕🤖

<img width="1366" height="768" alt="Demonstração do Bot de Automação" src="https://github.com/user-attachments/assets/a1d44cb4-f98e-4e09-a58a-5cded5a0f79e" />

---

## ✨ A Ideia por trás do Projeto

Sabe aqueles primeiros 10 ou 15 minutos do dia em que a gente só fica abrindo abas, fazendo logins e organizando janelas antes de realmente começar a trabalhar? 

Este projeto nasceu para acabar com essa "fricção" matinal. Criei um script em Python que assume as tarefas repetitivas de configuração do ambiente, para que eu (ou você) possa focar no que realmente importa desde o primeiro segundo.

**Em resumo:** Eu ganho tempo de foco e, de quebra, o bot me deseja um bom dia quando termina.

---

## 🚀 O que ele faz na prática?

O fluxo é pensado para ser o mais simples possível:

1.  **Ativação:** Assim que ligo o notebook, rodo o comando principal.
2.  **Automação:** Enquanto vou buscar um café, o PyAutoGUI assume o controle do mouse e teclado, abre os softwares necessários, organiza o layout das janelas e faz os logins iniciais.
3.  **Check-point:** Ao retornar à mesa, encontro tudo pronto e uma mensagem personalizada:
    > *"Tudo certo Rany, tenha um ótimo dia!"*

---

## 🛠️ Tecnologias e Ferramentas

Escolhi ferramentas leves e poderosas para garantir que a automação seja rápida:

* **Python:** A base de tudo, pela simplicidade e legibilidade.
* **PyAutoGUI:** A biblioteca mágica que permite ao script "enxergar" a tela e simular movimentos humanos de mouse e teclado.

---

## 📖 Como usar (mesmo se você não for dev)

Se você quer testar ou adaptar para o seu dia a dia, siga estes passos:

### 1. Preparando o terreno
Você vai precisar do Python instalado no seu computador. Depois, abra o seu terminal (ou CMD) e instale a biblioteca necessária:
```bash
pip install pyautogui
