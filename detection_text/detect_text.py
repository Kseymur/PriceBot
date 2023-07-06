import sentencepiece
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from PIL import Image
import pytesseract
import requests


# tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ka-ru")
# model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ka-ru")


pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

API_converter = 'f76d29f8c878bff3c169dc12'


def get_price_from_photo(image_path): # получает цену с фото
    custom_config = r'--oem 3 --psm 7 tessedit_char_whitelist=0123456789.,'
    price = pytesseract.image_to_string(image_path, config=custom_config)

    return price.replace(',','.')


def get_converted_price(price): # конвертирует цену с фото
    # Where USD is the base currency you want to use
    url = f'https://v6.exchangerate-api.com/v6/{API_converter}/latest/GEL'

    # Making our request
    response = requests.get(url)
    data = response.json()

    return data['conversion_rates']['RUB']*float(price)


def convert_to_rubles_and_kop(amount):
    rubles = int(amount)
    kop = round((amount - rubles) * 100)
    return rubles, kop


def get_description_from_photo(image_path): # получает описание товара с фото
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image, lang='kat+eng')
    #batch = tokenizer([text], return_tensors="pt")

   # generated_ids = model.generate(**batch)
    return text #tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]