if [ -d Team105 ] 
then 
    cd Team105;
    git pull;
    cd ..;
else
    git clone git@github.com:sebuaa2019/Team105.git;
fi

rm Team105/*.pdf;
cp ./build/shattuckite-v*.pdf ./Team105;

git config user.email "2463765697@qq.com"
git config user.name "CNLHC"

cd Team105;
git add -A;
git commit -m "auto CI build";
git push;
