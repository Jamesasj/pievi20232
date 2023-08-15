Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

`
python -m venv .venv
.\.venv\Scripts\activate 
pip install pandas
pip freeze > requirements.txt
`
