# 🎬 Automação de Criação de Shorts para YouTube

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Demonstração](#demonstração)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Fluxo de Trabalho](#fluxo-de-trabalho)
- [Funções Principais](#funções-principais)
- [Troubleshooting](#troubleshooting)
- [Contribuindo](#contribuindo)
- [Roadmap](#roadmap)
- [Licença](#licença)
- [Contato](#contato)

## 🎯 Sobre o Projeto

Este projeto é um **sistema automatizado completo** para criação, edição e publicação de vídeos shorts no YouTube. Ele integra diversas tecnologias de automação web, processamento de vídeo, geração de narração por IA e upload automático, permitindo a criação em massa de conteúdo vertical para redes sociais.

### 🌟 Principais Características

- ✨ **Automação End-to-End**: Desde a geração de script até o upload no YouTube
- 🤖 **Integração com ChatGPT**: Geração automática de roteiros envolventes
- 🎥 **Processamento de Vídeo**: Conversão automática para formato 9:16 (1080x1920)
- 🎙️ **Narração Automática**: Síntese de voz com Google Text-to-Speech
- 📝 **Legendas Animadas**: Geração automática de legendas palavra por palavra
- 🔄 **Sistema de Auto-Reset**: Recuperação automática de falhas do Selenium
- 🎨 **Download de Mídia**: Busca automática de vídeos no Freepik
- 📤 **Upload Automático**: Publicação direta no YouTube

## 🚀 Funcionalidades

### 1. Geração de Conteúdo com IA
- Integração com ChatGPT para criação de roteiros
- Prompts otimizados para conteúdo de 1 minuto
- Suporte a múltiplos temas simultaneamente
- Estilo de narração inspirado em shorts virais

### 2. Processamento de Vídeo
- **Redimensionamento Inteligente**: Conversão automática para formato vertical (9:16)
- **Crop Centralizado**: Foco no centro da imagem para melhor enquadramento
- **Concatenação de Clipes**: Combinação de múltiplos vídeos em um único short
- **Sincronização de Áudio**: Adição automática de narração aos vídeos
- **Efeitos Visuais**: Suporte para fade in/out

### 3. Geração de Legendas
- Legendas animadas palavra por palavra
- Sincronização precisa com áudio
- Estilo personalizado (cor amarela com borda preta)
- Posicionamento otimizado para shorts

### 4. Automação Web Robusta
- **Sistema de Auto-Reset**: Recuperação automática de falhas do navegador
- **Tratamento de Exceções**: Gerenciamento completo de erros do Selenium
- **Múltiplas Tentativas**: Sistema de retry automático (até 5 tentativas)
- **Gestão de Popups**: Fechamento automático de elementos obstrutivos

### 5. Download Automatizado
- Busca no Freepik por vídeos relacionados aos temas
- Filtro de conteúdo gratuito
- Download de múltiplos vídeos por tema
- Organização automática em diretórios

### 6. Upload no YouTube
- Login automático com conta Google
- Navegação até área de shorts
- Upload múltiplo de arquivos
- Configuração automática de metadados

## 🎥 Demonstração

### Processo Completo (Workflow)

```
┌─────────────────────────────────────────────────────────────┐
│  1. COLETA DE INFORMAÇÕES                                   │
│     • E-mail e senha Google                                 │
│     • Temas de interesse (até 6)                           │
│     • Configuração de diretórios                           │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  2. GERAÇÃO DE ROTEIROS (ChatGPT)                          │
│     • Login automático no ChatGPT                          │
│     • Envio de prompts customizados                        │
│     • Coleta de respostas da IA                            │
│     • Salvamento em JSON                                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  3. GERAÇÃO DE NARRAÇÃO (gTTS)                             │
│     • Conversão de texto para áudio                        │
│     • Geração de arquivos MP3                              │
│     • Organização por tema                                 │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  4. DOWNLOAD DE VÍDEOS (Freepik)                           │
│     • Login automático no Freepik                          │
│     • Busca por tema                                       │
│     • Filtro de vídeos gratuitos                           │
│     • Download de 5 vídeos por tema                        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  5. PROCESSAMENTO DE VÍDEO (MoviePy)                       │
│     • Redimensionamento para 1080x1920                     │
│     • Crop centralizado                                    │
│     • Cálculo de duração (60s ÷ nº de vídeos)             │
│     • Concatenação de clipes                               │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  6. ADIÇÃO DE ÁUDIO                                        │
│     • Sincronização vídeo + narração                       │
│     • Exportação de shorts com áudio                       │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  7. GERAÇÃO DE LEGENDAS                                    │
│     • Divisão do texto em palavras                         │
│     • Cálculo de tempo por palavra                         │
│     • Criação de TextClips animados                        │
│     • Composição final do vídeo                            │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  8. UPLOAD NO YOUTUBE                                      │
│     • Login automático                                     │
│     • Navegação até área de shorts                         │
│     • Upload múltiplo de vídeos                            │
│     • Finalização do processo                              │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Tecnologias Utilizadas

### Linguagem Principal
- **Python 3.8+** - Linguagem de programação

### Automação Web
- **Selenium WebDriver** - Automação de navegador
- **Undetected ChromeDriver** - Versão modificada do ChromeDriver para evitar detecção
- **PyAutoGUI** - Automação de interface gráfica
- **Pyperclip** - Manipulação de área de transferência

### Processamento de Vídeo
- **MoviePy** - Edição e processamento de vídeo
  - VideoFileClip - Manipulação de arquivos de vídeo
  - AudioFileClip - Manipulação de arquivos de áudio
  - TextClip - Geração de texto em vídeo
  - CompositeVideoClip - Composição de múltiplas camadas
  - concatenate_videoclips - Concatenação de clipes
  - FadeIn/FadeOut - Efeitos de transição

### Geração de Áudio
- **gTTS (Google Text-to-Speech)** - Síntese de voz

### Interface e Utilidades
- **Colorama** - Colorização de terminal
- **PSUtil** - Informações do sistema
- **Requests** - Requisições HTTP

### Gerenciamento de Dados
- **JSON** - Armazenamento de dados estruturados
- **Re (Regex)** - Validação de entrada

## 🏗️ Arquitetura do Sistema

```
┌────────────────────────────────────────────────────────────────┐
│                     CAMADA DE INTERFACE                        │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Terminal Interface (Colorama)                           │ │
│  │  • Coleta de dados do usuário                           │ │
│  │  • Validação de inputs                                  │ │
│  │  • Feedback visual do progresso                         │ │
│  └──────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────┐
│                  CAMADA DE AUTOMAÇÃO WEB                       │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Selenium Controller                                     │ │
│  │  • Sistema de Auto-Reset                                │ │
│  │  • Gerenciamento de sessões Chrome                      │ │
│  │  • Tratamento de exceções                               │ │
│  └──────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Integration Modules                                     │ │
│  │  • ChatGPT (geração de roteiros)                        │ │
│  │  • Freepik (download de vídeos)                         │ │
│  │  • YouTube (upload de shorts)                           │ │
│  └──────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────┐
│               CAMADA DE PROCESSAMENTO                          │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Video Processing Engine (MoviePy)                       │ │
│  │  • Redimensionamento e crop                             │ │
│  │  • Concatenação de clipes                               │ │
│  │  • Sincronização de áudio                               │ │
│  │  • Geração de legendas                                  │ │
│  └──────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Audio Generator (gTTS)                                  │ │
│  │  • Conversão texto para fala                            │ │
│  │  • Geração de arquivos MP3                              │ │
│  └──────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────┐
│                 CAMADA DE ARMAZENAMENTO                        │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  File System Manager                                     │ │
│  │  • Gerenciamento de diretórios                          │ │
│  │  • Organização de arquivos                              │ │
│  │  • Limpeza automática                                   │ │
│  └──────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Data Storage                                            │ │
│  │  • JSON (roteiros e metadados)                          │ │
│  │  • MP3 (narrações)                                      │ │
│  │  • MP4 (vídeos processados)                             │ │
│  └──────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
```

## 📦 Pré-requisitos

### Sistema Operacional
- Windows 10/11 (devido ao uso de comandos específicos do Windows)

### Software
- Python 3.8 ou superior
- Google Chrome (versão mais recente)
- ChromeDriver (instalado automaticamente pelo undetected-chromedriver)

### Contas Necessárias
- Conta Google (Gmail)
- Conta ChatGPT (acesso gratuito ou pago)
- Conta Freepik (gratuita)
- Canal no YouTube

### Requisitos de Hardware
- **RAM**: Mínimo 8GB (recomendado 16GB para processamento de vídeo)
- **Armazenamento**: 5GB de espaço livre por sessão
- **Processador**: Multi-core recomendado para processamento de vídeo

## 💾 Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/automacao-shorts-youtube.git
cd automacao-shorts-youtube
```

### 2. Crie um Ambiente Virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Arquivo requirements.txt

Crie um arquivo `requirements.txt` com o seguinte conteúdo:

```txt
selenium==4.15.2
undetected-chromedriver==3.5.4
colorama==0.4.6
psutil==5.9.6
gtts==2.5.0
requests==2.31.0
urllib3==2.1.0
moviepy==1.0.3
pyautogui==0.9.54
pyperclip==1.8.2
```

### 5. Estrutura de Diretórios

O programa criará automaticamente as pastas necessárias, mas você pode criá-las manualmente:

```bash
mkdir fonts
# Adicione a fonte ARIAL.TTF na pasta fonts
```

## ⚙️ Configuração

### 1. Fonte para Legendas

Baixe a fonte Arial (ARIAL.TTF) e coloque-a na pasta `fonts/`:

```
projeto/
│
├── fonts/
│   └── ARIAL.TTF
│
└── seu_script.py
```

### 2. Configuração do Chrome

O script criará automaticamente um perfil do Chrome. Na primeira execução:

1. Será solicitado seu e-mail e senha do Google
2. O programa fará login automático
3. O perfil será salvo para uso futuro

### 3. Variáveis de Ambiente (Opcional)

Para maior segurança, você pode criar um arquivo `.env`:

```bash
# .env
GOOGLE_EMAIL=seu.email@gmail.com
GOOGLE_PASSWORD=sua_senha_segura
```

E modificar o código para usar `python-dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv('GOOGLE_EMAIL')
SENHA = os.getenv('GOOGLE_PASSWORD')
```

## 🎮 Como Usar

### Execução Básica

```bash
python seu_script.py
```

### Passo a Passo de Uso

#### 1. Inicialização
Ao executar o script, você verá uma interface colorida no terminal explicando o processo.

#### 2. Inserção de Dados

```
📧 Insira o seu E-mail: seu.email@gmail.com
🗝️ Insira a sua Senha: ********
```

#### 3. Definição de Temas

```
🎯 Insira o seu Tema: inteligencia artificial
1° Termo: inteligencia artificial
2° Termo: fisica quantica
3° Termo: astronomia
4° Termo: biologia marinha
5° Termo: e  (digite 'e' para encerrar antes de 6 temas)
```

#### 4. Configuração de Pastas

```
📁 Insira o nome da sua Pasta(Core): meu_projeto
💻 Insira o índice da sua Unidade de Processamento: 1
🗂️ Insira o nome da sua Pasta(Bin): dados_temp
📁 Insira o nome da sua Pasta(PROMPT): prompts
```

#### 5. Processamento Automático

O sistema executará automaticamente:
- ✅ Login no Google
- ✅ Acesso ao ChatGPT
- ✅ Geração de roteiros
- ✅ Criação de narrações
- ✅ Download de vídeos
- ✅ Processamento de vídeo
- ✅ Adição de legendas
- ✅ Upload no YouTube

### Exemplo de Sessão Completa

```bash
$ python seu_script.py

Olá, boa tarde
✨ Seja, Bem - Vindo

🏃‍♂️ Para agilizarmos o processo, precisarei lhe explicar como o processo funcionará

[... instruções ...]

🚀 Iniciando o Sistema

📧 Insira o seu E-mail: anderson@example.com
🗝️ Insira a sua Senha: ********
🎯 Insira o seu Tema: 
1° Termo: curiosidades sobre o espaço
2° Termo: fatos sobre animais marinhos
3° Termo: e

📁 Insira o nome da sua Pasta(Core): shorts_project
💻 Insira o índice da sua Unidade de Processamento: 1
🗂️ Insira o nome da sua Pasta(Bin): temp_data
📁 Insira o nome da sua Pasta(PROMPT): prompts

🔄 Fechando todas as janelas do seu Google Chrome para evitar conflito
||||||||||||||||||||||||||||||||||||||||||||||||||||
100%

[... processamento ...]

✅ Processo concluído com sucesso!
```

## 📁 Estrutura do Projeto

```
projeto/
│
├── .venv/                          # Ambiente virtual Python
│
├── fonts/                          # Fontes para legendas
│   └── ARIAL.TTF
│
├── core/                           # Pasta principal (criada durante execução)
│   ├── Videos/                     # Vídeos baixados do Freepik
│   ├── Videos_sem_audio/           # Vídeos processados sem áudio
│   ├── Shorts_sem_audio/           # Shorts individuais sem áudio
│   ├── Shorts_audioless/           # Shorts concatenados sem áudio
│   ├── Audios/                     # Narrações em MP3
│   ├── Shorts_com_Audio/           # Shorts com narração
│   ├── shorts/                     # Shorts finais com legendas
│   └── prompts.json                # Roteiros gerados
│
├── prompt/                         # Prompts temporários (criada durante execução)
│   └── [arquivos .txt]
│
├── bin/                            # Dados temporários no disco escolhido
│   └── Default/                    # Perfil do Chrome
│
├── prompt.txt                      # Template de prompt (temporário)
├── seu_script.py                   # Script principal
├── requirements.txt                # Dependências Python
├── README.md                       # Este arquivo
└── .gitignore                      # Arquivos ignorados pelo Git
```

### Descrição dos Diretórios

#### `/core` (Pasta Principal do Projeto)
- **Videos/**: Armazena vídeos brutos baixados do Freepik (5 vídeos por tema)
- **Videos_sem_audio/**: Vídeos após redimensionamento e crop (intermediário)
- **Shorts_sem_audio/**: Clipes individuais cortados para duração calculada
- **Shorts_audioless/**: Shorts concatenados finais sem áudio
- **Audios/**: Arquivos MP3 de narração gerados pelo gTTS
- **Shorts_com_Audio/**: Shorts após adição de narração
- **shorts/**: **Produto final** - Shorts com legendas prontos para upload
- **prompts.json**: Arquivo JSON com roteiros organizados por tema

#### `/prompt` (Pasta Temporária)
Armazena prompts customizados antes do envio ao ChatGPT. Deletada após uso.

#### `/bin` (Pasta no Disco Escolhido)
Contém o perfil do Chrome para manter sessão logada. Estrutura:
```
bin/
└── Default/
    ├── Cache/
    ├── Cookies
    ├── Preferences
    └── [outros arquivos do Chrome]
```

## 🔄 Fluxo de Trabalho Detalhado

### Fase 1: Coleta de Informações (5-10 minutos)

```python
# 1. Coleta de credenciais
EMAIL = input("Insira seu e-mail: ")
SENHA = input("Insira sua senha: ")

# 2. Coleta de temas (até 6)
_TEMAS = {}
for i in range(1, 7):
    tema = input(f"{i}° Termo: ")
    if tema.lower() == 'e':
        break
    _TEMAS[i] = tema

# 3. Configuração de diretórios
CORE = input("Nome da pasta Core: ")
UDP = input("Índice da unidade: ")
BIN = input("Nome da pasta Bin: ")
PROMPT = input("Nome da pasta Prompt: ")
```

### Fase 2: Login e Autenticação (2-5 minutos)

```python
# 1. Fecha instâncias anteriores do Chrome
CMD('close', None)

# 2. Inicia Chrome com perfil personalizado
driver = undetected_chromedriver.Chrome(options=criar_configuracao(caminho))

# 3. Realiza login no Google
button_login_selenium(driver)
input_login_email_selenium(driver, EMAIL)
input_login_send_selenium(driver)
input_login_password_selenium(driver, SENHA)
input_login_send_selenium(driver)

# 4. Acessa ChatGPT e faz login via Google
driver.get("https://www.chatgpt.com/")
input_div_enter_account_gpt(driver)
input_continue_google_account_gpt(driver)
```

### Fase 3: Geração de Roteiros (5-15 minutos)

```python
# 1. Cria prompts customizados para cada tema
temas_prompt(PROMPT, temas_, 'prompt.txt')

# 2. Envia prompts ao ChatGPT e coleta respostas
input_value_prompt_gpt(driver, PROMPT)

# 3. Salva respostas em JSON
json_file(prompts_files(narracao, _TEMAS), CORE)
```

**Exemplo de Prompt Enviado:**
```
chat, não responde mais nada, e traga apenas um texto bem animado, 
explicando [curiosidades sobre o espaço] de modo que seja apenas 1 minuto, 
inspire-se em vídeos de shorts, e começe com um, "Você sabia que os(as) 
[curiosidades sobre o espaço]..." começe assim e não envie mais nada a não 
ser a fala do vídeo, sem separações ou marcações apenas o texto cru
```

### Fase 4: Geração de Narração (1-3 minutos)

```python
# 1. Lê roteiros do JSON
with open('prompts.json', 'r') as file:
    dados = json.load(file)

# 2. Gera áudio para cada roteiro
for key in dados:
    texto = dados[key]
    voz = gTTS(text=texto, lang='pt', slow=False)
    voz.save(f'narracao-{key}.mp3')
```

### Fase 5: Download de Vídeos (10-20 minutos)

```python
# 1. Login no Freepik
video_login(driver)

# 2. Para cada tema:
for tema in temas_:
    # 2.1. Busca vídeos relacionados
    # 2.2. Aplica filtros (gratuito, vídeo)
    # 2.3. Extrai links de 5 vídeos
    # 2.4. Faz download de cada vídeo
    video_input(driver, tema, file_videos_aloqued)
```

### Fase 6: Processamento de Vídeo (5-15 minutos por tema)

```python
# 1. Para cada tema, calcula duração de cada clipe
duration = 60 // numero_de_videos  # Ex: 60s ÷ 5 vídeos = 12s cada

# 2. Redimensiona e corta cada vídeo
for video in videos:
    # 2.1. Carrega vídeo
    clip = VideoFileClip(video)
    
    # 2.2. Calcula escala para 1080x1920
    scale = max(1080/clip.w, 1920/clip.h)
    
    # 2.3. Redimensiona
    resized = clip.resized(scale)
    
    # 2.4. Crop centralizado
    cropped = resized.cropped(
        x_center=resized.w/2,
        y_center=resized.h/2,
        width=1080,
        height=1920
    )
    
    # 2.5. Corta duração
    final_clip = cropped.subclipped(0, duration)

# 3. Concatena todos os clipes
final_short = concatenate_videoclips(clips)
```

### Fase 7: Adição de Áudio (2-5 minutos)

```python
# 1. Carrega vídeo e áudio
video = VideoFileClip('short_sem_audio.mp4')
audio = AudioFileClip('narracao.mp3')

# 2. Combina áudio com vídeo
short_com_audio = video.with_audio(audio)

# 3. Exporta
short_com_audio.write_videofile('short_com_audio.mp4')
```

### Fase 8: Geração de Legendas (3-10 minutos)

```python
# 1. Divide texto em palavras
palavras = texto_completo.split()

# 2. Calcula tempo por palavra
tempo_por_palavra = video.duration / len(palavras)

# 3. Cria legenda para cada palavra
clips_legendas = []
for i, palavra in enumerate(palavras):
    inicio = i * tempo_por_palavra
    
    legenda = TextClip(
        font='fonts/ARIAL.TTF',
        text=palavra,
        font_size=90,
        color='yellow',
        stroke_color='black',
        stroke_width=3
    ).with_position(("center", video.h - 170)) \
     .with_start(inicio) \
     .with_duration(tempo_por_palavra)
    
    clips_legendas.append(legenda)

# 4. Compõe vídeo final
final = CompositeVideoClip([video] + clips_legendas)
```

### Fase 9: Upload no YouTube (5-10 minutos)

```python
# 1. Acessa YouTube Studio
driver.get('https://www.youtube.com/')

# 2. Navega até área de shorts
# 3. Clica em "Enviar vídeos"
# 4. Seleciona todos os shorts
# 5. Usa PyAutoGUI para upload múltiplo
pyperclip.copy(caminhos_dos_videos)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('ENTER')
```

## 🔧 Funções Principais

### 1. Sistema de Auto-Reset

```python
def executar_com_auto_reset(func, nav, caminho, *args, max_tentativas=5):
    """
    Executa uma função com sistema de recuperação automática.
    
    Args:
        func: Função a ser executada
        nav: Instância do WebDriver
        caminho: Caminho do perfil do Chrome
        *args: Argumentos da função
        max_tentativas: Número máximo de tentativas
    
    Returns:
        nav: Instância do WebDriver (possivelmente recriada)
    
    Raises:
        RuntimeError: Se todas as tentativas falharem
    """
```

**Exceções Tratadas:**
- `WebDriverException` - Falha geral do Selenium
- `ProtocolError` - Erro de protocolo HTTP
- `ConnectionResetError` - Conexão perdida
- `TimeoutException` - Timeout de elemento
- `StaleElementReferenceException` - Elemento obsoleto
- `ElementNotInteractableException` - Elemento não interagível
- `ElementClickInterceptedException` - Clique bloqueado
- `ReadTimeoutError` - Timeout de leitura
- `TimeoutError` - Timeout geral
- `SocketTimeout` - Timeout de socket

**Funcionamento:**
1. Tenta executar a função
2. Em caso de erro, fecha o navegador
3. Aguarda 5 segundos
4. Reinicia o Chrome com o perfil salvo
5. Tenta novamente (até 5 vezes)
6. Lança exceção se todas as tentativas falharem

### 2. Processamento de Vídeo

```python
def recortar_shorts(dir, name, new_duration, dir_dest):
    """
    Redimensiona e corta vídeos para formato de shorts.
    
    Args:
        dir: Diretório dos vídeos originais
        name: Nome do tema para filtrar vídeos
        new_duration: Duração desejada para cada clipe
        dir_dest: Diretório de destino
    
    Processo:
        1. Carrega vídeo
        2. Calcula escala para 1080x1920
        3. Redimensiona mantendo proporção
        4. Crop centralizado
        5. Corta na duração especificada
        6. Salva em pasta temporária
    """
```

**Cálculo de Escala:**
```python
target_width = 1080
target_height = 1920
scale_width = target_width / video.w
scale_height = target_height / video.h
scale = max(scale_width, scale_height)  # Garante que preencha toda a tela
```

### 3. Geração de Legendas

```python
def criar_legendas(video, texto):
    """
    Gera legendas animadas palavra por palavra.
    
    Args:
        video: VideoFileClip do short
        texto: Texto completo da narração
    
    Returns:
        clips_legendas: Lista de TextClips animados
    
    Configurações:
        - Fonte: ARIAL.TTF
        - Tamanho: 90px
        - Cor: Amarelo (#FFFF00)
        - Borda: Preta, 3px
        - Posição: Centro inferior (170px de margem)
        - Largura máxima: 980px (video.w - 100)
    """
```

## 🐛 Troubleshooting

### Problema 1: Chrome não abre ou fecha imediatamente

**Sintoma:**
```
Error: selenium não está respondendo
Driver Morreu...
```

**Soluções:**
1. Verifique se o Chrome está atualizado
2. Limpe o diretório `bin` (perfil do Chrome)
3. Execute como administrador
4. Desative antivírus temporariamente

```bash
# Limpar perfil do Chrome
rmdir /s /q "D:\bin"  # Ou caminho escolhido
```

### Problema 2: Timeout ao buscar elementos

**Sintoma:**
```
TimeoutException: Message: 
```

**Soluções:**
1. Aumente os tempos de espera:
```python
WebDriverWait(nav, 120)  # Era 60, agora 120
```

2. Verifique sua conexão de internet
3. O site pode ter mudado a estrutura

### Problema 3: Erro ao processar vídeo

**Sintoma:**
```
ValueError: invalid literal for int() with base 10
IOError: [Errno 2] No such file or directory
```

**Soluções:**
1. Verifique se os vídeos foram baixados:
```python
print(os.listdir('core/Videos'))
```

2. Verifique espaço em disco
3. Certifique-se de que o FFmpeg está instalado:
```bash
ffmpeg -version
```

Se não estiver, instale:
- Windows: Baixe de https://ffmpeg.org/ e adicione ao PATH
- Linux: `sudo apt install ffmpeg`

### Problema 4: Fonte não encontrada para legendas

**Sintoma:**
```
OSError: cannot open resource
```

**Solução:**
1. Certifique-se de que `ARIAL.TTF` está em `fonts/`
2. Ou use fonte do sistema:
```python
font='Arial'  # Em vez de 'fonts/ARIAL.TTF'
```

### Problema 5: ChatGPT não responde

**Sintoma:**
- Bot fica esperando resposta indefinidamente

**Soluções:**
1. Verifique manualmente se o ChatGPT está funcionando
2. Sua conta pode ter atingido o limite de requisições
3. Ajuste o XPath do elemento de resposta:
```python
# Versão atual
"//div[contains(@class , 'markdown')]"

# Se não funcionar, inspecione o elemento e atualize
```

### Problema 6: Upload no YouTube falha

**Sintoma:**
- Vídeos não são selecionados
- PyAutoGUI não cola os caminhos

**Soluções:**
1. Execute com privilégios de administrador
2. Verifique se a janela está em foco:
```python
# Antes do pyautogui
import time
time.sleep(5)  # Dá tempo para focar manualmente
```

3. Teste o clipboard:
```python
import pyperclip
pyperclip.copy("teste")
print(pyperclip.paste())
```

### Problema 7: Memória insuficiente

**Sintoma:**
```
MemoryError
```

**Soluções:**
1. Processe menos temas por vez (2-3 em vez de 6)
2. Feche programas desnecessários
3. Use vídeos de menor resolução no Freepik
4. Adicione limpeza de memória:
```python
import gc
gc.collect()
```

## 📊 Otimizações e Melhorias

### Performance

1. **Processamento Paralelo**
```python
from multiprocessing import Pool

def processar_video(args):
    video, duration = args
    # ... código de processamento

with Pool(4) as p:  # 4 processos paralelos
    p.map(processar_video, [(v, d) for v, d in videos])
```

2. **Cache de Downloads**
```python
# Evita baixar o mesmo vídeo duas vezes
cache = {}
if url in cache:
    return cache[url]
```

### Qualidade

1. **Filtros de Vídeo**
```python
# Adicione verificação de qualidade
if video.size[0] < 1920 or video.size[1] < 1080:
    print(f"Vídeo de baixa qualidade ignorado: {video}")
    continue
```

2. **Legendas Melhoradas**
```python
# Adicione sombra para melhor legibilidade
legenda = TextClip(
    ...,
    method='caption',
    bg_color='rgba(0,0,0,0.5)',  # Fundo semi-transparente
    padding=10
)
```

### Confiabilidade

1. **Logs Detalhados**
```python
import logging

logging.basicConfig(
    filename='automacao.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Iniciando processamento...")
```

2. **Checkpoint System**
```python
# Salva progresso a cada etapa
checkpoint = {
    'roteiros_gerados': True,
    'videos_baixados': False,
    'processamento_completo': False
}

with open('checkpoint.json', 'w') as f:
    json.dump(checkpoint, f)
```

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Siga os passos abaixo:

### 1. Fork o Projeto

Clique no botão "Fork" no canto superior direito da página do GitHub.

### 2. Clone seu Fork

```bash
git clone https://github.com/seu-usuario/automacao-shorts-youtube.git
cd automacao-shorts-youtube
```

### 3. Crie uma Branch

```bash
git checkout -b feature/minha-feature
# ou
git checkout -b fix/meu-bugfix
```

### 4. Faça suas Alterações

- Mantenha o código limpo e documentado
- Siga a PEP 8 (style guide Python)
- Adicione comentários explicativos

### 5. Teste suas Alterações

```bash
python seu_script.py
```

### 6. Commit suas Mudanças

```bash
git add .
git commit -m "feat: adiciona funcionalidade X"
# ou
git commit -m "fix: corrige bug Y"
```

**Formato de Commits (Conventional Commits):**
- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Alteração em documentação
- `style:` Formatação de código
- `refactor:` Refatoração de código
- `test:` Adição de testes
- `chore:` Tarefas gerais

### 7. Push para o GitHub

```bash
git push origin feature/minha-feature
```

### 8. Abra um Pull Request

Vá até seu fork no GitHub e clique em "New Pull Request".

### Diretrizes de Contribuição

- ✅ Código limpo e bem documentado
- ✅ Commits descritivos
- ✅ Testes quando aplicável
- ✅ Atualização do README quando necessário
- ❌ Não incluir credenciais ou dados sensíveis
- ❌ Não fazer commits diretamente na branch main

## 🗺️ Roadmap

### Versão 2.0 (Planejado)

- [ ] **Interface Gráfica (GUI)**
  - Tkinter ou PyQt5
  - Visualização de progresso em tempo real
  - Configuração visual de parâmetros

- [ ] **Suporte a Múltiplas Plataformas**
  - TikTok
  - Instagram Reels
  - Facebook Reels

- [ ] **Melhorias de IA**
  - Integração com GPT-4
  - Geração de thumbnails automáticas
  - Sugestões de tags e descrições

- [ ] **Analytics**
  - Dashboard de desempenho
  - Análise de engajamento
  - Sugestões de melhorias

### Versão 2.1 (Futuro)

- [ ] **Agendamento de Posts**
  - Sistema de fila
  - Publicação em horários otimizados

- [ ] **Banco de Dados**
  - PostgreSQL ou MongoDB
  - Histórico de vídeos
  - Análise de tendências

- [ ] **API REST**
  - Controle via API
  - Integração com outros sistemas

- [ ] **Testes Automatizados**
  - Unit tests
  - Integration tests
  - CI/CD pipeline

### Versão 3.0 (Longo Prazo)

- [ ] **Machine Learning**
  - Previsão de viralização
  - Otimização automática de conteúdo

- [ ] **Comunidade**
  - Marketplace de templates
  - Compartilhamento de prompts

## ⚠️ Avisos Importantes

### Uso Responsável

- ✅ Use apenas com suas próprias contas
- ✅ Respeite os termos de serviço de cada plataforma
- ✅ Dê crédito ao conteúdo original quando aplicável
- ❌ Não use para spam ou conteúdo malicioso
- ❌ Não abuse das APIs (respeite rate limits)

### Limitações Conhecidas

1. **Dependência de Layout**: O script usa XPath para localizar elementos. Se o layout de qualquer site mudar, o script pode quebrar.

2. **Captchas**: Em alguns casos, captchas podem aparecer e o processo será interrompido.

3. **Limites de API**: O ChatGPT gratuito tem limites de requisições por hora.

4. **Processamento Intensivo**: O processamento de vídeo consome muitos recursos. Não recomendado para laptops com pouca RAM.

5. **Windows Only**: Alguns comandos são específicos do Windows (`taskkill`, paths com `\`).

### Legalidade

- ✅ O código é open-source e pode ser modificado livremente
- ⚠️ Certifique-se de ter direitos sobre o conteúdo usado
- ⚠️ Vídeos do Freepik gratuitos possuem licenças específicas
- ⚠️ Leia os termos de uso do YouTube, ChatGPT e Freepik

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2024 [Seu Nome]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 📞 Contato

**Anderson** - Desenvolvedor Python

- GitHub: [@AndersonTechEnthusiast](https://github.com/AndersonTechEnthusiast)
- LinkedIn: [Anderson](https://www.linkedin.com/in/anderson-pires-97131b247)
- Email: andersonpiresdacruz@gmail.com

**Link do Projeto:** [https://github.com/seu-usuario/automacao-shorts-youtube](https://github.com/AndersonTechEnthusiast/ShortForge)

## 🙏 Agradecimentos

- [Selenium](https://www.selenium.dev/) - Framework de automação web
- [MoviePy](https://zulko.github.io/moviepy/) - Biblioteca de edição de vídeo
- [gTTS](https://gtts.readthedocs.io/) - Google Text-to-Speech
- [Undetected ChromeDriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) - ChromeDriver modificado
- [ChatGPT](https://chat.openai.com/) - IA para geração de conteúdo
- [Freepik](https://www.freepik.com/) - Plataforma de recursos visuais
- Comunidade Python - Pelo suporte e recursos

## 📈 Status do Projeto

![Status](https://img.shields.io/badge/status-active-success)
![Maintenance](https://img.shields.io/badge/maintained-yes-green)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

**Última atualização:** Janeiro 2024

---

<p align="center">
  Feito com ❤️ e ☕ por Anderson
</p>

<p align="center">
  <sub>⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!</sub>

</p>
