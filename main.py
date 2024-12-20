# -*- coding: utf-8 -*-
#! /usr/bin/python3,11                                                                                                                   import os
import requests
import datetime
import time
import asyncio
import validators
from urllib.parse import urlparse
from sys import stdout
from colorama import Fore, Style, init
import logging                                                                                                                             
# Inisialisasi Colorama dan Logging                                                                                                        init(autoreset=True)
                                                                                                                                           # Pengaturan Logging yang benar
logging.basicConfig(
    filename='attack.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',  # Perbaiki dari levellevel menjadi levelname                                          datefmt='%Y-%m-%d %H:%M:%S'
)

# Fungsi untuk Logging Informasi Serangan
def log_attack_status(message, level='info', print_to_terminal=True):
    if level == 'info':
        logging.info(message)
        if print_to_terminal:
            print(f"{Fore.CYAN}|    [INFO] {message.ljust(63)}|")
    elif level == 'error':
        logging.error(message)
        if print_to_terminal:
            print(f"{Fore.RED}|    [ERROR] {message.ljust(63)}|")
    elif level == 'warning':
        logging.warning(message)
        if print_to_terminal:
            print(f"{Fore.YELLOW}|    [WARNING] {message.ljust(63)}|")


# Fungsi untuk Menampilkan Header PBLACK dengan Warna
def display_header():
    header_lines =[
    f"{Fore.YELLOW}                                                                            ",
    f"{Fore.RED}     _/ _/ _/     _/  _/ _/ _/   _/        _/       _/ _/    _/    _/   ",
    f"{Fore.RED}    _/       _/  _/  _/      _/ _/       _/ _/    _/        _/   _/    ",
    f"{Fore.RED}   _/       _/      _/      _/ _/       _/  _/  _/         _/  _/     ",
    f"{Fore.WHITE}   _/ _/ _/         _/ _/ _/   _/       _/   _/ _/         _/ _/      ",
    f"{Fore.WHITE}  _/               _/      _/ _/       _/ _/ _/  _/       _/   _/     ",
    f"{Fore.WHITE} _/               _/ _/ _/   _/ _/ _/ _/     _/   _/ _/  _/     _/     ",
    f"{Fore.CYAN}                                                                           ",
    f"{Fore.RED}╔═════════════════════════════════════════════════════════════════╗ ",   
    f"{Fore.RED}║\033[32m                 PASTBLACK IS A FALLING DARK ATTACK              {Fore.RED}║ ",
    f"{Fore.RED}║\033[33m              FOR THE PURPOSE OF RECOMMENDING ARROGANCE          {Fore.RED}║ ",
    f"{Fore.RED}║\033[34m                    THEN USE IT FOR GOOD PURPOSES                {Fore.RED}║ ",
    f"{Fore.RED}║\033[35m                           Design By: Kun'F                      {Fore.RED}║ ",
    f"{Fore.RED}╚═════════════════════════════════════════════════════════════════╝ ",    
    ]

# Tampilkan header dengan warna
    for line in header_lines:
        print(line)

# Fungsi untuk Meminta Input dari Pengguna dengan Tampilan Rapi
def get_user_input(prompt_message):
    print(f"{Fore.GREEN}|{' ' * 4}[?] {prompt_message.ljust(63)}|")
    return input(f"{Fore.YELLOW}{' ' * 4}> ").strip()

# Fungsi Countdown untuk Menampilkan Waktu Serangan
def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        remaining_time = (until - datetime.datetime.now()).total_seconds()
        if remaining_time > 1:
            stdout.flush()
            stdout.write(f"\r{Fore.BLUE}[*] {Fore.MAGENTA}P-BLACK {Fore.WHITE} FLOODING THE WEBS  {Fore.RED} התקפה רצה {Fore.YELLOW} :::.. {remaining_time:.2f}{' ' * 26}|")  
            stdout.write(f"\r{Fore.MAGENTA}[*] {Fore.CYAN}P-BLACK {Fore.YELLOW} FLOODING THE WEBS  {Fore.BLUE} התקפה רצה {Fore.WHITE} ::.. {remaining_time:.2f}{' ' * 26}|")
        else:
            stdout.flush()
            stdout.write(f"\r{Fore.MAGENTA}|    [*] Attack Done!{' ' * 53}|\n")
            print(f"{Fore.CYAN}|{'=' * 74}|")
            return

# Validasi URL dan Parsing Target
def get_target(url):
    if not validators.url(url):
        log_attack_status(f"URL tidak valid: {url}", level='error')
        raise ValueError(f"URL tidak valid: {url}")

    target = {
        'uri': urlparse(url).path or "/",
        'host': urlparse(url).netloc,
        'scheme': urlparse(url).scheme,
        'port': urlparse(url).netloc.split(":")[1] if ":" in urlparse(url).netloc else ("443" if urlparse(url).scheme == "https" else "80")
    }
    log_attack_status(f"Target: {target['host']} ({target['scheme']}://{target['host']}:{target['port']}{target['uri']})")
    return target

# Fungsi Serangan Utama
def launch_attack(target_url, duration):
    target = get_target(target_url)

    # Inisialisasi Serangan dan Waktu Serangan
    log_attack_status(f"Attack {target['host']} for {duration} second...")
    countdown(duration)

if __name__ == "__main__":
    # Tampilkan Header
    display_header()

    # Prompt untuk input dari pengguna dengan tampilan yang rapi
    target_url = get_user_input("URL:   ")
    while not validators.url(target_url):
        print(f"{Fore.RED}|    [ERROR] URL tidak valid. Coba lagi.{' ' * 37}|")
        print(f"{Fore.CYAN}|{'=' * 74}|")
        target_url = get_user_input("URL: ")

    try:
        attack_duration = int(get_user_input("Duration: "))
    except ValueError:
        attack_duration = 60  # Default durasi

    # Luncurkan serangan
    launch_attack(target_url, attack_duration)

