# 🐍 Snake Game

Este projeto foi desenvolvido em grupo no âmbito da Unidade Curricular de **Introdução à Programação e Resolução de Problemas**.

## 📝 Descrição do Projeto
O objetivo principal deste trabalho foi consolidar competências de resolução de problemas e programação em **Python** através da implementação do clássico jogo "Snake". No jogo, o utilizador controla a cabeça de uma cobra que deve colecionar pedaços de comida gerados aleatoriamente, crescendo a cada refeição e evitando colisões com as paredes ou com o próprio corpo.

## 🛠️ Funcionalidades Implementadas
- **Movimentação Dinâmica:** Controlo da cobra nas 4 direções (Cima, Baixo, Esquerda, Direita). O movimento é realizado através do teclado, utilizando as teclas W (Cima), S (Baixo), A (Esquerda) e D (Direita).
- **Lógica de Colisões:** Deteção precisa de colisões com os limites do ambiente e com o corpo da cobra.
- **Gestão de Itens:** Geração aleatória de comida dentro dos limites de jogo e sistema de crescimento.
- **Sistema de Pontuação:** Incremento de 10 pontos por cada comida ingerida.
- **Persistencia de dados:** Gravação e leitura de *high-scores* num ficheiro externo.

## 💻 Tecnologias Utilizadas
- **Linguagem:** Python.
- **Bibliotecas:** Turtle Graphics (usada para a interface visual).

## 🚀 Como Executar
1. Certifica-te de que tens o Python instalado.
2. Clona este repositório.
3. Executa o ficheiro principal:
   ```bash
   python snake.py
