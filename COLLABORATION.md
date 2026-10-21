# A 和 B 的操作 / Работа A и B

平台选择 GitHub。先解压到独立学习目录。在 PyCharm Terminal、PowerShell 或 Git Bash 逐条执行 Git 命令。
Выбрана платформа GitHub. Распакуйте проект в отдельную учебную папку. Команды выполняются в терминале PyCharm, PowerShell или Git Bash.

## A 创建源仓库 / A создаёт исходный репозиторий

在 bookclub-docs 根目录执行以下命令。user.name 和 user.email 用本人提交身份替换，可使用平台提供的隐私邮箱。
Выполните команды в корне bookclub-docs. Замените имя и адрес данными своего автора коммитов, при необходимости используйте приватный адрес платформы.

```text
git --version
git init -b main
git config --local user.name "YOUR_NAME"
git config --local user.email "YOUR_NOREPLY_EMAIL"
git status --short
```

先逐项查看包内文件，确认无真实秘密和个人数据，再暂存和提交。占位符应先替换；不要照原样提交作者身份。
Сначала просмотрите файлы и убедитесь в отсутствии секретов и персональных данных. Замените заполнители автора перед коммитом.

```text
git add README.md .gitignore .gitattributes STORAGE_POLICY.md SOURCES.md
git add COLLABORATION.md docs api tools
git diff --cached --check
git diff --cached --stat
git diff --cached
git commit -m "Prepare bilingual course documentation"
git status
```

在本人 GitHub 账号中创建空的私有 bookclub-docs 仓库，不自动添加 README。复制真实 HTTPS 地址后，在 PowerShell 中执行：
Создайте пустой частный репозиторий bookclub-docs без автоматического README. Скопируйте фактический HTTPS адрес; в PowerShell выполните:

```powershell
$courseRepoUrl = Read-Host "Paste the real repository HTTPS URL"
git remote add origin $courseRepoUrl
git push -u origin main
```

确认远端可访问并授予 B 访问权限。身份验证由平台处理，令牌不保存到项目文件。
Подтвердите доступ и предоставьте B права. Аутентификация выполняется через платформу; токены не сохраняются в файлах.

## B 克隆并检查 / B клонирует и проверяет

B 在自己的独立学习父目录中执行，目标 bookclub-docs-b 必须尚不存在。B 使用自己的账号和提交身份。
B работает в своей учебной папке; каталог bookclub-docs-b ещё не должен существовать. Используются собственные учётная запись и автор коммитов.

```powershell
git --version
$courseRepoUrl = Read-Host "Paste the real repository HTTPS URL"
git clone $courseRepoUrl bookclub-docs-b
Set-Location bookclub-docs-b
git config --local user.name "YOUR_NAME"
git config --local user.email "YOUR_NOREPLY_EMAIL"
git remote -v
git status
git log -1 --oneline
```

A 打开 docs/user-guide.md，B 打开 docs/admin-guide.md。双方各自检查命令输出和页面；此处只确定分工，不要求本步骤中额外修改和推送两份指南。
A открывает docs/user-guide.md, B — docs/admin-guide.md. Каждый самостоятельно проверяет команды и страницы; на этом шаге определяется разделение работы без обязательного редактирования руководств.
