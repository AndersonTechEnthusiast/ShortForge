from colorama import Fore as Cor
from datetime import datetime as horario
from time import sleep as dormir
from re import fullmatch as correspondencia_total
from psutil import disk_partitions as particoes_do_disco
from os.path import join as juntar
from os.path import exists as existir
from os.path import isfile as e_um_arquivo
from os import makedirs as diretorio
from os import listdir as listar
from os import system as cmd
from os import remove as apagar
from shutil import rmtree as remover
from json import dump as descarregar # escrever 
from json import load as carregar # ler
import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchWindowException # elemento não encontrado na janela (usado usualmente uma janela fecha rapidamente)
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
import undetected_chromedriver
from selenium.webdriver.common.action_chains import ActionChains
from gtts import gTTS
import requests
from urllib3.exceptions import ProtocolError
from urllib3.exceptions import ReadTimeoutError
from socket import timeout as SocketTimeout
from moviepy import VideoFileClip
from moviepy import VideoClip
from moviepy import concatenate_videoclips
from moviepy import AudioFileClip
from moviepy import TextClip
from moviepy import CompositeVideoClip
from moviepy.video.fx import FadeIn
from moviepy.video.fx import FadeOut
import traceback
import pyautogui
from os.path import abspath as caminho_absoluto
import pyperclip
narracao = []
if existir('.venv/Lib/site-packages/__pycache__'):
    if len(listar('.venv/Lib/site-packages/__pycache__')) > 0:
        remover('.venv/Lib/site-packages/__pycache__')
#________________________________________________________________________________INFORMAÇÕES DO USUÁRIO________________________________________________________________________________#
#__________Funções__________#
def CMD(action,path):
    if action == 'close':
        return cmd('start "" taskkill /F /IM chrome.exe')
    if action == 'insert':
        return cmd(f'start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir="{path}"')
def selenium_vivo(nav):
    try:
        nav.current_url
        return True
    except:
        return False
def criar_configuracao(caminho_):
    options = Options()
    options.add_argument(f'--user-data-dir={caminho_}')
    options.add_argument('--profile-directory=Default')
    return options
def executar_com_auto_reset(func, nav, caminho, *args, max_tentativas=5):
    tentativa = 0

    while tentativa < max_tentativas:
        try:
            if not selenium_vivo(nav):
                raise WebDriverException("Driver Morreu...")

            func(nav, *args)
            return nav  # sucesso → sai da função

        except (
            WebDriverException,
            ProtocolError,
            ConnectionResetError,
            TimeoutException,
            StaleElementReferenceException,
            ElementNotInteractableException,
            ElementClickInterceptedException,
            ReadTimeoutError,
            TimeoutError,
            SocketTimeout
        ) as e:
            tentativa += 1
            print(f"Error: {e}")
            print(f"Selenium caiu ({tentativa}/{max_tentativas}) → reiniciando...")

            try:
                nav.quit()
            except Exception:
                pass  # se já morreu, segue o jogo

            CMD('close', None)
            dormir(5)

            nav = undetected_chromedriver.Chrome(
                options=criar_configuracao(caminho),
                use_subprocess=True
            )
            dormir(5)

    # se saiu do loop, falhou geral
    raise RuntimeError(
        f"Falha crítica: função '{func.__name__}' falhou após {max_tentativas} tentativas."
    )
def delete_dirs_start(udp,dir,file):
    if udp is not None and file is None:
        caminho = juntar(udp , dir)
        if existir(caminho):
            cmd('start "" taskkill /F /IM chrome.exe')
            dormir(5)
            remover(caminho)
        else:
            return None
    elif udp is None and file is None:
        if existir(dir):
            remover(dir)
        else:
            return None
    elif file:
        apagar(dir)
    else:
        None
def prompt_tema(action):
    if action == 'create':
        with open('prompt.txt','w',encoding='utf-8') as arquivo:
            arquivo.write('chat , não responde mais nada , e traga apenas um texto bem animado , explicando [tema] de modo que seja apenas 1 minuto , inspire-se em vídeos de shorts , e começe com um , "Você sabia que os(as) [tema]..." começe assim e não envie mais nada a não ser a fala do vídeo , sem sepações ou marcações apenas o texto cru')
    elif action == 'delete':
        apagar('prompt.txt')
def horas():
    
    agora = horario.now()
    
    hora = agora.strftime("%H:%M:%S")
    
    H = int(hora.split(":")[0])
    
    M = int(hora.split(":")[1])
    
    S = int(hora.split(":")[2])
    
    if H <= 12:
        return "bom dia"
    elif H > 12 and H <= 18:
        return "boa tarde"
    elif H > 18:
        return "boa noite"
    else:
        return "boa madrugada"
def mensagem(value):
    mensagens = {
        'M-01':Cor.WHITE+'Olá , '+Cor.GREEN+f'{horas()}'+Cor.WHITE+'\n',
        'M-02':Cor.WHITE+'✨ Seja , Bem - Vindo \n',
        'M-03':Cor.WHITE+'🏃‍♂️ Para agilizarmos o '+Cor.GREEN+'processo'+Cor.WHITE+' , precisarei lhe explicar como o '+Cor.GREEN+'processo'+Cor.WHITE+' funcionará\n',
        'M-04':Cor.WHITE+'1️⃣  - Adicione o seu '+Cor.GREEN+'E-mail'+Cor.WHITE+' que você mais usa e que esteja mais completo no Cadastro do '+Cor.GREEN+'Google'+Cor.WHITE+' !! \n',
        'M-05':Cor.WHITE+'2️⃣  - Adicione a sua '+Cor.GREEN+'Senha'+Cor.WHITE+' do '+Cor.GREEN+'E-mail'+Cor.WHITE+' que você inseriu anteriormente para cadastro !! \n',
        'M-06':Cor.WHITE+'3️⃣  - Adicione os '+Cor.GREEN+'Temas'+Cor.WHITE+' do seu interesse !! \n',
        'M-07':Cor.WHITE+'4️⃣  - Adicione o nome da '+Cor.YELLOW+'Pasta'+Cor.GREEN+' Core '+Cor.WHITE+'!!!'+Cor.MAGENTA+' (pasta que ficará no seu projeto e guardará seus vídeos)'+Cor.WHITE+'\n',
        'M-08':Cor.WHITE+'5️⃣  - Adicione o nome da '+Cor.YELLOW+'Pasta'+Cor.GREEN+' Bin '+Cor.WHITE+'!!!'+Cor.MAGENTA+' (pasta que ficará na sua Unidade de Processamento)'+Cor.WHITE+'\n',
        'M-09':Cor.WHITE+'6️⃣  - Adicione qual a '+Cor.GREEN+'Unidade de Processamento '+Cor.WHITE+'do seu '+Cor.BLUE+'Computador !!!'+Cor.MAGENTA+'(Unidade de Processamento: Pendrive (D:/) ou Computador (C:/) ou qualquer outra que tiver)'+Cor.WHITE+'\n',
        'M-10':Cor.WHITE+'7️⃣  - Adicione o nome da '+Cor.YELLOW+'Pasta'+Cor.WHITE+' do '+Cor.GREEN+'Prompt'+Cor.MAGENTA+' (Pasta onde guardaremos o prompt disponibilizados por uma I.A externa ao código)'+Cor.WHITE+'\n',
        'M-11':Cor.WHITE+'⚠️  - '+Cor.YELLOW+'Atenção'+Cor.WHITE+' nosso '+Cor.GREEN+'sistema '+Cor.WHITE+'possui um prompt proprio imbutido , pensado especialmente para ajudar e facilitar o progresso , um prompt treinado e testado com metodos de repetição para o texto',
        'break':'\n',
        'M-12':Cor.WHITE+'🚀  - Iniciando o '+Cor.GREEN+' Sistema '+Cor.WHITE+'\n',
        'M-13':Cor.WHITE+'📧  - Insira o seu '+Cor.GREEN+'E-mail'+Cor.WHITE+': ',
        'M-14':Cor.WHITE+'🗝️  - Insira a sua '+Cor.GREEN+'Senha'+Cor.WHITE+': ',
        'M-15':Cor.WHITE+'🎯  - Insira o seu '+Cor.GREEN+'Tema'+Cor.WHITE+': ',
        'M-16':Cor.WHITE+'📁  - Insira o nome da sua '+Cor.YELLOW+'Pasta'+Cor.BLUE+'(Core)'+Cor.WHITE+': ',
        'M-17':Cor.WHITE+'🗂️  - Insira o nome da sua '+Cor.YELLOW+'Pasta'+Cor.BLUE+'(Bin)'+Cor.WHITE+': ',
        'M-18':Cor.WHITE+'💻  - Insira o índice da sua '+Cor.BLUE+'Unidade de Processamento'+Cor.WHITE+': ',
        'M-19':Cor.WHITE+'📁  - Insira o nome da sua '+Cor.YELLOW+'Pasta'+Cor.BLUE+'(PROMPT)'+Cor.WHITE+': ',
        'M-20':Cor.WHITE+'🔄  - Fechando todas as janelas do seu Google Chrome para evitar conflito\n',
        'M-21':Cor.WHITE+'🔄  - Baixando todos os requesitos para abrir o Google Externamente em sua Máquina\n',
        'M-22':Cor.WHITE+'🔄  - Fechando o Google Chrome externo para evitar configurações desnecessarias e adiantar o processo\n'
    }
    return mensagens
def error(value):
    errors = {
        'M-01':Cor.RED+'❌ Error ❌'+Cor.WHITE+', o e-mail não pode ser '+Cor.RED+'nulo'+Cor.WHITE+'\n',
        'M-02':Cor.RED+'❌ Error ❌'+Cor.WHITE+', a senha não pode ser '+Cor.RED+'nulo'+Cor.WHITE+'\n',
        'M-03':Cor.RED+'❌ Error ❌'+Cor.WHITE+', o nome da Pasta não pode conter '+Cor.RED+'caracteres especiais ou espaços '+Cor.WHITE+'ou o nome da Pasta que você mencionou já '+Cor.RED+'existe'+Cor.WHITE+' no seu diretório'+'\n',
        'M-04':Cor.RED+'❌ Error ❌'+Cor.WHITE+', nenhum índice coerente com as Unidades de Processamento encontradas em seu Computador \n',
        'M-05':Cor.RED+'❌ Error ❌'+Cor.WHITE+', a pasta mencionada já se encontra em seu projeto , é necessario que tente criar outra pasta \n'
    }
    return errors
def exibir_mensagem(value,timeout):
    for letra in value:
        print(f"{letra}",end="",flush=True)
        dormir(timeout)
    return " "
def exibir_input(value,timeout):
    for letra in value:
        print(f"{letra}",end="",flush=True)
        dormir(timeout)
    return input("")
def exibir_reparticoes():
    udps = particoes_do_disco()
    for ind, udp in enumerate(udps,1):
        print(f"{ind}° <=> {udp.device}")
    return ""
def reparticoes(value):
    value = int(value)
    udps = particoes_do_disco()
    udps_ = {}
    for ind,udp in enumerate(udps,1):
        udps_[ind] = udp.device
    indices = [i for i in udps_]
    if value in indices:
        return udps_[value]
    else:
        return False
def pasta(name,extra,action):
    if extra is None:
        if action == 'create':
            if not existir(name):
                diretorio(name)
                return True
            else:
                return False
        if action == 'delete':
            if existir(name):
                remover(name)
                return True
            else:
                return False
    else:
        if action == 'create':
            udp = reparticoes(extra)
            arquivo = juntar(udp , name)
            if not existir(arquivo):
                diretorio(arquivo)
                return True
            else:
                return False
        elif action == 'delete':
            udp = reparticoes(extra)
            arquivo = juntar(udp , name)
            if existir(arquivo):
                remover(arquivo)
                return True
            else:
                return False
def filtro_input(value,action,extra):
    if action == 'email':
        if not str(value).strip():
            return False
        elif len(str(value)) < 11:
            return False
        else:
            return True
    if action == 'senha':
        if not str(value).strip():
            return False
        else:
            return True
    if action in ['core','bin','prompt']:
        if correspondencia_total(r'^[A-Za-z0-9_]+$',value):
            if action == 'core':
                return pasta(value,extra,'create')
            if action == 'bin':
                return pasta(value,extra,'create')
            if action == 'prompt':
                return pasta(value,extra,'create')
        else:
            return False
    if action == 'udp':
        value = int(value)
        udps = particoes_do_disco()
        udps_ = {}
        for ind,udp in enumerate(udps,1):
            udps_[ind] = udp.device
        indices = [i for i in udps_] # adiciona apenas os indices {0:...,1:...,2:...} | apenas os [0,1,2,...]
        if not isinstance(value , int):
            return False
        if int(value) in indices:
            return True
        else:
            return False
    else:
        return False
def while_error(action,timeout):
    value = ""
    if action == 'email':
        value = error(None)['M-01']
        for letra in value:
            print(f"{letra}",end="",flush=True)
            dormir(timeout)
        return exibir_input(mensagem(None)['M-13'],0.02)
    if action == 'senha':
        value = error(None)['M-02']
        for letra in value:
            print(f"{letra}",end="",flush=True)
            dormir(timeout)
        return exibir_input(mensagem(None)['M-14'],0.02)
    if action in ['core','bin','prompt']:
        value = error(None)['M-03']
        if action == 'core':
            for letra in value:
                print(f"{letra}",end="",flush=True)
                dormir(timeout)
            return exibir_input(mensagem(None)['M-16'],0.02)
        if action == 'bin':
            for letra in value:
                print(f"{letra}",end="",flush=True)
                dormir(timeout)
            return exibir_input(mensagem(None)['M-17'],0.02)
        if action == 'prompt':
            for letra in value:
                print(f"{letra}",end="",flush=True)
                dormir(timeout)
            return exibir_input(mensagem(None)['M-19'],0.02)
    if action == 'udp':
        value = error(None)['M-04']
        for letra in value:
            print(f"{letra}",end="",flush=True)
            dormir(timeout)
        return exibir_input(mensagem(None)['M-18'],0.02)
def temas(value):
    if isinstance(value ,dict):
        temas = {}
        temp = []
        for keys in value:
            item = value[keys]
            if str(item).strip() and not str(item).isdigit():
                if str(item) not in temp:
                    temp.append(str(item))
        for ind,item in enumerate(temp,1):
            temas[ind] = item
        return temas
def prompts(value,dir,prompt):
    
    if isinstance(value , dict) and isinstance(prompt , list):
    
        textos_prompt = {}
    
        for k,texto in zip(value , prompt):
    
            key = value[k]
    
            textos_prompt[key] = texto 
    
        for Key in textos_prompt:
    
            texto = textos_prompt[Key]
    
            name = str(Key).strip().replace(" ","_")
    
            caminho = juntar(dir , name)
    
            with open(caminho , 'w' , encoding='utf-8') as arquivo:
    
                arquivo.write(str(texto))
    
        count_files = listar(dir)
    
        if len(count_files) > 0:
            return True
        else:
            return False
def path(dir,interdir):
    pasta = juntar(dir , interdir)
    return pasta
def loading(message,timeout,time):
    for text in message:
        print(f"{text}",end="",flush=True)
        dormir(timeout)
    # print("\n")
    porcent = 100
    pont = Cor.GREEN+'|'
    for i in range(100):
        num = i + 1
        pont = pont + '|'
        print(f"{pont}",end="",flush=True)
        print(f"\r{int((num/porcent)*porcent)}%  ",end="",flush=True)
        dormir(time)
    print(Cor.WHITE+"\n")
def temas_prompt(dir,temas,prompt):
    if existir(dir):
        with open(prompt , 'r' , encoding='utf-8') as arquivo:
            texto = arquivo.read()
        for ind in temas:
            file = temas[ind]
            tema = texto.replace('[tema]',f'{file}')
            name = str(file).strip().replace(' ','_')
            caminho = juntar(dir , name)+'.txt'
            with open(caminho , 'w' , encoding='utf-8') as arquivo:
                arquivo.write(tema)
        count = listar(dir)
        if len(count) > 0:
            return True
        else:
            return False
    else:
        return False
def button_login_selenium(nav):
    try:
        nav.get('https://accounts.google.com/ServiceLogin?hl=pt-BR&amp;passive=true&amp;continue=https://www.google.com/%3Fzx%3D1766551441599%26no_sw_cr%3D1&amp;ec=futura_exp_og_so_72776762_e')
        print("Redirecionado com Sucesso !!!")
    except TimeoutException:
        print("Não redirecionado !!!")
    return nav
def input_login_email_selenium(nav,email):
    try:
        elemento = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//input[@type='email'][@name='identifier'][@id='identifierId']"))
        )
        elemento.click()
        for letra in email:
            elemento.send_keys(letra)
            dormir(0.05)
        print("Email Inserido no Input !!!")
    except TimeoutException:
        print("Email não foi inserido porque o Input não foi encontrado no tempo Limite !!!")
    return nav
def input_login_send_selenium(nav):
    try:
        elemento = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//span[contains(text() , 'Avançar')]"))
        )
        elemento.click()
        print("o botão avançar foi clicado !!!")
    except TimeoutException:
        print("o botão de avançar de email -> senha , não foi encontrado no Tempo Limite !!!")
    return nav
def input_login_password_selenium(nav,senha):
    try:
        elemento = WebDriverWait(nav , 120).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//input[@type='password'][@name='Passwd']"))
        )
        elemento.click()
        for letra in senha:
            elemento.send_keys(letra)
            dormir(0.05)
        print("A senha foi inserida com sucesso !!!")
    except TimeoutException:
        print("A senha não foi inserida por que o input não foi encontrado no Tempo Limite !!!")
    return nav
def redic(nav):
    nav.get('https://www.chatgpt.com/')
    return nav
def continue_gpt_selenium_account(nav):
    try:
        elemento = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//button[@id='continue-as']"))
        )
        elemento.click()
        print("botão de continuar com sua conta , clicado !!!")
    except TimeoutException:
        print("botão de continua com sua conta , não apareceu !!!")
    return nav
def input_div_enter_account_gpt(nav):
    if "https://www.chatgpt.com/" not in nav.current_url:
        nav.get("https://www.chatgpt.com/")
        
    try:
        elemento = WebDriverWait(nav , 60).until(
            expected_conditions.presence_of_element_located((By.XPATH , "//div[contains(text() , 'Entrar')]"))
        )
        if elemento:
            elemento.click()
        print("Botão de Entrar no ChatGPT clicado com sucesso !!!")
    except TimeoutException:
        print("Botão de Entrar não foi encontrado !!!")
    return nav
def input_continue_google_account_gpt(nav):
    try:
        elemento = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//div[contains(text() , 'Continuar com o Google')]"))
        )
        elemento.click()
        print("Botão 'Continuar com Google' , clicado !!!")
    except TimeoutException:
        try:
            elemento = WebDriverWait(nav , 60).until(
                expected_conditions.element_to_be_clickable((By.XPATH , "//button[contains(text() , 'Continuar com o Google')]"))
            )
            elemento.click()
            print("Botão 'Continuar com Google' foi redirecionado para outra tela , foi clicado")
        except TimeoutException:
            print("Botão 'Continuar com o Google' , não foi encontrado !!!")
    return nav
def input_value_prompt_gpt(nav,dir):
    nav : WebDriver = nav
    if "https://www.chatgpt.com/" not in nav.current_url:
        nav.get("https://www.chatgpt.com/")
    for file in listar(dir):
        caminho = juntar(dir , file)
        with open(str(caminho) , 'r' , encoding='utf-8') as arquivos:
            texto = arquivos.read()
        try:
            elemento_father = WebDriverWait(nav , 60).until(
                expected_conditions.element_to_be_clickable((By.XPATH , "//div[contains(@class , '-my-2.5')]"))
            )
            elemento_father.click()
            dormir(2)
            precensa_child = WebDriverWait(nav , 60).until(
                expected_conditions.presence_of_element_located((By.XPATH , "//div[contains(@class , 'ProseMirror-focused')]"))
            )
            dormir(2)
            for letra in texto:
                precensa_child.send_keys(letra)
                dormir(0.02)
            button = WebDriverWait(nav , 60).until(
                expected_conditions.element_to_be_clickable((By.XPATH , "//button[@id='composer-submit-button']"))
            )
            button.click()
            dormir(2)
            Voz = WebDriverWait(nav,120).until(
                expected_conditions.presence_of_element_located((By.XPATH , "//button[@type='button'][@aria-label='Iniciar modo voz'][contains(@class , 'composer-submit-button-color ')]"))
            )
            if Voz:
                while True:
                    try:
                        resposta = WebDriverWait(nav , 60).until(
                            expected_conditions.element_to_be_clickable((By.XPATH , "//div[contains(@class , 'markdown')]"))
                        )
                        if str(resposta.text).strip():
                            resultado = resposta.text
                            narracao.append(resultado)
                            break
                    except: 
                        dormir(5)
                        pass
                new = WebDriverWait(nav , 60).until(
                    expected_conditions.element_to_be_clickable((By.XPATH , "//div[contains(@class , 'truncate')]"))
                )
                if new:
                    new.click()
                    print("concluído")
                    dormir(10)
        except TimeoutException:
            print("Error elemento não foi clicado")
    return nav
def prompts_files(values,keys):
    feedback = {}
    if isinstance(keys , dict):
        print(keys)
        if isinstance(values,list):
            print(values)
            for k in keys:
                key = keys[k]
                for v in values:
                    if str(key).lower() in str(v).lower():
                        feedback[key] = v
            print("Dados Alocados com sucesso!!!")
            return feedback
        else:
            print("error 'prompt' não é um dado do tipo 'list' ")
            return False
    else:
        print("error 'keys' não é um dado do tipo 'dict' ")
        return False
def json_file(dict_,path):
    if isinstance(dict_ , dict):
        print(dict_)
        if existir(path):
            caminho = juntar(path , 'prompts.json')
            with open(str(caminho) , 'w' , encoding='utf-8') as file:
                descarregar(dict_,file,ensure_ascii=False,indent=4)
            return True
        else:
            return False
    else:
        return False
def audio(path,lingua,dir):
    if existir(path):
        new_past = juntar(path , 'Audios')
        diretorio(new_past)
        with open(str(dir) , 'r' , encoding='utf-8') as arquivo:
            dados = carregar(arquivo)
        for key in dados:
            texto = dados[key]
            name = str(f'narracao-{key}.mp3')
            alocacao = juntar(new_past,name)
            voz = gTTS(text=texto,lang=lingua,slow=False)
            voz.save(alocacao)
    else:
        print("O Caminho não existe !!!")
        return False
def video_login(nav):
    nav.get("https://br.freepik.com/")
    try:
        login_start = WebDriverWait(nav,60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//a[contains(text() , 'Fazer login')]"))
        )
        login_start.click()
        print("Botão de Fazer Login no FreePik foi clicado com Sucesso !!!")
    except TimeoutException:
        print("Error , botão de fazer login não foi encontrado no tempo limite")
    
    
    try:
        iframe = WebDriverWait(nav , 60).until(
            expected_conditions.presence_of_element_located((By.XPATH , "//iframe[contains(@class , 'L5Fo6c-PQbLGe')]"))
        )
        nav.switch_to.frame(iframe)
        print("Acessando o Iframe...")
        print("Iframe Acessado com Sucesso")
    except TimeoutException:
        print("Error ao tentar acessar o Iframe")

    try:
        with_google = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//span[contains(text() , 'Continuar com o Google')]"))
        )
        with_google.click()
        print("continuando com Google...")
    except TimeoutException:
        try:
            continue_with_my_account = WebDriverWait(nav , 60).until(
                expected_conditions.element_to_be_clickable((By.XPATH , "//div[contains(@class , 'haAclf')]"))
            )
            continue_with_my_account.click()
            print("Redirecionamento de fluxo , para acessar sua conta diretamente !!!")
            print("conta selecionada com sucesso !!!")
        except TimeoutException:
            print("Error , botão de continuar com Google não foi encontrado !!!")
        
    atual = nav.current_window_handle
    janelas = nav.window_handles
    nav.switch_to.window(janelas[-1])
    
    try:
        my_account = WebDriverWait(nav , 60).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH , "//li[contains(@class , 'aZvCDf ')]"))
        )
        my_account[0].click()
        print("Conta selecionada com sucesso !!!")
    except TimeoutException:
        print("Conta não foi selecionada !!!")
    dormir(10)
    if len(janelas) > 1:
        print("existe mais janelas abertas")
        try:
            continue_with_my_account = WebDriverWait(nav , 60).until(
                expected_conditions.presence_of_element_located((By.XPATH , "//span[contains(text() , 'Continuar')]"))
            )
            continue_with_my_account.click()
            print("Conta Selecionada com sucesso e continuando com ela !!!")
        except NoSuchWindowException:
            print("Error não foi possivel continuar com a conta escolhida !!!")
        nav.switch_to.window(atual)
    else:
        nav.switch_to.window(atual)
    
    try:
        close_popup = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//button[contains(@class , '_a5lvtw10')][@type='button']"))
        )
        close_popup.click()
        print("PopUp fechado com sucesso !!!")
    except TimeoutException:
        print("Error ao fechar o popup !!!")
    
    return nav
def video_input(nav,search,dir):
    nav : WebDriver = nav
    if isinstance(search , dict):
        for key in search:
            tema = str(search[key])
            
            if "freepik" not in nav.current_url:
                nav.get("https://www.freepik.com/")
                
            try:
                form_input_search = WebDriverWait(nav,60).until(
                    expected_conditions.presence_of_element_located((By.XPATH , "//div[contains(@class , 'relative')]"))
                )
                if form_input_search:
                    form_input_search.click()
                    print("formulario clicado !!!")
            except TimeoutException:
                print("formulario não foi clicado !!!")    
            
            try:
                input_search = WebDriverWait(nav , 60).until(
                    expected_conditions.element_to_be_clickable((By.XPATH , "//input[@name='term']"))
                )
                input_search.click()
                dormir(2)
                text_verify = input_search.get_attribute('value')
                dormir(2)
                if len(text_verify) > 1:
                    input_search.clear()
                dormir(2)
                for letra in tema:
                    input_search.send_keys(letra)
                    dormir(0.05)
                print("Termo adicionado no input de pesquisa !!!")
            except TimeoutException:
                print("Error ao tentar acessar o input de pesquisa")
            
            try:
                lupa = WebDriverWait(nav , 60).until(
                    expected_conditions.element_to_be_clickable((By.XPATH , "//button[@type='submit'][contains(@class , 'size-8')]"))
                )
                lupa.click()
                print("Lupa clicada !!!")
            except ElementNotInteractableException:
                try:
                    lupa = WebDriverWait(nav , 60).until(
                        expected_conditions.presence_of_element_located((By.XPATH , "//button[@type='submit'][contains(@class , 'size-8')]"))
                    )
                    lupa.click()
                except TimeoutException:
                    print("Error , Lupa de pesquisa não foi clicada !!!")
            dormir(10)
            
            try:
                dormir(10)
                videos_select = WebDriverWait(nav , 60).until(
                    expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="w-full"]'))
                )
                if videos_select:
                    videos_select.click()
                    print("botão de seleção de categorias clicado com Sucesso !!!")
            except ElementNotInteractableException:
                dormir(10)
                try:
                    videos_select = WebDriverWait(nav , 60).until(
                        expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="w-full"]'))
                    )
                    if videos_select:
                        videos_select.click()
                        print("botão de seleção de categorias clicado com Sucesso !!!")
                except TimeoutException: 
                    print("botão de seleção de categorias não foi clicado no tempo determinado !!!")
            
            dormir(5)    
            
            try:
                videos = WebDriverWait(nav , 60).until(
                    expected_conditions.element_to_be_clickable((By.XPATH , "//a[@data-cy='filter-type-video']"))
                )
                videos.click()
                print("categoria de vídeos selecionada com sucesso !!!")
            except TimeoutException:
                print("categoria de vídeos não foi selecionada no tempo limite !!!")
            
            dormir(5)
            
            try:
                licenca = WebDriverWait(nav , 60).until(
                    expected_conditions.element_to_be_clickable((By.XPATH , "//button[@type='button'][@aria-label='license options']"))
                )
                licenca.click()
                print("Botão Licença clicado")
            except TimeoutException:
                print("Error ao clicar em Liçenca")
            
            try:
                gratuito = WebDriverWait(nav , 60).until(
                    expected_conditions.element_to_be_clickable((By.XPATH , "//a[@data-cy='filter-license-free']"))
                )
                gratuito.click()
                print("gratuito clicado")
            except TimeoutException:
                print("gratuito não foi clicado !!!")
            
            dormir(10)
            while True:
                try:
                    # body = WebDriverWait(nav , 60).until(
                    #     expected_conditions.presence_of_element_located((By.XPATH , "//body[@class='_otnfkq0']"))
                    # )
                    # if body:
                    #     # Aperta a tecla END 20 vezes (ajuste conforme necessário)
                    #     for i in range(20):
                    #         body.send_keys(Keys.END)  # Vai pro final da página
                    #         dormir(1)  # Espera 1 segundo
                    #         print(f"Scroll {i+1} feito")
                        print("esperando 30 segundos...")
                        dormir(30)
                        print("buscando elementos...")
                        imagens = WebDriverWait(nav , 60).until(
                            expected_conditions.presence_of_all_elements_located((By.XPATH , "//figure//video//source"))
                        )
                        if imagens:
                            print("'imagens' encontradas")
                            for i in range(5):
                                data_src = imagens[i].get_attribute('data-src')
                                name = juntar(dir , f'{str(tema).replace(" ","-")}-{int(i)}.mp4')
                                if data_src is not None and data_src.strip():
                                    video = requests.get(str(data_src))
                                else:
                                    print(f"vazia {data_src}")
                                    continue
                                with open(name,'wb') as file:
                                    file.write(video.content)    
                                print("extração concluida com sucesso!!!")
                            if len(imagens) < 5:
                                for ind,imagem in enumerate(imagens,1):
                                    data_src = imagem.get_attribute('data-src')
                                    name = juntar(dir , f'{str(tema).replace(" ","-")}-{int(ind)}.mp4')
                                    if data_src is not None and data_src.strip():
                                        video = requests.get(str(data_src))
                                    else:
                                        print(f"vazia {data_src}")
                                        continue
                                    with open(name,'wb') as file:
                                        file.write(video.content)    
                                    print("extração concluida com sucesso!!!")
                            nav.get('https://www.freepik.com/')
                            break
                except ElementClickInterceptedException:
                    print("Elemento bloqueado por outro elemento , tentando 'ESC' ")
                    ActionChains(nav).send_keys(Keys.ESCAPE).perform()
                    dormir(5)
                    print("'ESC' pressionado , tentando novamente...")
                    continue
                except TimeoutException:
                    print("error na extração de 'links'")
                    print(f'{traceback.format_exc()}')
                    pass
    return nav
def YouTube(nav,caminho_da_pasta):
    nav : WebDriver = nav
    if "https://www.youtube.com/" not in nav.current_url:
        nav.get('https://www.youtube.com/')
    
    try: 
        Perfil = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//img[@id='img'][@alt='Imagem do avatar']"))
        )
        if Perfil:
            Perfil.click()
            print("Botão 'Criar' pressionado com sucesso !!!")
    except TimeoutException:
        print("Error botão 'Criar' não foi pressionado !!!")
    dormir(10)
    try: 
        Canal = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//a[contains(text() , 'Acessar seu canal')]"))
        )
        Canal.click()
        print("Canal clicado")
    except TimeoutException:
        print("Canal não foi clicado")
    dormir(10)
    try:
        Criar = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//a[@aria-label='Criar']"))
        )
        Criar.click()
        print("botão 'Criar' foi clicado com sucesso !!!")
    except TimeoutException:
        print("botão 'Criar' não foi clicado !!!")
    dormir(10)
    try: 
        PopUp = WebDriverWait(nav , 60).until(
            expected_conditions.visibility_of_element_located((By.XPATH , "//ytcp-uploads-dialog//tp-yt-paper-dialog[@id='dialog']"))
        )
        if PopUp:
            print("O PopUp está visivél")
            fechar = WebDriverWait(nav,60).until(
                expected_conditions.element_to_be_clickable((By.XPATH , "//ytcp-uploads-dialog//ytcp-icon-button[@id='close-button']"))
            )
            if fechar:
                fechar.click()
                print("botão clicado !!!")
    except Exception:
        print(f"{traceback.format_exc()}")
    dormir(10)
    try:
        shorts_area = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//tp-yt-paper-tab[@id='video-list-shorts-tab']"))
        )
        shorts_area.click()
    except Exception:
        print(f'{traceback.format_exc()}')
    dormir(10)
    try:
        Enviar_videos = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//ytcp-button[@id='upload-button']"))
        )
        Enviar_videos.click()
    except Exception:
        print(f'{traceback.format_exc()}')
    dormir(10)
    try:
        selecionar_videos = WebDriverWait(nav , 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH , "//ytcp-button[@id='select-files-button']"))
        )
        selecionar_videos.click()
    except Exception:
        print(f'{traceback.format_exc()}')
    dormir(10)
    arquivos_string = ""
    
    for arquivos in listar(caminho_da_pasta):
        file = juntar(caminho_da_pasta , arquivos)
        if e_um_arquivo(file):
            caminhos_absolutos = caminho_absoluto(file)
            arquivos_string = arquivos_string + f' "{str(caminhos_absolutos)}"'
    
    dormir(10)
    pyperclip.copy(str(arquivos_string))
    dormir(10)
    pyautogui.hotkey('ctrl','v')
    print("dados escritos com sucesso !!!")
    dormir(10)
    
    pyautogui.press("ENTER")
    print("enviando os dados")
    
    return nav

prompt_tema('create')
delete_dirs_start(reparticoes(2),'bin',None)
delete_dirs_start(None,'core',None)
delete_dirs_start(None,'prompt',None)
#_________________Exibindo_________________#
exibir_mensagem(mensagem(None)['M-01'],0.02)
exibir_mensagem(mensagem(None)['M-02'],0.02)
exibir_mensagem(mensagem(None)['M-03'],0.02)
exibir_mensagem(mensagem(None)['M-04'],0.02)
exibir_mensagem(mensagem(None)['M-05'],0.02)
exibir_mensagem(mensagem(None)['M-06'],0.02)
exibir_mensagem(mensagem(None)['M-07'],0.02)
exibir_mensagem(mensagem(None)['M-08'],0.02)
exibir_mensagem(mensagem(None)['M-09'],0.02)
exibir_mensagem(mensagem(None)['M-10'],0.02)
exibir_mensagem(mensagem(None)['M-11'],0.02)
for _ in range(6):
    print(mensagem(None)['break'])
exibir_mensagem(mensagem(None)['M-12'],0.02)
exibir_mensagem(mensagem(None)['M-04'],0.02)
#___________________Coleta______________________#
EMAIL = exibir_input(mensagem(None)['M-13'],0.02)

while not filtro_input(EMAIL,'email',None):

    EMAIL = while_error('email',0.02)

SENHA = exibir_input(mensagem(None)['M-14'],0.02)

while not filtro_input(SENHA,'senha',None):

    SENHA = while_error('senha',0.02)

_TEMAS = {}

contador = 0
while contador < 6:

    contador = contador + 1

    texto = Cor.GREEN+f"{contador}° Termo: "+Cor.WHITE

    print(texto , end="" , flush=True)

    TEMA = exibir_input(mensagem(None)['M-15'],0.02)
    
    if str(TEMA).lower() == 'e':
        break
    
    _TEMAS[contador] = TEMA

CORE = exibir_input(mensagem(None)['M-16'],0.02)

while not filtro_input(CORE,'core',None):

    CORE = while_error('core',0.02)

exibir_reparticoes()

UDP = exibir_input(mensagem(None)['M-18'],0.02)

while not filtro_input(UDP,'udp',None):
    UDP = while_error('udp',0.02)

BIN = exibir_input(mensagem(None)['M-17'],0.02)

while not filtro_input(BIN,'bin',UDP):
    
    BIN = while_error('bin',0.02)

PROMPT = exibir_input(mensagem(None)['M-19'],0.02)

while not filtro_input(PROMPT,'prompt',None):
    
    PROMPT = while_error('prompt',0.02)

temas_ = temas(_TEMAS)

caminho = path(reparticoes(UDP),BIN)

temas_prompt(PROMPT,temas_,'prompt.txt')
#____________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________Google___________________________________________________________________________
loading(mensagem(None)['M-20'],0.02,0.05)
CMD('close',None)
loading(mensagem(None)['M-21'],0.02,0.05)
CMD('insert',caminho)
loading(mensagem(None)['M-22'],0.02,0.05)
CMD('close',None)

driver = undetected_chromedriver.Chrome(options=criar_configuracao(caminho))
driver = executar_com_auto_reset(button_login_selenium,driver,caminho)
driver = executar_com_auto_reset(input_login_email_selenium,driver,caminho,EMAIL)
driver = executar_com_auto_reset(input_login_send_selenium,driver,caminho)
driver = executar_com_auto_reset(input_login_password_selenium,driver,caminho,SENHA)
driver = executar_com_auto_reset(input_login_send_selenium,driver,caminho)
dormir(2)
driver.get("https://www.chatgpt.com/")
driver = executar_com_auto_reset(input_div_enter_account_gpt,driver,caminho)
driver = executar_com_auto_reset(input_continue_google_account_gpt,driver,caminho)
dormir(10)
driver = executar_com_auto_reset(input_value_prompt_gpt,driver,caminho,PROMPT)
CMD('close',None)
dormir(10)
prompt_tema('delete')
json_file(prompts_files(narracao,_TEMAS),CORE)
diretorio_ = juntar(CORE , 'prompts.json')
audio(CORE,'pt',diretorio_)
file_videos_aloqued = juntar(CORE , "Videos")
diretorio(file_videos_aloqued)
driver = undetected_chromedriver.Chrome(options=criar_configuracao(caminho))
driver = executar_com_auto_reset(video_login,driver,caminho)
driver = executar_com_auto_reset(video_input,driver,caminho,temas_,file_videos_aloqued)
dormir(10)
driver.quit()
CMD('close',None)
dormir(20)
new_past_videos = juntar(CORE , 'Videos_sem_audio')
new_past_shorts = juntar(CORE , 'Shorts_sem_audio')
if existir(new_past_shorts):
   remover(new_past_videos)
   remover(new_past_shorts)
diretorio(new_past_videos)
diretorio(new_past_shorts)
def new_video_duration(segundos):
    if str(segundos).isdigit():
        duration = 60 // int(segundos)
        return int(duration)
def get_videos_from_dir(dir,name):
    dirs_from_videos_alocked = []
    if existir(dir):
        for dado in listar(dir):
            file = juntar(dir , dado)
            if e_um_arquivo(file):
                if str(name) in file:
                    dirs_from_videos_alocked.append(file)
            else:
                return str("não é um arquivo")
    else:
        return str("diretorio não existe")
   
    return new_video_duration(len(dirs_from_videos_alocked))
def recortar_shorts(dir,name,new_duration,dir_dest):
     arquivos_temporarios = []
     past_for_shorts_temp = juntar(dir_dest , f"past_temp_{name}")
     if existir(dir):
         for idx,dado in enumerate(listar(dir)):
             file = juntar(dir , dado)
             if e_um_arquivo(file):
                 if not existir(past_for_shorts_temp):
                     diretorio(past_for_shorts_temp)
                 if str(name) in file:
                     video = VideoFileClip(file)
                     duracao = int(video.duration)
                    
                     target_width = 1080
                     target_height = 1920
                     scale_width = target_width / video.w
                     scale_height = target_height / video.h
                     scale = max(scale_width, scale_height)  #ANTES: 1920/video.h | AGORA: max()
                    
                     if duracao < new_duration:
                         redimensionado = video.resized(scale)
                         trecho: VideoClip = redimensionado.cropped(x_center=redimensionado.w/2,y_center=redimensionado.h/2,width=1080,height=1920).subclipped(0,duracao)
                     else:
                         redimensionado = video.resized(scale)
                         trecho: VideoClip = redimensionado.cropped(x_center=redimensionado.w/2,y_center=redimensionado.h/2,width=1080,height=1920).subclipped(0,new_duration)
                    
                     file_temp = juntar(past_for_shorts_temp , f'temp_{idx}.mp4')
                     trecho.write_videofile(file_temp)
                     arquivos_temporarios.append(file_temp)
                     trecho.close()
                     redimensionado.close()
                     video.close()
     else:
         return str("esse diretorio não existe !!!")
def shorts(dir,name,dir_dest):
    trechos = []
    new_past = juntar(dir_dest , 'Shorts_audioless')
    if not existir(new_past):
        diretorio(new_past)
    if existir(dir):
        for dado in listar(dir):
            pasta = juntar(dir , dado)
            for interdado in listar(pasta):
                file = juntar(pasta , interdado)
                if e_um_arquivo(file):
                    if str(name).replace(' ','-') in file:
                        files_videos = VideoFileClip(file)
                        trechos.append(files_videos)
    
    concatenar = concatenate_videoclips(trechos)
    arquivo = juntar(new_past , f'{name}.mp4')
    concatenar.write_videofile(arquivo)
    concatenar.close()
    for t in trechos:
        trecho:VideoClip = t
        trecho.close()

with open(f'{CORE}\\prompts.json','r',encoding='utf-8') as file:
    dados = carregar(file)
    for nome in dados:
        duration_new_video = get_videos_from_dir(f'{CORE}\\Videos',str(nome).replace(' ','-'))
        recortar = recortar_shorts(f'{CORE}\\Videos',str(nome).replace(' ','-'),duration_new_video,new_past_shorts)
with open(f'{CORE}\\prompts.json','r',encoding='utf-8') as file:
    dados = carregar(file)
    for nome in dados:
        duration_new_video = get_videos_from_dir(f'{CORE}\\Videos',str(nome).replace(' ','-'))
        shorts(f'{CORE}\\Shorts_sem_audio',str(nome).replace(' ','-'),CORE)

caminho_documentos_mp4 = listar(f'{CORE}\\Shorts_audioless')
caminho_documentos_mp3 = listar(f'{CORE}\\Audios')
nome_do_caminho_do_documento_mp4 = f'{CORE}\\Shorts_audioless'
nome_do_caminho_do_documento_mp3 = f'{CORE}\\Audios'
caminho_documento_ttl = juntar(CORE,'Shorts_com_Audio')
if not existir(caminho_documento_ttl):
    diretorio(caminho_documento_ttl)
with open(f'{CORE}\\prompts.json','r',encoding='utf-8') as file:
    dados = carregar(file)
    for nome in dados:
        for documentos_mp4 in caminho_documentos_mp4:
            mp4 = juntar(nome_do_caminho_do_documento_mp4 , documentos_mp4)
            for documentos_mp3 in caminho_documentos_mp3:
                mp3 = juntar(nome_do_caminho_do_documento_mp3 , documentos_mp3)
                if str(nome).replace(' ','-') in documentos_mp4 and str(nome).replace(' ','-') in documentos_mp3:
                    video = VideoFileClip(mp4)
                    audio = AudioFileClip(mp3)
                   
                    shorts_com_audio = video.with_audio(audio)
                    arquivo = juntar(caminho_documento_ttl , f'{nome}_com_audio.mp4')
                    shorts_com_audio.write_videofile(arquivo)
                   
                    fechar_video:VideoClip = video
                    fechar_audio:VideoClip = audio
                    fechar_short:VideoClip = shorts_com_audio
                   
                    fechar_video.close()
                    fechar_audio.close()
                    fechar_short.close()
                    
path_video_for_add_legends = f'{CORE}\\Shorts_com_Audio'
path_legen_for_add_legends = f'{CORE}\\prompts.json'
new_past_for_shorts_with_legends = juntar('core','shorts')
diretorio(new_past_for_shorts_with_legends)
with open(path_legen_for_add_legends , 'r' , encoding='utf-8') as file:
    nomes = carregar(file)
for nome in nomes:
    for arquivo in listar(path_video_for_add_legends):
        arquivo_full_path = juntar(path_video_for_add_legends , arquivo)
        if e_um_arquivo(arquivo_full_path):
            if str(nome).replace(' ','-') in arquivo_full_path:
                
                video = VideoFileClip(arquivo_full_path)
                
                #Divide o texto em palavras ou frases curtas
                texto_completo = str(nomes[nome])
                palavras = texto_completo.split()  #Separa por palavras
                
                #Calcula tempo por palavra
                tempo_por_palavra = video.duration / len(palavras)
                
                #Cria legendas animadas
                clips_legendas = []
                for i, palavra in enumerate(palavras):
                    inicio = i * tempo_por_palavra
                    
                    legenda = (
                        TextClip(
                            font='fonts\\ARIAL.TTF',
                            text=palavra,
                            font_size=90,
                            color='yellow',
                            stroke_color='black',
                            stroke_width=3,
                            method='caption',
                            size=(video.w - 100, None),
                            text_align='center'
                        )
                        .with_position(("center", video.h - 170))
                        .with_start(inicio)
                        .with_duration(tempo_por_palavra)
                    )
                    clips_legendas.append(legenda)
                
                #Compõe tudo junto
                path_shorts = juntar(new_past_for_shorts_with_legends, f'{nome}.mp4')
                final = CompositeVideoClip([video] + clips_legendas)
                final.write_videofile(path_shorts)
                
                #FECHA TUDO AQUI
                for legenda in clips_legendas:
                    legenda.close()
                video.close()
                final.close()
dormir(10)
driver = undetected_chromedriver.Chrome(options=criar_configuracao(caminho))
driver = executar_com_auto_reset(YouTube,driver,caminho,str(f'{CORE}\\shorts'))
dormir(20)
input("pressiona qualquer tecla para Finalizar o programa !!!")
driver.close()
pasta(CORE,None,'delete')
pasta(BIN,UDP,'delete')
pasta(PROMPT,None,'delete')