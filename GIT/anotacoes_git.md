## Anotações Voltada a Versionamento de Código
# *Sistemas de Controle de Versão*
Controlam as versões de um arquivo ao longo do desenvolvimento da aplicação:
- Registra o histórioco de atualizações de um arquivo
- Gerencia  quais foram as Alterações, data, autor e etc.
- Organização, controle e Segurança.

# *Tipos de VCS*
# VCS Centralizado: Subversion
- Repositório Único, existe um repositório central que contém todas as versões do código. 
Os desenvolvedores precisam se conectar a esse repositório central para fazer qualquer 
operação (checkout, commit, update), dependendo da conectividade para realizar operações.
- Backup simples, por ser Centralizado.
- Desempenho lento por depender do servidor central.
# VCS Distribuídos: Git
- Repositório local e completo, cada desenvolvedor possui uma copida completa incluindo
todo histórioco de mudança. Permite operações por não depender da conexão com servidor 
local, podendo ser feita quando conveniente.
- A chance de perder algum arquivo e menos provável por possuir diversas cópias.
- Complexidade de sincronização.

# *GIT*
- Open source
- Permite ramificações e fusões eficientes
- Leve e rápido

# *Anotações de configuração*
- global: Configurações para o usuário atual, aplicadas a todos os repositórios do usuário.
- local: Configurações para o repositório atual, aplicadas apenas a esse repositório específico.
- system: Configurações para todo o sistema, aplicadas a todos os usuários e repositórios no sistema.

# Gerar token no github, e a senha será o token: 
git config --global credential.helper "cache" ou "storage"

# Gerar autenticacao por SSH:
ssh-keygen -t ed25519 -C "email-git" - caso nao tiver chave SSH
adicinar chave a um local seguro:
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# *Comando Git*
# Config
```
git config --global user.name "nome-github"
git config user.name 
git config --global user.email emailutilizado
git config user.email 
git config init.defaultBranch               - indica qual o nome da branch padrão
git config --global init.defaultBranch nome - define o nome da branch padrão
```

# Uso
```
git init                   - inicia um repositório
rm -rf .git                - remove a inicializacao feita para um repositório
git remote origin "url"    - vincula repositório do github
git clone "url-github" "novo nome"
git remote -v              - mostra os repositórios vinculados
git status                 - mostra o status do repositório
git add                    - adiciona arquivos ao repositório
git commit -m "descricao"  - adiciona o commit juntamente a uma descricao 
```

# Restaurar arquivos modificados:
```
git restore "nome do arquivo"
```

# Alterar mensagem do último commit:
```
git log         - verifica histórico do último commit
git commit --ammend -m "nova mensagem"
```

# Desfazer último commit:
```
git log
git reset --soft "id commit"  - Adiciona os arquivos na área de preparacao
git reset --mixed "id commit" - Remove da área de preparacao 
git reset --hard "id commit"  - Remove tudo
git reflog                    
```

# Enviar commits e receber alterações
```
git push -u origin main
git pull
```

## *Branches*
- Uma ramificação do projeto
- Um pónteiro móvel para um commit no histórico do repositório
- Um branch criada a partir de outra Branch, aponta o mesmo commit da Branch inicial

# Criar branche
```
git checkout -b teste            - cria e altera para branch criada
git checkout "nome da branche"   - altera para branch
```

# Listar branches
```
git branch -v
git branch
``` 

# Mesclar Branches
```
git merge teste    - Junta a branch criada com a branch principal
```

# Excluindo Branches
```
git branch -d teste  - exclui a brach especificada
```