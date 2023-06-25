# chatgpt with django

Describe your project here.

<details>
<summary>rye self update</summary>

``` PowerShell
> rye self update
Updating to latest
Checking checksum
Updated!

rye 0.9.0
commit: 0.9.0 (4fe886c47 2023-06-21)
platform: windows (x86_64)
self-python: cpython@3.11
symlink support: true
```

</details>

<details>
<summary>rye show</summary>

``` PowerShell
> cd path\to\Python\django\ChatGPT
> rye show
project: chatgpt
path: C:\Users\nagar\Development\Python\django\ChatGPT
venv: C:\Users\nagar\Development\Python\django\ChatGPT\.venv
target python: 3.8
venv python: cpython@3.11.3
PS C:\Users\nagar\Development\Python\django\ChatGPT> rye pin 3.11
pinned 3.11.3 in C:\Users\nagar\Development\Python\django\ChatGPT\.python-version
```

</details>

<details>
<summary>rye run</summary>

show all commands

``` PwerShell
> rye run --list
black
blackd
django-admin
dmypy
isort
isort-identify-imports
mypy
mypyc
normalizer
openai
pydoc
python
pythonw
sqlformat
stubgen
stubtest
tqdm
```

create django project

``` PowerShell
> rye run django-admin startproject chatbot_with_gpt
```

create django app

``` PowerShell
> cd path\to\Python\django\ChatGPT\chatbot_with_gpt
> rye run python manage.py startapp chatbot
```

run server

``` PowerShell
> rye run python manage.py runserver
```

</details>
