# IronRacers Data Analysis

Manual de usuario do software de analise de dados da equipe Formula SAE Iron Racers.

Este documento foi escrito para que um novo membro da equipe consiga abrir o software, carregar os dados de teste, preencher as informacoes de pista e interpretar as paginas principais sem depender de orientacao externa.

## Sumario

1. [Visao geral](#visao-geral)
2. [Como acessar online pelo Streamlit Community Cloud](#como-acessar-online-pelo-streamlit-community-cloud)
3. [Como rodar localmente pelo GitHub](#como-rodar-localmente-pelo-github)
4. [Fluxo recomendado em um dia de teste](#fluxo-recomendado-em-um-dia-de-teste)
5. [Formato dos arquivos CSV e padrao de nomes](#formato-dos-arquivos-csv-e-padrao-de-nomes)
6. [Paginas funcionais](#paginas-funcionais)
7. [Paginas planejadas ou em desenvolvimento](#paginas-planejadas-ou-em-desenvolvimento)
8. [Boas praticas gerais](#boas-praticas-gerais)

# Visao geral

O **IronRacers Data Analysis** e um aplicativo Streamlit usado para registrar informacoes de teste, carregar logs do carro, comparar pilotos e apoiar decisoes de engenharia. O arquivo principal do aplicativo e:

```text
Performance.py
```

As paginas do menu lateral ficam na pasta:

```text
pages/
```

O software trabalha principalmente com dados guardados na memoria da sessao do Streamlit. Isso significa que as informacoes digitadas ficam disponiveis enquanto a sessao estiver aberta, mas podem ser perdidas ao recarregar o navegador, reiniciar o servidor ou fechar o app. Para registros oficiais, salve os logs originais e copie os comentarios importantes para o relatorio da equipe.

## Estado atual das paginas

| Pagina | Status no fluxo oficial | Uso principal |
|---|---:|---|
| Performance | Implementada | Planejamento do teste, selecao de pilotos, upload de logs e relatorio geral |
| General Conditions | Implementada | Massa do carro, massa do piloto, combustivel e temperaturas externas |
| Setup | Implementada | Registro de setup de freio, suspensao e amortecedores |
| Tires | Implementada | Temperaturas, pressoes e KPIs de pneus |
| Vital Signal | Implementada | Saude do carro: motor, bateria, oleo, combustivel e RPM |
| Driver | Implementada | Analise de pilotagem, acelerador, grip e tendencias |
| Drive Debriefings | Implementada | Feedback do piloto, notas, voltas e comparacao de ritmo |
| Project Validation | Planejada/em desenvolvimento | Ainda nao deve ser usada como fluxo oficial |
| Chassi | Planejada/em desenvolvimento | Ainda nao deve ser usada como fluxo oficial |
| Brake | Planejada/em desenvolvimento | Ainda nao deve ser usada como fluxo oficial |
| Powertrain | Planejada/em desenvolvimento | Ainda nao deve ser usada como fluxo oficial |
| Electronics PDM | Planejada/em desenvolvimento | Ainda nao deve ser usada como fluxo oficial |
| Aero | Planejada/em desenvolvimento | Ainda nao deve ser usada como fluxo oficial |
| Drivetrain | Planejada/em desenvolvimento | Ainda nao deve ser usada como fluxo oficial |
| Steering | Planejada/em desenvolvimento | Ainda nao deve ser usada como fluxo oficial |

# Como acessar online pelo Streamlit Community Cloud

Quando o app estiver publicado, a equipe deve fornecer um link do tipo:

```text
https://nome-do-app.streamlit.app
```

## Passo a passo para usuarios

1. Abra o link oficial enviado pela equipe Iron Racers.
2. Aguarde o Streamlit iniciar o aplicativo. Em apps gratuitos, a primeira abertura pode demorar alguns segundos porque o servidor pode estar "dormindo".
3. Se aparecer uma tela de login ou permissao, entre com a conta autorizada pela equipe.
4. Comece pela pagina **Performance**. Ela inicializa os pilotos, os dados gerais de teste e o upload de logs.
5. Use o menu lateral esquerdo para navegar entre as paginas.

## Passo a passo para mantenedores publicarem no Streamlit Cloud

1. Acesse [Streamlit Community Cloud](https://streamlit.io/cloud).
2. Conecte a conta do GitHub que tem acesso ao repositorio.
3. Selecione o repositorio:

```text
IronRacers/Data-Analysis-Software
```

4. Escolha a branch desejada, normalmente `main`.
5. No campo de arquivo principal, informe:

```text
Performance.py
```

6. Confirme o deploy.
7. Depois que o app abrir, copie o link gerado e compartilhe com a equipe.

# Como rodar localmente pelo GitHub

Rodar localmente e recomendado para desenvolvimento, testes sem internet ou uso em notebooks de pista.

## Requisitos

- Python 3.10 ou superior.
- Git instalado.
- Acesso ao repositorio no GitHub.
- Terminal PowerShell, CMD, Git Bash ou terminal integrado do VS Code.

## Instalacao

1. Clone o repositorio:

```bash
git clone https://github.com/IronRacers/Data-Analysis-Software.git
```

2. Entre na pasta do projeto:

```bash
cd Data-Analysis-Software
```

3. Crie um ambiente virtual:

```bash
python -m venv .venv
```

4. Ative o ambiente virtual no Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No CMD, use:

```bat
.venv\Scripts\activate.bat
```

No Linux/macOS, use:

```bash
source .venv/bin/activate
```

5. Instale as dependencias:

```bash
pip install -r requirements.txt
```

6. Execute o aplicativo:

```bash
streamlit run Performance.py
```

7. Abra o endereco exibido no terminal. Normalmente sera:

```text
http://localhost:8501
```

## Dependencias principais

O arquivo `requirements.txt` lista:

```text
streamlit
pandas
numpy
plotly
```

O app tambem usa imagens locais e a biblioteca `PIL`, normalmente instalada junto com dependencias usadas pelo Streamlit. Se aparecer erro relacionado a `PIL`, instale:

```bash
pip install pillow
```

# Fluxo recomendado em um dia de teste

1. Abra o app pela pagina **Performance**.
2. Preencha o objetivo do teste, local, pilotos, data e horarios.
3. Monte o planejamento do teste na tabela **Test Planing**.
4. Carregue os logs dos pilotos no campo **Select log**.
5. Confira se os arquivos aparecem em **Uploaded files**.
6. Va para **General Conditions** e registre massa, combustivel e temperaturas.
7. Va para **Setup** e registre o setup usado antes do stint.
8. Va para **Tires** e preencha pressoes/temperaturas antes e depois do teste.
9. Use **Vital Signal** para conferir se o carro operou dentro de limites aceitaveis.
10. Use **Driver** para comparar pilotagem, acelerador, velocidade e grip.
11. Use **Drive Debriefings** logo apos a volta para registrar feedback enquanto o piloto ainda lembra dos detalhes.
12. Ao final, copie conclusoes importantes para o relatorio oficial da equipe.

# Formato dos arquivos CSV e padrao de nomes

As paginas **Vital Signal** e **Driver** dependem dos logs carregados na pagina **Performance**. O software procura o arquivo de cada piloto pelo nome do arquivo.

## Padrao de nome obrigatorio

O nome do arquivo deve comecar exatamente com o nome do piloto selecionado na pagina **Performance**.

| Piloto selecionado | Nome aceito | Nome que pode falhar |
|---|---|---|
| Jenifer | `Jenifer_SkidPad_2026.csv` | `SkidPad_Jenifer.csv` |
| Muniz | `Muniz_Endurance_Run1.csv` | `MZ_Endurance.csv` |
| Rafael | `Rafael_Frenagem_60kmh.csv` | `Rafa_Frenagem.csv` |

Se o piloto selecionado for `Rafael`, a funcao de leitura procura um arquivo cujo nome comece com `Rafael`. Se o arquivo estiver como `IR04_Rafael.csv`, o software pode nao encontra-lo automaticamente.

## Formato do CSV

Use CSV com separador por virgula, codificacao UTF-8 e cabecalho na primeira linha.

Exemplo minimo recomendado:

```csv
TIME,RPM,TPS,Distância,Marcha,Temp._do_motor,Tensão_da_Bateria,Pressão_de_Óleo,Pressão_de_Combustível,Nível_de_combustível,Lenta,Velocidade_de_referência
0.020,3693,5.1,0.00,0,77.1,12.63,3.69,3.05,4.4,OFF,0.1
0.060,3739,5.2,0.00,0,77.1,12.64,3.67,3.03,4.4,OFF,0.1
```

## Colunas usadas pelo software

| Coluna | Usada em | Observacao |
|---|---|---|
| `TIME` | Vital Signal, Driver | Tempo da amostra, em segundos |
| `RPM` | Vital Signal, Driver | Rotacao do motor |
| `TPS` | Driver | Posicao do acelerador, em porcentagem |
| `Distância` | Vital Signal, Driver | Distancia percorrida, normalmente em metros |
| `Marcha` | Registro geral | Pode ser usada em futuras analises |
| `Temp._do_motor` | Vital Signal | Temperatura do motor em graus Celsius |
| `Tensão_da_Bateria` | Vital Signal | Tensao da bateria em volts |
| `Pressão_de_Óleo` | Vital Signal | Pressao de oleo em bar |
| `Pressão_de_Combustível` | Vital Signal | Pressao de combustivel em bar |
| `Nível_de_combustível` | Registro geral | Nivel de combustivel registrado pelo sistema |
| `Lenta` | Registro geral | Estado de lenta, normalmente `ON` ou `OFF` |
| `Velocidade_de_referência` | Vital Signal, Driver | Velocidade usada para graficos e calculo de aceleracao |

## Cuidados com acentos e separadores

1. Mantenha os nomes das colunas exatamente como exportados pelo logger.
2. Evite editar o cabecalho no Excel sem necessidade, porque acentos podem ser alterados.
3. Se o software nao encontrar uma coluna, confira se o arquivo usa `Distância` ou outro nome parecido, como `Distancia`.
4. As paginas principais usam leitura CSV padrao por virgula. Arquivos separados por ponto e virgula podem falhar nas paginas **Vital Signal** e **Driver**.
5. Os valores numericos devem usar ponto decimal, por exemplo `12.63`, nao `12,63`.

# Paginas funcionais

# Performance

## Finalidade

A pagina **Performance** e a entrada principal do software. Ela define o contexto do teste, seleciona os pilotos ativos, registra o planejamento do dia, recebe os logs e cria uma area para relatorio geral.

Use esta pagina antes de qualquer outra. Muitas paginas dependem dos pilotos selecionados e dos logs carregados aqui.

## Campos e funcoes

### Test goal

Campo de texto para escrever o objetivo do teste.

Exemplos:

| Situacao | Exemplo de preenchimento |
|---|---|
| Skidpad | `Validar setup de cambagem dianteira no skidpad` |
| Frenagem | `Comparar bias 60/40 e 65/35 em frenagem reta` |
| Endurance | `Avaliar temperatura de motor e consistencia de ritmo` |

Como usar:

1. Clique no campo **Test goal**.
2. Escreva o objetivo de forma curta e verificavel.
3. Evite objetivos vagos como `testar carro`.
4. Prefira frases que indiquem o que sera comparado ou validado.

Erros comuns:

- Escrever um objetivo muito generico.
- Mudar o objetivo no meio do teste sem registrar no relatorio.
- Nao ligar o objetivo aos dados que serao coletados.

Boas praticas:

- Comece com verbo de engenharia: `validar`, `comparar`, `medir`, `investigar`.
- Inclua o sistema avaliado: pneus, freio, motor, piloto, setup ou arrefecimento.

### Test location

Campo de texto para registrar o local do teste.

Exemplos:

- `Kartodromo RBC`
- `Patio da universidade`
- `Area de testes - aceleracao`

Como usar:

1. Digite o local real.
2. Se houver mais de uma configuracao de pista, inclua a configuracao.
3. Use o mesmo nome em todos os relatorios do mesmo local.

Erro comum:

- Preencher apenas `pista`, o que dificulta comparar testes futuros.

### Select the drivers

Seletor multiplo de pilotos. Atualmente os nomes disponiveis sao:

- `Jenifer`
- `Muniz`
- `Rafael`

Como usar:

1. Clique no seletor.
2. Marque os pilotos que participaram do teste.
3. Confira se os logs carregados comecam com o nome dos pilotos selecionados.

Exemplo:

Se voce selecionar `Jenifer` e `Rafael`, o software tentara exibir dados desses dois pilotos nas paginas de pneus, sinais vitais, driver e debriefing.

Erros comuns:

- Selecionar um piloto sem carregar o log correspondente.
- Carregar um log chamado `SkidPad_Jenifer.csv`; o software espera que o arquivo comece com `Jenifer`.
- Esquecer de remover um piloto que nao participou do teste.

### Select the date

Campo de data do teste.

Como usar:

1. Clique no calendario.
2. Escolha a data real do teste.
3. Use a data do dia em que os dados foram coletados, nao a data em que a analise foi feita.

### Start time e End time

Campos de horario inicial e final do teste.

Como usar:

1. Em **Start time**, coloque o horario de inicio da atividade.
2. Em **End time**, coloque o horario de encerramento.
3. Se o teste tiver varios stints, registre o periodo geral e detalhe os stints no planejamento ou relatorio.

Exemplo:

| Campo | Valor |
|---|---|
| Start time | `09:00` |
| End time | `12:30` |

### Test Planing

Tabela editavel para planejar as atividades do teste.

Colunas:

| Coluna | Finalidade | Exemplo |
|---|---|---|
| `Description` | Descricao da tarefa | `Frenagem reta de 60 km/h` |
| `Time` | Horario planejado | `10:30` |
| `Responsible` | Pessoa responsavel | `Freios - Pedro` |
| `Done` | Checkbox de conclusao | Marcado quando concluido |

Como usar:

1. Clique em uma celula da tabela.
2. Preencha a tarefa, horario e responsavel.
3. Use **Add row** ou a linha vazia para criar novas tarefas.
4. Marque **Done** quando a tarefa for executada.
5. Clique em **Confirm planing** para confirmar o planejamento na sessao.

Exemplo de planejamento:

| Description | Time | Responsible | Done |
|---|---:|---|---|
| Checar torque das rodas | 08:40 | Chassi | false |
| Aquecer motor | 09:00 | Powertrain | false |
| Skidpad Jenifer | 09:30 | Dados | false |
| Medir temperatura dos pneus | 09:40 | Vehicle Dynamics | false |

Erros comuns:

- Nao marcar tarefas concluidas.
- Usar nomes de responsaveis ambiguos, como `eu`.
- Nao registrar mudancas de plano durante o teste.

### General Reports

Area de texto para observacoes gerais do dia.

Como usar:

1. Escreva eventos importantes que nao pertencem a uma pagina especifica.
2. Registre problemas, condicoes externas, atrasos e decisoes.
3. Use frases objetivas.

Exemplos:

- `Primeiro stint interrompido por perda de pressao no pneu dianteiro esquerdo.`
- `Pista com baixa aderencia ate 10h por umidade.`
- `Setup alterado apos segunda bateria: bias dianteiro de 60% para 62%.`

### Select log

Area de upload de arquivos. Permite carregar multiplos logs.

Como usar:

1. Clique em **Browse files** ou arraste os arquivos para a area.
2. Selecione os CSVs dos pilotos.
3. Aguarde a mensagem de sucesso.
4. Confira em **Uploaded files** se todos os arquivos apareceram.

Regras importantes:

1. O arquivo deve ser texto legivel em UTF-8.
2. Para as paginas **Vital Signal** e **Driver**, o nome do arquivo deve comecar com o nome do piloto.
3. O CSV deve ter as colunas esperadas.

### Uploaded files

Lista dos arquivos carregados.

Funcoes:

- Abrir o expander do arquivo para visualizar o conteudo bruto.
- Conferir rapidamente se o cabecalho do CSV esta correto.
- Remover um arquivo usando o botao **Remover**.

Erros comuns:

- Carregar arquivo errado e nao conferir o cabecalho.
- Carregar o mesmo piloto duas vezes com nomes diferentes.
- Remover um arquivo e esquecer de fazer novo upload antes de ir para **Driver**.

# General Conditions

## Finalidade

A pagina **General Conditions** registra as condicoes basicas do teste: massa do carro, massa do piloto, combustivel e temperaturas externas. Esses dados ajudam a interpretar diferencas entre stints e pilotos.

A pagina usa os pilotos selecionados na **Performance**. Para cada piloto selecionado, ela cria um bloco de preenchimento.

## Aba Weight Information

### Car (Kg)

Massa do carro em quilogramas.

Como usar:

1. Escolha o piloto/bloco correto.
2. Digite a massa do carro na condicao do teste.
3. Use o mesmo criterio de medicao em todos os testes: com ou sem combustivel, com ou sem piloto, conforme definido pela equipe.

Exemplo:

```text
Car (Kg) - Rafael: 230.5
```

### Driver (Kg)

Massa do piloto em quilogramas.

Como usar:

1. Digite a massa do piloto equipado, se esse for o padrao da equipe.
2. Caso use massa sem equipamento, registre isso no **General Reports**.

Exemplo:

```text
Driver (Kg) - Jenifer: 62.0
```

### Fuel (L)

Quantidade de combustivel em litros.

Como usar:

1. Digite o volume estimado ou medido antes do stint.
2. Use sempre a mesma unidade: litros.
3. Atualize se o volume mudar entre stints importantes.

Exemplo:

```text
Fuel (L) - Muniz: 4.5
```

## Aba External Temperatures

### Track temperature

Temperatura da pista em graus Celsius.

Como usar:

1. Meça a pista com termometro infravermelho.
2. Aponte sempre para regioes semelhantes da pista.
3. Registre a temperatura proxima ao horario do stint.

### Air temperature

Temperatura do ar em graus Celsius.

Como usar:

1. Use dado de sensor local ou estacao meteorologica confiavel.
2. Evite registrar a temperatura de dentro do box se o teste ocorre ao ar livre.

## Exemplo real de preenchimento

| Piloto | Car (Kg) | Driver (Kg) | Fuel (L) | Track temp | Air temp |
|---|---:|---:|---:|---:|---:|
| Jenifer | 230.0 | 62.0 | 4.0 | 38.5 | 27.0 |
| Rafael | 230.0 | 74.0 | 3.5 | 41.0 | 28.0 |

## Erros comuns e como evitar

1. **Esquecer de selecionar piloto na Performance**: volte para **Performance** e selecione os pilotos antes de preencher.
2. **Misturar massa do carro com massa carro + piloto**: defina um padrao da equipe e mantenha.
3. **Registrar temperatura de pista muito depois do stint**: temperaturas mudam rapidamente; meca perto da saida ou chegada do carro.
4. **Usar graus Fahrenheit**: a pagina espera graus Celsius.

## Boas praticas

1. Meça combustivel e temperatura sempre antes do stint.
2. Registre mudancas no **General Reports**.
3. Use os mesmos instrumentos sempre que possivel.
4. Revise os valores antes de trocar de pagina.

# Setup

## Finalidade

A pagina **Setup Settings** registra o acerto mecanico usado por cada piloto. Ela e importante para relacionar comportamento do carro, temperatura de pneus, feedback do piloto e dados de log.

A pagina tem tres abas:

- **Brake**
- **Suspension**
- **Compression**

Cada aba mostra campos para cada piloto selecionado na **Performance**.

## Aba Brake

### Brake Bias Front (%)

Percentual de bias de freio no eixo dianteiro.

Como usar:

1. Digite o percentual de freio dianteiro.
2. Use valores entre `0` e `100`.
3. Confira se o valor corresponde ao ajuste real do balance bar ou regulagem usada.

Exemplo:

```text
Brake Bias Front (%) - Rafael: 60.0
```

### Brake Bias Rear (%)

Percentual de bias traseiro. Este campo e calculado automaticamente como:

```text
100 - Brake Bias Front
```

Ele fica desabilitado para evitar inconsistencias.

Exemplo:

Se **Brake Bias Front** for `60.0`, o traseiro sera `40.0`.

Erros comuns:

- Tentar digitar manualmente no campo traseiro.
- Registrar bias estimado sem conferir o ajuste fisico.
- Usar valores que nao somam 100% fora do software.

## Aba Suspension

### Toe (%)

Campo para registrar o toe do carro.

Como usar:

1. Digite o valor medido ou definido no setup.
2. Use sinal positivo/negativo conforme o padrao da equipe.
3. Mantenha o mesmo padrao em todos os testes.

Exemplo:

```text
Toe (%) - Jenifer: 0.2
```

### Camber Front (%)

Cambagem dianteira. A pagina permite valores de `-10.0` a `0.0`.

Como usar:

1. Digite a cambagem dianteira do setup.
2. Use valores negativos para cambagem negativa.
3. Compare depois com a analise de pneus.

Exemplo:

```text
Camber Front (%) - Muniz: -1.5
```

### Camber Rear (%)

Cambagem traseira. A pagina permite valores de `-10.0` a `0.0`.

Exemplo:

```text
Camber Rear (%) - Muniz: -2.0
```

### Rebound (Clicks)

Numero de cliques de retorno do amortecedor.

Como usar:

1. Use a referencia padrao da equipe: por exemplo, totalmente fechado para aberto, ou o contrario.
2. Digite o numero de cliques.
3. Nao misture referencias entre testes.

Exemplo:

```text
Rebound (Clicks) - Rafael: 10
```

### Preload Rear (mm)

Pre-carga da mola traseira, em milimetros.

Exemplo:

```text
Preload Rear (mm) - Rafael: 10.0
```

### Preload Front (mm)

Pre-carga da mola dianteira, em milimetros.

Exemplo:

```text
Preload Front (mm) - Rafael: 8.5
```

## Aba Compression

### DHX RC4 Air Assist (Psi)

Pressao de assistencia do amortecedor DHX RC4, em psi.

Exemplo:

```text
DHX RC4 Air Assist (Psi) - Jenifer: 100
```

### Low Speed Compression (Clicks)

Compressao de baixa velocidade em cliques.

Use para registrar ajuste que afeta movimentos mais lentos de chassi, como transferencia de carga.

### High Speed Compression (Clicks)

Compressao de alta velocidade em cliques.

Use para registrar ajuste que afeta impactos, zebras e irregularidades.

## Exemplo real de uso

1. Antes do teste, registre o setup inicial.
2. Rode o stint.
3. Preencha pneus em **Tires** e feedback em **Drive Debriefings**.
4. Se mudar cambagem, bias ou amortecedor, registre a nova configuracao antes do proximo stint.

## Erros comuns e como evitar

1. **Nao registrar a referencia dos cliques**: sempre indique no relatorio se a contagem parte de fechado ou aberto.
2. **Mudar setup sem atualizar a pagina**: cria analises erradas depois.
3. **Confundir dianteiro e traseiro**: revise antes de comparar com pneus.
4. **Usar porcentagem para camber sem padrao claro**: se a equipe mede em graus, mantenha a conversao ou padronize o campo.

## Boas praticas

1. Fotografe a folha de setup fisica e confira contra o software.
2. Altere apenas uma variavel importante por vez quando possivel.
3. Relacione mudancas de setup com comentarios do piloto.
4. Confira o bias antes de qualquer teste de frenagem.

# Tires

## Finalidade

A pagina **Tires Performance** registra temperaturas e pressoes dos pneus antes e depois do teste. Ela tambem gera graficos e KPIs para apoiar decisoes sobre pressao, cambagem, janela de temperatura e inflacao.

## Configuracoes internas usadas pela pagina

| Parametro | Valor atual |
|---|---:|
| Temperatura alvo do pneu | `85 °C` |
| Pressao alvo | `28 psi` |
| Tolerancia da pressao ideal | aproximadamente `±1 psi` |
| Superficies medidas | `Outside`, `Middle`, `Inside` |

## Aba Manual Input

Para cada piloto selecionado, a pagina cria dois momentos:

- **Before Test**: dados antes do stint.
- **After Test**: dados depois do stint.

Para cada momento, aparecem os quatro pneus:

- `Rear left`
- `Front left`
- `Rear right`
- `Front right`

Para cada pneu, devem ser preenchidas:

1. Temperatura na parte externa: `Outside`.
2. Temperatura no meio: `Middle`.
3. Temperatura na parte interna: `Inside`.
4. Pressao em `psi`.

### Como preencher temperaturas

1. Pare o carro depois do stint.
2. Meça os pneus rapidamente, sempre na mesma ordem.
3. Para cada pneu, registre `Outside`, `Middle` e `Inside`.
4. Use graus Celsius.
5. Evite medir depois de muito tempo parado, porque o pneu esfria e distorce a analise.

Exemplo:

| Pneu | Outside | Middle | Inside | Pressao |
|---|---:|---:|---:|---:|
| Front left | 78.0 | 83.0 | 88.0 | 28.5 |
| Front right | 80.0 | 85.0 | 90.0 | 28.7 |
| Rear left | 75.0 | 80.0 | 84.0 | 27.8 |
| Rear right | 76.0 | 81.0 | 85.0 | 27.9 |

### Como preencher pressoes

1. Use calibrador confiavel.
2. Registre pressao fria antes do teste em **Before Test**.
3. Registre pressao quente logo apos o stint em **After Test**.
4. Use sempre `psi`.

## Aba Temperature Graphs

Mostra graficos de temperatura por superficie usando os dados de **After Test**.

Graficos exibidos:

- Rear Left
- Rear Right
- Front Left
- Front Right

Como usar:

1. Preencha **Manual Input**.
2. Va para **Temperature Graphs**.
3. Compare as curvas dos pilotos.
4. Observe se a temperatura cresce de fora para dentro ou se o meio esta muito quente/frio.

Situacoes de uso real:

- Se o pneu esta muito quente no meio, pode indicar pressao alta.
- Se a parte interna esta muito mais quente, pode indicar cambagem excessiva.
- Se a parte externa esta muito mais quente, pode indicar pouca cambagem ou excesso de rolagem.

## Aba KPIs

### Pressure analysis

Mostra a pressao final de cada pneu e classifica:

| Status | Significado |
|---|---|
| Ideal | Pressao proxima de `28 psi` |
| Alta | Pressao acima da referencia |
| Baixa | Pressao abaixo da referencia |

Como usar:

1. Veja quais pneus ficaram fora da referencia.
2. Compare com temperatura do meio do pneu.
3. Ajuste a pressao inicial no proximo stint se necessario.

### Camber analysis

Calcula a diferenca entre temperatura interna e externa:

```text
Inside - Outside
```

Depois compara com a cambagem registrada na pagina **Setup**.

Como usar:

1. Preencha o setup de cambagem em **Setup**.
2. Preencha temperaturas em **Tires**.
3. Veja se a pagina indica cambagem adequada, pouca ou excessiva.

Observacao: o criterio atual e simples e deve ser usado como indicacao inicial, nao como decisao isolada.

### Temperature Window Analysis

Compara a temperatura media de cada pneu com a janela alvo de temperatura.

Status:

| Status | Interpretacao |
|---|---|
| Cold | Pneu abaixo da janela |
| Ok | Pneu dentro da janela |
| Hot | Pneu acima da janela |

Como usar:

1. Verifique se todos os pneus estao chegando perto da janela.
2. Compare esquerda/direita.
3. Relacione com pista, piloto e tipo de prova.

### Tire Inflation Analysis

Analisa o perfil de temperatura para sugerir tendencia de inflacao.

Interpretacao geral:

| Resultado | Possivel leitura |
|---|---|
| Over | Tendencia de pressao alta |
| Under | Tendencia de pressao baixa |
| Ok | Perfil mais equilibrado |

## Erros comuns e como evitar

1. **Medir pneus tarde demais**: meça imediatamente apos o carro parar.
2. **Trocar Outside e Inside**: defina sempre o lado de referencia antes da coleta.
3. **Usar psi em um stint e bar em outro**: a pagina espera psi.
4. **Nao preencher Before Test**: perde-se comparacao frio/quente.
5. **Esquecer de preencher Setup antes dos KPIs**: a analise de cambagem depende dos valores de setup.

## Boas praticas

1. Uma pessoa mede e outra digita para ganhar tempo.
2. Use sempre a mesma ordem: dianteiro esquerdo, dianteiro direito, traseiro esquerdo, traseiro direito.
3. Registre condicao da pista na pagina **General Conditions**.
4. Compare pneus com feedback do piloto em **Drive Debriefings**.

# Vital Signal

## Finalidade

A pagina **Vital Signal Analysis** avalia sinais de saude do carro a partir dos logs carregados. Ela ajuda a identificar problemas de temperatura, pressao de oleo, pressao de combustivel, tensao de bateria e distribuicao de RPM.

Antes de abrir esta pagina:

1. Va para **Performance**.
2. Selecione os pilotos.
3. Carregue os logs com nomes que comecem pelos nomes dos pilotos.

Se nao houver log carregado ou piloto selecionado, a pagina exibira aviso e interrompera a analise.

## Como a pagina encontra o log

Para cada piloto selecionado, o software procura um arquivo cujo nome comece com o nome do piloto.

Exemplo:

```text
Rafael_Frenagem_15_03.csv
```

funciona para o piloto `Rafael`.

```text
Frenagem_Rafael_15_03.csv
```

pode nao funcionar.

## Aba KPI

Mostra valores maximos, minimos e medios de sinais vitais.

Sinais avaliados:

| Sinal no software | Coluna do CSV | Unidade | Faixa verde atual |
|---|---|---:|---:|
| Engine temperature | `Temp._do_motor` | °C | `70` a `100` |
| Engine oil pressure | `Pressão_de_Óleo` | bar | `1` a `10` |
| Fuel pressure | `Pressão_de_Combustível` | bar | `2` a `3.5` |
| Battery voltage | `Tensão_da_Bateria` | V | `11.5` a `14` |

Indicadores coloridos:

| Cor | Significado geral |
|---|---|
| Verde | Valor dentro da faixa esperada |
| Vermelho | Valor acima do limite alto |
| Azul | Valor abaixo da faixa esperada |

Como usar:

1. Abra a aba **KPI**.
2. Confira cada piloto.
3. Observe os valores **Max**, **Min** e **Avg**.
4. Priorize investigacoes quando houver vermelho ou azul em sinais criticos.

Exemplo de situacao:

- Se a pressao de oleo minima ficar abaixo de `1 bar`, verifique se ocorreu em baixa rotacao, curva longa, frenagem forte ou falha de sensor.

## Aba X/Y Analysis

Mostra graficos empilhados por distancia.

Sinais exibidos:

- RPM
- Temperatura do motor
- Tensao da bateria
- Pressao de oleo
- Pressao de combustivel

Tambem sao desenhadas linhas de referencia para alguns limites.

Como usar:

1. Abra **X/Y Analysis**.
2. Passe o mouse no grafico para comparar sinais no mesmo ponto da distancia.
3. Procure quedas bruscas, picos ou comportamento repetitivo.
4. Use a area **Engineer's Notes** para registrar conclusoes.

Campo **Engineer's Notes**:

Use para escrever observacoes tecnicas, como:

- `Queda de pressao de oleo entre 120 m e 150 m durante frenagem.`
- `Bateria permaneceu estavel durante todo o stint.`
- `Temperatura do motor estabilizou em 92 °C.`

## Aba Oil Pressure

Analisa pressao de oleo com uma curva minima interpolada por RPM.

Graficos disponiveis no seletor **Select chart for driver**:

| Opcao | O que mostra | Quando usar |
|---|---|---|
| Pressure vs Distance | Pressao de oleo e pressao minima ao longo da distancia | Para localizar onde a pressao cai |
| Oil Pressure vs RPM with Trend | Relacao entre RPM e pressao de oleo com tendencia | Para avaliar comportamento geral do sistema |
| Critical Points: Pressure vs Accelerations | Pontos criticos cruzados com aceleracoes | Para investigar perda de pressao em frenagem/curva |

Como usar:

1. Escolha o piloto.
2. Selecione um grafico.
3. Procure pontos onde a pressao real fica abaixo da pressao minima.
4. Registre a interpretacao em **Engineer's Notes**.

Cuidados:

- A pagina calcula aceleracao a partir da velocidade de referencia.
- Logs com velocidade ruidosa podem gerar aceleracoes irreais.
- Confira se a coluna `Velocidade_de_referência` esta coerente.

## Aba RPM Trend

Mostra um histograma de RPM para cada piloto.

Como usar:

1. Abra a aba **RPM Trend**.
2. Veja em quais faixas de RPM o motor passou mais tempo.
3. Compare pilotos ou mapas de pista.
4. Use para avaliar uso de marcha, faixa de torque e comportamento de conducao.

## Erros comuns e como evitar

1. **Nenhum log carregado**: volte para **Performance** e faca upload.
2. **Log nao encontrado para piloto**: renomeie o arquivo para comecar com o nome do piloto.
3. **Coluna ausente**: confira cabecalho do CSV.
4. **Separador errado**: use virgula como separador.
5. **Valores nao numericos em colunas de sensores**: mantenha numeros limpos; textos como `erro` podem virar zero.

## Boas praticas

1. Sempre confira sinais vitais antes de analisar performance do piloto.
2. Trate falhas de pressao de oleo como prioridade.
3. Compare o grafico com eventos de pista: frenagem, curva, reta e troca de marcha.
4. Registre conclusoes no campo de notas enquanto a analise esta fresca.

# Driver

## Finalidade

A pagina **Driver Data Analysis** analisa comportamento de pilotagem usando logs. Ela compara velocidade, RPM, TPS, aceleracoes e regioes de grip.

Antes de usar:

1. Selecione pilotos na pagina **Performance**.
2. Carregue logs com nomes iniciando pelo nome do piloto.
3. Confirme que os logs possuem `Distância`, `RPM`, `TPS` e `Velocidade_de_referência`.

## Aba Driving Influences

Mostra graficos por distancia com:

- RPM
- Velocidade
- TPS

Tambem possui campo **Engineer's Notes**.

Como usar:

1. Abra a aba **Driving Influences**.
2. Compare os pilotos na mesma distancia.
3. Procure diferencas de velocidade, uso de acelerador e rotacao.
4. Escreva conclusoes no campo de notas.

Exemplo de leitura:

- Se um piloto abre TPS antes da saida da curva mas a velocidade nao cresce, pode haver falta de tracao.
- Se um piloto reduz velocidade antes do outro, pode estar freando cedo.

## Aba Throttle

Analisa o uso do acelerador.

Graficos exibidos:

| Sinal | Descricao |
|---|---|
| Speed | Velocidade de referencia |
| TPS | Posicao do acelerador |
| Full TPS | Tempo acumulado em acelerador alto |
| Speed TPS | Derivada do TPS, indicando velocidade de abertura/fechamento |

Como usar:

1. Abra **Throttle**.
2. Veja onde o piloto mantem TPS alto.
3. Compare se a abertura do acelerador e progressiva ou brusca.
4. Relacione com perda de tracao, subesterco ou sobresterco relatado pelo piloto.

Erros comuns:

- Interpretar TPS alto como sempre positivo. Em curvas, TPS alto cedo demais pode causar perda de tracao.
- Comparar pilotos sem garantir que os logs sao da mesma pista ou mesmo trecho.

## Aba Analysis acceleration

Mostra o plano de aceleracao longitudinal versus aceleracao lateral. E uma ferramenta para visualizar uso de aderencia.

### Checkboxes de fatores de grip

| Checkbox | O que destaca |
|---|---|
| Aero Grip | Pontos de alta aceleracao lateral em maior velocidade |
| Straightline Braking Grip | Frenagens fortes em linha reta |
| Traction Grip | Tracao em saida de curva |
| Trail Braking Grip | Frenagem com aceleracao lateral relevante |
| Cornering Grip | Curvas com pouca aceleracao longitudinal |

Como usar:

1. Marque ou desmarque os checkboxes para isolar regioes.
2. Observe o espalhamento dos pontos.
3. Compare pilotos.
4. Use as regioes destacadas para discutir onde ha ganho de tempo.

Exemplos:

- Muitos pontos em **Straightline Braking Grip** indicam frenagens fortes em linha reta.
- Pontos em **Trail Braking Grip** mostram uso combinado de freio e curva.
- Pontos de **Traction Grip** ajudam a avaliar saida de curva.

Campo **Engineer's Notes**:

Use para registrar:

- `Rafael alcanca maior G longitudinal em frenagem reta.`
- `Jenifer mantem curva mais constante, com menor variacao de TPS.`
- `Possivel perda de tracao nas saidas lentas.`

## Aba Trends

Mostra histogramas:

- Histograma de velocidade.
- Histograma de TPS.

Como usar:

1. Veja em quais velocidades o piloto passou mais tempo.
2. Veja se o TPS ficou muito tempo em baixa, media ou alta abertura.
3. Compare entre pilotos ou stints.

Situacoes de uso:

- Em endurance, histograma pode mostrar consistencia de ritmo.
- Em aceleracao, pode indicar se o piloto manteve o acelerador aberto.
- Em skidpad, pode mostrar faixa de velocidade predominante.

## Erros comuns e como evitar

1. **Log com nome errado**: o arquivo deve comecar com o nome do piloto.
2. **Dados de pistas diferentes**: nao compare pilotos se os trechos nao sao equivalentes.
3. **Velocidade ruidosa**: pode distorcer aceleracoes calculadas.
4. **TPS com escala diferente**: confirme se o TPS esta de `0` a `100`.
5. **Amostragem diferente da esperada**: algumas analises assumem frequencias fixas; logs muito diferentes podem alterar resultados.

## Boas praticas

1. Compare pilotos no mesmo tipo de teste e com mesmo setup.
2. Use notas para conectar grafico e sensacao do piloto.
3. Analise sinais vitais antes de concluir que diferenca e apenas pilotagem.
4. Combine **Driver** com **Drive Debriefings** para separar problema de setup, confianca e tecnica.

# Drive Debriefings

## Finalidade

A pagina **Driver Feedback** registra a percepcao dos pilotos e transforma avaliacoes subjetivas em dados comparaveis. Ela tambem permite registrar tempos de volta e gerar um grafico de ritmo.

Use esta pagina logo apos o stint, enquanto o piloto ainda lembra do comportamento do carro.

## Estrutura da pagina

Se houver pilotos selecionados, a pagina cria:

1. Uma aba para cada piloto.
2. Uma aba final chamada **Race Pace**.

Se nenhum piloto estiver selecionado, a pagina avisa para selecionar pilotos na interface principal.

## Aba de cada piloto

### Lap Info

Tabela editavel com:

| Coluna | Descricao | Exemplo |
|---|---|---|
| `Lap` | Identificacao da volta | `1`, `2`, `Run A` |
| `Lap Time (s)` | Tempo da volta em segundos | `62.431` |

Como usar:

1. Digite a identificacao da volta.
2. Digite o tempo em segundos.
3. Adicione novas linhas conforme necessario.
4. Evite misturar formato `mm:ss` com segundos.

Exemplo:

| Lap | Lap Time (s) |
|---|---:|
| 1 | 64.20 |
| 2 | 62.85 |
| 3 | 62.10 |

### Performance Rating

Conjunto de sliders de `0` a `6`.

Escala:

| Valor | Significado |
|---:|---|
| 0 | Very Poor |
| 1 | Poor |
| 2 | Below Average |
| 3 | Average |
| 4 | Good |
| 5 | Very Good |
| 6 | Excellent |

Criterios avaliados:

| Criterio | O que avaliar |
|---|---|
| Throttle response | Resposta ao acelerador e controle de tracao |
| Steering | Sensacao de direcao, precisao e esforco |
| Braking | Confianca, estabilidade e capacidade de freio |
| Gear shifting | Qualidade das trocas de marcha |
| Seat + pedal adjustment comfort | Ergonomia, banco e pedais |

Como usar:

1. Entrevistem o piloto logo apos o stint.
2. Para cada criterio, escolha uma nota de `0` a `6`.
3. Evite discutir demais antes de registrar a primeira impressao.
4. Depois compare com os dados objetivos.

### Radar Chart

Grafico radar gerado automaticamente a partir dos sliders.

Como usar:

1. Ajuste os sliders.
2. Observe o formato do radar.
3. Procure pontos fracos: por exemplo, boa direcao mas freio ruim.
4. Compare com comentarios e logs.

### General Comments

Area de texto livre para comentario do piloto.

Boas perguntas para guiar o comentario:

1. O carro estava previsivel?
2. A frente saiu ou a traseira escapou?
3. O freio estava consistente?
4. A resposta do acelerador estava progressiva?
5. Algum ruido, vibracao ou cheiro anormal apareceu?
6. O piloto teve dificuldade ergonomica?

Exemplo de comentario:

```text
Carro estavel em frenagem reta, mas dianteira escorrega no meio da curva. Acelerador bom na saida, sem cortes. Pedal de freio ficou mais longo no fim do terceiro stint.
```

## Aba Race Pace

Mostra comparacao de tempo de volta entre pilotos usando os dados preenchidos em **Lap Info**.

Como usar:

1. Preencha as voltas dos pilotos.
2. Abra **Race Pace**.
3. Compare curvas de tempo.
4. Procure consistencia, evolucao ou queda de performance.

Exemplos de uso:

- Comparar quem melhorou ao longo das voltas.
- Ver se um piloto perdeu ritmo por temperatura de pneus.
- Relacionar queda de tempo com problema mecanico ou fadiga.

## Erros comuns e como evitar

1. **Tempo em formato errado**: use segundos, como `62.43`, nao `1:02.43`.
2. **Feedback muito generico**: evite `carro bom`; registre onde e por que.
3. **Preencher muito tarde**: feedback perde qualidade depois de muito tempo.
4. **Comparar voltas de pistas diferentes**: Race Pace so faz sentido com o mesmo tracado.

## Boas praticas

1. Uma pessoa entrevista e outra digita.
2. Registre primeiro a percepcao do piloto, depois discuta dados.
3. Use a mesma escala de notas ao longo da temporada.
4. Compare feedback com pneus, setup e sinais vitais.

# Paginas planejadas ou em desenvolvimento

As paginas abaixo aparecem no repositorio ou no menu, mas nao fazem parte do fluxo oficial de uso documentado neste manual. Algumas podem ter campos iniciais ou prototipos, porem ainda nao devem ser usadas para decisoes oficiais sem revisao da equipe responsavel.

## Project Validation

Status: planejada/em desenvolvimento.

Objetivo esperado: registrar responsavel pelo projeto, descricao da validacao, resultados esperados e comparacao entre projeto e teste real.

Uso recomendado por enquanto: nao usar como fonte oficial ate que criterios, exportacao e padrao de validacao estejam definidos.

## Chassi

Status: planejada/em desenvolvimento.

Objetivo esperado: registrar dados teoricos de chassi, material, modulo elastico, pontos criticos, carga aplicada e possivelmente teste de rigidez torcional.

Uso recomendado por enquanto: tratar como prototipo.

## Brake

Status: planejada/em desenvolvimento.

Objetivo esperado: consolidar validacao teorica e experimental do sistema de freios, incluindo bias, capacidade de frenagem, temperatura e logs de frenagem.

Uso recomendado por enquanto: nao considerar como fluxo oficial do README ate revisao e aprovacao pela equipe de freios.

## Powertrain

Status: planejada/em desenvolvimento.

Objetivo esperado: analises especificas de motor, consumo, torque, potencia, arrefecimento e estrategia de powertrain.

Uso recomendado por enquanto: pagina sem fluxo oficial.

## Electronics PDM

Status: planejada/em desenvolvimento.

Objetivo esperado: monitoramento de eletronica, PDM, alimentacao, cargas eletricas e diagnosticos.

Uso recomendado por enquanto: pagina sem fluxo oficial.

## Aero

Status: planejada/em desenvolvimento.

Objetivo esperado: registrar dados de simulacao aerodinamica, velocidade de simulacao, area frontal, arrasto, coeficiente `Cd`, densidade do ar e massa do veiculo.

Uso recomendado por enquanto: tratar como prototipo de cadastro, nao como ferramenta completa de analise.

## Drivetrain

Status: planejada/em desenvolvimento.

Objetivo esperado: analises de transmissao, relacao, corrente, diferencial, perdas e comportamento em pista.

Uso recomendado por enquanto: pagina sem fluxo oficial.

## Steering

Status: planejada/em desenvolvimento.

Objetivo esperado: registrar dados teoricos de direcao e possivelmente analise de angulo de volante.

Uso recomendado por enquanto: tratar como prototipo.

# Boas praticas gerais

## Antes do teste

1. Confirme que o app abre corretamente.
2. Confirme que os nomes dos pilotos estao corretos.
3. Teste o upload de um CSV conhecido.
4. Combine o padrao de nomes dos arquivos.
5. Defina quem sera responsavel por preencher cada pagina.

## Durante o teste

1. Preencha dados de condicao assim que forem medidos.
2. Carregue logs logo apos cada stint.
3. Registre alteracoes de setup imediatamente.
4. Colete feedback do piloto antes de mostrar graficos.
5. Anote eventos fora do normal no **General Reports**.

## Depois do teste

1. Confira se todos os logs foram salvos fora do Streamlit.
2. Revise paginas **Vital Signal** e **Driver**.
3. Compare feedback subjetivo com dados objetivos.
4. Extraia conclusoes e acoes para o proximo teste.
5. Atualize a base de conhecimento da equipe.

## Checklist rapido de problemas

| Problema | Causa provavel | Solucao |
|---|---|---|
| Pagina Vital Signal mostra que nao ha log | Upload nao foi feito ou sessao reiniciou | Voltar em Performance e carregar CSV |
| Log nao encontrado para piloto | Nome do arquivo nao comeca com o nome do piloto | Renomear arquivo para `Piloto_Descricao.csv` |
| Grafico nao aparece | Coluna obrigatoria ausente | Conferir cabecalho do CSV |
| Valores zerados | Dados nao numericos foram convertidos para zero | Limpar CSV antes do upload |
| Comparacao de pilotos parece incoerente | Logs de pistas/stints diferentes | Comparar apenas dados equivalentes |
| Race Pace nao plota | Tempos vazios ou nao numericos | Usar tempos em segundos |
| KPIs de pneus parecem errados | Inside/Middle/Outside invertidos | Padronizar ordem de medicao |

## Padrao recomendado para nomear arquivos

Use:

```text
Piloto_TipoDeTeste_Data_Stint.csv
```

Exemplos:

```text
Jenifer_SkidPad_2026-05-31_Stint1.csv
Muniz_Endurance_2026-05-31_Stint2.csv
Rafael_Frenagem_2026-05-31_60kmh.csv
```

Evite:

```text
teste1.csv
log_final.csv
skidpad.csv
IR04_Rafael.csv
```

## Principio de uso

O software nao substitui julgamento de engenharia. Ele organiza dados, facilita comparacoes e ajuda a encontrar sinais importantes. Decisoes de setup, seguranca e validacao devem sempre combinar:

1. Dados objetivos do log.
2. Condicoes registradas de pista.
3. Setup usado.
4. Feedback do piloto.
5. Inspecao fisica do carro.
