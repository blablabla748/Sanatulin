#руководство по гитхабу 
##1 ssh ключ
ssh-keygen -t ed25518 -C
##2 как добавить ssh ключ в github
cat ~/.ssh/id_ed25519.pub
в github settings ssh and gpg keys new ssg key 
add ssh key 
##3 как клонировать 
git clone git@github.com:blablabla748/Sanatulin.git
##4
git status проверить изменения
git add добавить все файлы в коммит
git push отправить изменения на GitHub
