# Sistema de Agendamento Clínico

Uma aplicação simples desenvolvida em Python para gerenciar consultas em uma clínica local.


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

## Capturas de Tela

![Captura 1](capturas\print 1.png)
![Captura 2](capturas\print 2.png)
