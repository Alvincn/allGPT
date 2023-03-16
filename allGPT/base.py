from aip import AipSpeech
from aip import AipOcr
from aip import AipBodyAnalysis
from aip import AipImageClassify
from aip import AipImageProcess
from aip import AipNlp

APP_ID = 'Your APP_Id'
API_KEY = 'Your API_KEY'
SECRET_KEY = 'Your Secret_Key'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
client2 = AipOcr(APP_ID, API_KEY, SECRET_KEY)
client3 = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
client4 = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
client5 = AipImageProcess(APP_ID, API_KEY, SECRET_KEY)
client6 = AipNlp(APP_ID, API_KEY, SECRET_KEY)
