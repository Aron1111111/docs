# Git案例实践五项任务 / Практикум Git Пять заданий

此页面为Word报告的网页版；命令哈希是本地练习历史，可用bundle恢复。
Это веб-версия отчёта Word. Хеши относятся к учебной истории, восстанавливаемой из bundle.


作者 Aron    日期2026年10月22日
Автор Aron    Дата 22.10.2026

已完成本地仓库、分支合并、价格冲突处理和版本标签；另附PR书面方案及两种分支策略选择。
Выполнены создание репозитория, слияние веток, разрешение конфликта и тег. Добавлены письменный план PR и выбор стратегий.

环境：Git 2.51.1，Bash终端。由Aron独立完成操作与复核；aron@example.com仅为本地练习邮箱。
Среда: Git 2.51.1, терминал Bash. Aron самостоятельно выполнил команды и проверку; aron@example.com — учебный локальный адрес.

## 任务1 创建第一个仓库 / Задание 1 Первый репозиторий

以下为逐条执行的命令和实际输出。无输出且退出码0表示命令成功。
Ниже приведены команды и фактический вывод. Отсутствие вывода при коде 0 означает успех.

```text
$ mkdir lab-git
[无输出 / Нет вывода; exit 0]
```

```text
$ cd lab-git
[无输出 / Нет вывода; exit 0]
```

```text
$ git init -b main
Initialized empty Git repository in /workspace/scratch/dbbed2acc316/tmp/git_case/lab-
git/.git/
```

```text
$ git config user.name "Aron"
[无输出 / Нет вывода; exit 0]
```

```text
$ git config user.email "aron@example.com"
[无输出 / Нет вывода; exit 0]
```

```text
$ echo "Проект: учебный" > readme.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git add readme.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git commit -m "Add readme"
[main (root-commit) 47d5c1c] Add readme
 1 file changed, 1 insertion(+)
 create mode 100644 readme.txt
```

```text
$ git log --oneline
47d5c1c Add readme
```

结果：main中有readme.txt和一个提交47d5c1c。-b main明确指定初始分支名称。
Результат: в main есть readme.txt и один коммит 47d5c1c. Параметр -b main задаёт имя начальной ветки.

## 任务2 分支与无冲突合并 / Задание 2 Ветки и слияние без конфликта

在feature-a新增a.txt，提交后切回main并合并，再检查文件内容与历史。
В feature-a создан a.txt. После коммита выполнены переход в main, слияние и проверка файла и истории.

```text
$ git branch feature-a
[无输出 / Нет вывода; exit 0]
```

```text
$ git switch feature-a
Switched to branch 'feature-a'
```

```text
$ echo "Функция A" > a.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git add a.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git commit -m "Add feature A"
[feature-a 2f27fa1] Add feature A
 1 file changed, 1 insertion(+)
 create mode 100644 a.txt
```

```text
$ git switch main
Switched to branch 'main'
```

```text
$ git merge feature-a
Updating 47d5c1c..2f27fa1
Fast-forward
 a.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 a.txt
```

```text
$ cat a.txt
Функция A
```

```text
$ git log --oneline
2f27fa1 Add feature A
47d5c1c Add readme
```

结果：main中a.txt内容为“Функция A”。历史只有两个提交；本次为快进合并，没有额外生成合并提交。
Результат: a.txt в main содержит «Функция A». В истории два коммита. Выполнено fast-forward без отдельного коммита слияния.

## 任务3 创建价格冲突 / Задание 3 Создание конфликта цены

共同起点为100卢布。price-up改为120，price-promo改为90；先合并price-up，再合并price-promo。
Общая цена — 100 рублей. price-up задаёт 120, price-promo — 90. Сначала объединена price-up, затем price-promo.

```text
$ echo "Цена: 100 рублей" > price.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git add price.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git commit -m "Add base price"
[main 7e8c651] Add base price
 1 file changed, 1 insertion(+)
 create mode 100644 price.txt
```

```text
$ git branch price-up
[无输出 / Нет вывода; exit 0]
```

```text
$ git branch price-promo
[无输出 / Нет вывода; exit 0]
```

```text
$ git switch price-up
Switched to branch 'price-up'
```

```text
$ echo "Цена: 120 рублей" > price.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git commit -am "Increase price"
[price-up ce9bbc6] Increase price
 1 file changed, 1 insertion(+), 1 deletion(-)
```

```text
$ git switch price-promo
Switched to branch 'price-promo'
```

```text
$ echo "Цена: 90 рублей" > price.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git commit -am "Set promotional price"
[price-promo e2dc07d] Set promotional price
 1 file changed, 1 insertion(+), 1 deletion(-)
```

```text
$ git switch main
Switched to branch 'main'
```

```text
$ git merge price-up
Updating 7e8c651..ce9bbc6
Fast-forward
 price.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

```text
$ git merge price-promo
Auto-merging price.txt
CONFLICT (content): Merge conflict in price.txt
Automatic merge failed; fix conflicts and then commit the result.
```

最后一条命令退出码为1，出现预期的同一行内容冲突；下一页继续解决。
Последняя команда вернула код 1: ожидаемый конфликт одной строки. Разрешение приведено на следующей странице.

## 任务3 解决冲突并检查历史 / Задание 3 Разрешение конфликта и проверка истории

```text
$ cat price.txt
  <<<<<<< HEAD
Цена: 120 рублей
  =======
Цена: 90 рублей
  >>>>>>> price-promo
```

最终选择促销价90卢布。本练习将促销视为当前有效规则，因此保留price-promo的价格；120卢布的修改仍可在历史中追溯。
Выбрана акционная цена 90 рублей. В упражнении акция считается действующим правилом. Изменение до 120 рублей сохранено в истории.

```text
$ echo "Цена: 90 рублей" > price.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git add price.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git commit -m "Resolve price conflict"
[main 192c9a7] Resolve price conflict
```

```text
$ git log --oneline --graph --all
*   192c9a7 Resolve price conflict
|\
| * e2dc07d Set promotional price
* | ce9bbc6 Increase price
|/
* 7e8c651 Add base price
* 2f27fa1 Add feature A
* 47d5c1c Add readme
```

## 完成后的实际检查 / Фактические проверки результата

price.txt为90卢布且无冲突标记；git status --porcelain=v1、git ls-files -u和git diff --check均无输出，退出码0。
price.txt содержит 90 рублей без маркеров. git status --porcelain=v1, git ls-files -u и git diff --check не дали вывода; код завершения 0.

main有6个提交；合并提交192c9a7的两个父提交为ce9bbc6和e2dc07d，双方历史均已保留。
В main 6 коммитов. У коммита слияния 192c9a7 два родителя: ce9bbc6 и e2dc07d. История обеих веток сохранена.

## 任务4 版本标签与合并请求 / Задание 4 Тег версии и запрос на слияние

先在已解决冲突的main上添加轻量标签v1.0.0，再创建修改readme.txt的分支。
Сначала в main после разрешения конфликта создан лёгкий тег v1.0.0, затем ветка для изменения readme.txt.

```text
$ git tag v1.0.0
[无输出 / Нет вывода; exit 0]
```

```text
$ git tag --list
v1.0.0
```

```text
$ git switch -c docs/readme-usage
Switched to a new branch 'docs/readme-usage'
```

```text
$ echo "Запуск: откройте readme.txt и price.txt." >> readme.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git add readme.txt
[无输出 / Нет вывода; exit 0]
```

```text
$ git commit -m "Explain how to inspect the exercise files"
[docs/readme-usage fe6d0b5] Explain how to inspect the exercise files
 1 file changed, 1 insertion(+)
```

```text
$ git diff main...docs/readme-usage -- readme.txt
diff --git a/readme.txt b/readme.txt
index ed8d9a8..2d70a43 100644
--- a/readme.txt
+++ b/readme.txt
@@ -1 +1,2 @@
 Проект: учебный
+Запуск: откройте readme.txt и price.txt.
```

```text
$ git switch main
Switched to branch 'main'
```

标签指向192c9a7；说明分支提交为fe6d0b5，尚未合并。回到main后工作区干净。
Тег указывает на 192c9a7. Коммит ветки документации — fe6d0b5, он ещё не объединён. После возврата в main рабочее дерево чистое.

## 书面说明如何发起PR / Письменный порядок создания PR

有远端仓库时，配置origin并推送main、标签和docs/readme-usage；在平台选择base为main、compare为docs/readme-usage，再填写标题、修改原因与检查结果。
При наличии удалённого репозитория настройте origin и отправьте main, тег и docs/readme-usage. На платформе выберите base main и compare docs/readme-usage, укажите заголовок, причину и проверки.

本题仅要求书面说明；本练习未配置远端、未实际创建线上PR。
Здесь требуется письменное описание; удалённый репозиторий не настроен, онлайн-PR не создан.

## 任务4 PR说明与审查内容 / Задание 4 Описание PR и проверка

## 可填写到PR中的说明 / Текст для описания PR

Title: Explain how to inspect the exercise files

修改内容：在readme.txt追加“打开readme.txt与price.txt”的操作说明，只修改一行文档。
Изменение: в readme.txt добавлена инструкция открыть readme.txt и price.txt. Добавлена одна строка документации.

修改原因：让首次查看练习仓库的读者知道应检查哪些文件。
Причина: новый читатель должен понимать, какие файлы нужно проверить.

验证：已检查diff，新增一行；price.txt仍为90卢布；v1.0.0仍指向解决冲突后的main；工作区干净。
Проверка: diff содержит одну новую строку; price.txt сохраняет 90 рублей; v1.0.0 указывает на main после разрешения конфликта; дерево чистое.

合并方式：审查通过后，将docs/readme-usage合并到main。本次保留所有练习分支，便于教师核对。
Слияние: после проверки объединить docs/readme-usage с main. Учебные ветки сохраняются для проверки преподавателем.

## 同学应检查的内容 / Что должен проверить коллега

1. 新增说明是否清晰，是否只涉及本次任务。
Понятна ли инструкция и соответствует ли она задаче.

2. readme.txt与price.txt是否真实存在，文件名是否正确。
Существуют ли readme.txt и price.txt, верны ли имена.

3. diff是否只有预期的一行，没有误删原内容或冲突标记。
Есть ли в diff только нужная строка, без случайных удалений и маркеров.

4. 价格是否仍为90卢布，标签是否仍指向预定版本。
Осталась ли цена 90 рублей и указывает ли тег на нужную версию.

5. 提交说明、源分支与目标main是否正确；有意见时先修正再复核。
Верны ли сообщение коммита, исходная ветка и main; замечания нужно исправить и проверить повторно.

本次已完成自检；上述同学审查为建议流程，没有虚构他人批准。
Самопроверка выполнена. Проверка коллегой описана как порядок действий, чужое одобрение не заявлено.

## 任务5 选择分支策略 / Задание 5 Выбор стратегии ветвления

## 场景一 每月发布并支持旧版本的移动应用 / Сценарий 1 Мобильное приложение с ежемесячным выпуском

选择Git Flow。该应用有固定版本和发布周期，还要维护旧版本，适合将日常开发、发布准备和紧急修复分开管理。
Выбор: Git Flow. Приложение имеет версии, регулярные выпуски и поддержку старых версий. Разработка, подготовка релиза и срочные исправления разделяются.

main保存已发布版本，develop汇总下一版功能，feature分支用于单项开发，release分支用于发布前测试，hotfix分支处理线上紧急问题。
main хранит выпущенную версию, develop объединяет функции следующей версии, feature используется для отдельных задач, release — для подготовки релиза, hotfix — для срочных исправлений.

针对题目中的旧版本支持，再保留maintenance/1.x等维护分支；旧版修复经验证后，同步到适用的新版与develop，避免修复遗漏。
Для поддержки старых версий дополнительно сохраняются ветки maintenance/1.x. Проверенные исправления переносятся в подходящие новые версии и develop, чтобы не потерять исправление.

## 场景二 每天更新多次的内部网站 / Сценарий 2 Внутренний сайт с несколькими обновлениями в день

选择GitHub Flow。main保持可部署；修改进入短期分支，经PR检查与审查后合并并部署。
Выбор: GitHub Flow. main готова к развёртыванию. Изменение выполняется в короткой ветке; после проверки PR оно объединяется и развёртывается.

理由：频繁的小更新需要快速反馈，短期分支减少等待与合并成本。本场景通常只维护当前线上版本，无需为每次更新设置release分支。
Обоснование: частым небольшим обновлениям нужна быстрая обратная связь. Короткие ветки сокращают ожидание и сложность слияний. Обычно поддерживается текущая версия сайта, отдельная release-ветка для каждого обновления не требуется.

## 参考资料 / Источники

GitHub Docs与Git Flow作者说明，查阅日期2026年10月22日。
GitHub Docs и описание автора Git Flow. Дата обращения 22.10.2026.

https://docs.github.com/en/get-started/using-github/github-flow

https://nvie.com/posts/a-successful-git-branching-model/
