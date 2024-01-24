![Sistema de consultas Thumbnail](https://i.imgur.com/id45DXH.png)

# Sistema de Agendamento Clínico

Uma aplicação simples desenvolvida em Python para gerenciar consultas em uma clínica local.


## Como utilizar o projeto

1. **Clone o Repositório:**
   - Para rodar o projeto, é necessário primeiramente fazer um clone deste repositório. Utilize o seguinte comando no seu terminal:
     ```bash
     git clone https://github.com/mattheusp/sistema-clinica-Python
     ```

2. **Executar o Programa:**
   - Navegue até o diretório do projeto clonado e execute o programa em Python:
     ```bash
     cd sistema-clinica-Python
     python main.py
     ```

3. **Interagir com o Sistema:**
   - Escolha as opções do menu para cadastrar pacientes, marcar ou cancelar consultas.
   - Siga as instruções na tela para interagir com o sistema.
  
   4. **Persistência de Dados:**
   - Os dados são salvos automaticamente nos arquivos CSV para uso futuro.
   - Ao iniciar, o programa carrega automaticamente informações dos pacientes e consultas.


**Funcionalidades Implementadas:**

1. **Cadastro de Paciente:**
   - Cadastro simples com nome e telefone.
   - Evita duplicidade através da verificação do número de telefone.
   - Os dados dos pacientes são armazenados no arquivo `pacientes.csv`.

2. **Marcação de Consulta:**
   - Permite escolher um paciente e agendar uma consulta.
   - Verifica disponibilidade do horário e impede que seja realizados agendamentos retroativos.
   - As consultas agendadas são salvas no arquivo `consultas.csv`.

3. **Cancelamento de Consulta:**
   - Permite cancelar consultas existentes.
   - Mostra detalhes antes de confirmar o cancelamento.

4. **Persistência de Dados:**
   - É utilizado arquivos CSV para persistência dos dados entre execuções.
   - Ao iniciar, carrega automaticamente informações dos pacientes e consultas.

5. **Tratamento de Erros:**
   - Evita cadastros duplicados e agendamentos em horários ocupados.
   - As mensagens de erro vão ser visiveis para orientar o usuário.

   
**Instruções de Uso:**

1. Execute o programa em Python.
2. Escolha opções do menu para cadastrar pacientes, marcar ou cancelar consultas.
3. Os dados são salvos automaticamente nos arquivos CSV para uso futuro.

## Ferramentas utilizadas:
    - JavaScript
    - Html
    - CSS

## Capturas de Tela

![Captura 1](capturas/print%201.png)
![Captura 2](capturas/print%202.png)

## Contato ✉️

- Email: mattheusp382@gmail.com
- LinkedIn: [Mattheus-Pereira](https://www.linkedin.com/in/mattheuspereira/)
- Portfolio: [mtp-dev.com](https://mtpdev.com.br/)

## Contribuição 🤝

Se você quiser contribuir com um projeto ou encontrar um problema, sinta-se à vontade para abrir um novo problema ou enviar uma solicitação pull. Qualquer contribuição é bem-vinda!

## Licença📄

Este portfólio está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
