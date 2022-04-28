1. create virtualenv with any name (here I use `myenv`)
```
pyenv virtualenv myenv
```

2. download `python-kms` and checkout the `kms_gdch` branch, and install 
```
git clone https://github.com/arithmetic1728/python-kms.git
cd python-kms
git checkout kms_gdch
pyenv local myenv
python -m pip install -e .
```

3. download `google-auth` and install
```
cd ..
git clone https://github.com/googleapis/google-auth-library-python.git
cd google-auth-library-python
pyenv local myenv
python -m pip install -e .
```

4. go to `python-kms/gdch_sample` folder, edit in the `gdch.json`.
```
export GOOGLE_APPLICATION_CREDENTIALS="./gdch.json"
python gdch_sample.py
```

