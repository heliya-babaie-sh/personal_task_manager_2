# Personal Task Mananger 
![Static Badge](https://img.shields.io/badge/python-blue?logo=python&logoColor=white)

A simple  task manager built with Python

## Features
- Add multiple tasks 
- Saves tasks 
- loads saved tasks
- admin mode
- set tas priority

## Task priority 
Each task can have one of this priority levele:
- low
- medium
- high

## Requirements
- `python 3`
- `python-dotenv`
## Project structure
```text
personal_task_manager_ostad/
│   .env.example
│   .gitignore
│   main.py
│   README.md
│   requirments.txt
│   tasks.py
│
├───gifs/
│       task_demo.gif
│
├───image/
│       pic1.png

```
## Installation
install the required packages:
```bash
pip install -r requirements.txt
```
## Environment Setup
create a `.env` file in the project folde
Use `.env.example` as a templet
Add your admin password 
```env
admin_pass = your_passport_here
```
replaace `your_passport_here` with your own admin password.
## run the program 
run the main file:

```bash 
python main.py
```

## screen shot
![personal_task_manager_sccreen_shot](\image\pic.png)


## Demo
![personal_task_manager_demo](\gifs\demo_2.gif)