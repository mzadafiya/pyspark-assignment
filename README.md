# pyspark-assignment

pip3 install virtualenv

virtualenv --version

vi ~/.zshrc

export PATH=$PATH:/Users/mzadafiya/Library/Python/3.8/bin

source ~/.zshrc

virtualenv venv

source venv/bin/activate

git clone git@github.com:mzadafiya/pyspark-assignment.git

cd pyspark-assignment

git checkout assignment

pip3 install -r requirements.txt

nohup python3 covid-analysis.py &

python3 -m notebook
