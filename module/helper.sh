git clone https://github.com/samita100/rust.git
sleep 17400
cd rust
sleep 6
echo "Done at ==> $(date)" >> required.txt
sleep 4
git config --global user.email "samita100@yandex.com"
sleep 7
export GIT_USERNAME="samita100"
export GIT_PASSWORD="@Gm37155mm38985"
git config credential.helper '!f() { sleep 1; echo "username=${GIT_USER}"; echo "password=${GIT_PASSWORD}"; }; f'
sleep 3
git add .
sleep 6
git commit -am "Adding new Changes"
sleep 5
git push origin main
